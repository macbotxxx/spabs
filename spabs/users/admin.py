from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportActionModelAdmin, ExportActionModelAdmin
from import_export import resources

from .forms import UserAdminChangeForm
from .forms import UserAdminCreationForm
from .models import User, JobPortal, JobEnrollment, Transactions

if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    # Force the `admin` sign in process to go through the `django-allauth` workflow:
    # https://docs.allauth.org/en/latest/common/admin.html#admin
    admin.autodiscover()
    admin.site.login = secure_admin_login(admin.site.login)  # type: ignore[method-assign]


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["email", "name", "is_superuser"]
    search_fields = ["name"]
    ordering = ["id"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


@admin.register(JobPortal)
class JobPortalAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'fee')
    list_display_links = ('job_title', 'fee')


@admin.register(JobEnrollment)
class JobEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('names', 'gender', 'job_categories')
    list_display_links = ('names', 'gender', 'job_categories')


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('job_aplicant', 'amount_paid', 'payment_ref')
    list_display_links = ('job_aplicant', 'amount_paid', 'payment_ref')


class JobEnrollmentResource(resources.ModelResource):
    class Meta:
        model = JobEnrollment


class TransactionsResource(resources.ModelResource):
    class Meta:
        model = Transactions
