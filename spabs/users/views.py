import random
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.http import JsonResponse
from django.db.models import Sum, Count
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from spabs.users.models import User, JobEnrollment, JobPortal, Transactions
from .forms import JobEnrollmentForm, FormatForm
from .filters import JobENrollmentFilter, TransactionsFilter
from .admin import JobEnrollmentResource, TransactionsResource



def generate_random_10_digits():
    return "".join([str(random.randint(0, 9)) for _ in range(10)])

@login_required()
def change_password(request):
    user_password = PasswordChangeForm(request.user)

    if request.method == 'POST':
        user_password = PasswordChangeForm(request.user, request.POST)
        if user_password.is_valid():
            user = user_password.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return reverse_lazy("users:list_agent_view")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_password = PasswordChangeForm(request.user)

    context = {
        'form': user_password,
    }
    return render(request, 'dashboard/password_change.html', context)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        # for mypy to know that the user is authenticated
        assert self.request.user.is_authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})


user_redirect_view = UserRedirectView.as_view()


class AboutView(TemplateView):
    template_name = "pages/about.html"


about_view = AboutView.as_view()


class ContactView(TemplateView):
    template_name = "pages/contact.html"


contact_view = ContactView.as_view()


class ProjectsView(TemplateView):
    template_name = "pages/projects.html"


projects_view = ProjectsView.as_view()


class CancelledView(TemplateView):
    template_name = "pages/cancelled.html"


cancelled_view = CancelledView.as_view()

class JobPortalsView(TemplateView):
    template_name = "pages/job_portal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs_qs'] = JobPortal.objects.all()
        return context


job_portal_view = JobPortalsView.as_view()


class EnrollmentFormView(ListView):
    model = JobEnrollment
    context_object_name = "job_portal_form"
    form_class = JobEnrollmentForm
    paginate_by = 100
    template_name = "pages/enrollment_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = JobEnrollmentForm()
        return context
    

enrollment_view = EnrollmentFormView.as_view()


class EnrolmentSubmit(TemplateView):
    template_name = "pages/upload.html"

    def post(self, request, *args, **kwargs):
        form = JobEnrollmentForm(request.POST, request.FILES)
        ref = generate_random_10_digits()
      
        if form.is_valid():
            aplicant=form.save()
            job_aplicant = JobEnrollment.objects.get(id=aplicant.id) 

            Transactions.objects.create(
                job_aplicant=aplicant,
                amount_paid=job_aplicant.job_categories.fee,
                payment_ref=f"SPABS_REF_{ref}",
            )
        
            # Return JSON response with validated inputs
            return JsonResponse({
                'success': True,
                'id': job_aplicant.id,
                'tx_ref': f"SPABS_REF_{ref}"
            })

        # Return JSON response indicating failure
        else:
            print(form.errors)  # Print form errors for debugging
            return JsonResponse({'success': False, 'errors': form.errors})


enrolment_verify_view = EnrolmentSubmit.as_view()


class InformationVerify(TemplateView):
    template_name = "pages/confirm_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aplicant_id = self.request.GET.get('id')
        if aplicant_id:
            id = aplicant_id.split('?')[0]        
        context["aplicant_qs"] = JobEnrollment.objects.get(id=id)
        return context


formation_verify = InformationVerify.as_view()


class PaymentVerify(TemplateView):
    template_name = "pages/pdf_page.html"

    def get(self, request, *args, **kwargs):
        status = request.GET.get('status')
        tx_ref = request.GET.get('tx_ref')
        transaction_id = request.GET.get('transaction_id')

        try:
            trans_qs = Transactions.objects.get(payment_ref=tx_ref)
        except Transactions.DoesNotExist:
            # Handle the case where the transaction does not exist
            return redirect('error_view')  # Redirect to an error page if the transaction does not exist

        if status == 'cancelled':
            trans_qs.settled = False
            trans_qs.status = status
            trans_qs.save()
            return redirect('cancelled_view')  # Replace 'cancelled_view' with your desired URL name or path
        else:
            # update the aplicant profile after payment
            aplicant_qs = JobEnrollment.objects.get(id=trans_qs.job_aplicant.id)
            aplicant_qs.completed_enrollment = True
            aplicant_qs.save()
            # save the transaction queryset
            trans_qs.settled = True
            trans_qs.status = status
            trans_qs.save()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tx_ref = self.request.GET.get('tx_ref')

        try:
            trans_qs = Transactions.objects.get(payment_ref=tx_ref)
            context['trans_qs'] = trans_qs
        except Transactions.DoesNotExist:
            context['trans_qs'] = None

        return context


payment_verify = PaymentVerify.as_view()


class DashboardIndex(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # fetching the job portal
        job_qs = JobEnrollment.objects.filter(completed_enrollment=True)
        job_category_list_count = job_qs.values('job_categories__job_title').annotate(total_enrollment=Count('job_categories'))
        tranx_qs =  Transactions.objects.filter(settled=True).aggregate(total_amount=Sum('amount_paid'))['total_amount']
        context['job_qs'] = job_category_list_count
        context['job_cat_count'] = job_qs.count()
        context['tranx_qs'] = tranx_qs
        return context


dashboard_index = DashboardIndex.as_view()


class EnrollmentList(LoginRequiredMixin, ListView):
    model = JobEnrollment
    context_object_name = "job_qs"
    template_name = "dashboard/enrollment.html"
    paginate_by = 100

    def get_queryset(self):
        queryset = JobEnrollment.objects.all()
        self.filter = JobENrollmentFilter(self.request.GET, queryset=queryset)
        return self.filter.qs

    def post(self, request, *args, **kwargs):
        export_format = request.POST.get('format')

        dataset = JobEnrollmentResource().export()
        if export_format == "xls":
            exported_data = dataset.export('xls')
            content_type = 'application/vnd.ms-excel'
            filename = 'enrollment_list.xls'
        elif export_format == "csv":
            exported_data = dataset.export('csv')
            content_type = 'text/csv'
            filename = 'enrollment_list.csv'
        else:
            # Default to JSON if format is not specified or unknown
            exported_data = dataset.export('json')
            content_type = 'application/json'
            filename = 'enrollment_list.json'

        response = HttpResponse(exported_data, content_type=content_type)
        response['Content-Disposition'] = f"attachment; filename={filename}"
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = JobENrollmentFilter()
        context['tranx_filter'] = self.filter
        context["form_export"] = FormatForm()
        context['count'] = self.filter.qs.count()
        return context


enrollment_list = EnrollmentList.as_view()


class TransactionsView(LoginRequiredMixin, ListView):
    template_name = "dashboard/transactions.html"
    model = Transactions
    context_object_name = "tranx_qs"
    paginate_by = 100

    def get_queryset(self):
        queryset = Transactions.objects.all()
        self.filter = TransactionsFilter(self.request.GET, queryset=queryset)
        return self.filter.qs

    def post(self, request, *args, **kwargs):
        export_format = request.POST.get('format')

        dataset = TransactionsResource().export()
        if export_format == "xls":
            exported_data = dataset.export('xls')
            content_type = 'application/vnd.ms-excel'
            filename = 'transaction_list.xls'
        elif export_format == "csv":
            exported_data = dataset.export('csv')
            content_type = 'text/csv'
            filename = 'transaction_list.csv'
        else:
            # Default to JSON if format is not specified or unknown
            exported_data = dataset.export('json')
            content_type = 'application/json'
            filename = 'transaction_list.json'

        response = HttpResponse(exported_data, content_type=content_type)
        response['Content-Disposition'] = f"attachment; filename={filename}"
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TransactionsFilter()
        context['tranx_filter'] = self.filter
        context["form_export"] = FormatForm()
        context['count'] = self.filter.qs.count()
        return context
    

transactions_view = TransactionsView.as_view()


class EnrollmentDetailsView(DetailView):
    model = JobEnrollment
    template_name = "dashboard/enrollment_details.html"
    context_object_name = "enrollment_qs"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     Enrollment_id_value = self.object.pk
    #     # Add additional context data if needed
    #     context["more_Enrollment"] = Enrollment.objects.all().order_by('-created_date')[:10]
    #     context["vote_form"] = EnrollmentVote(initial={'contestant_id': contestant_id_value})
    #     return context


enrollment_details = EnrollmentDetailsView.as_view()


