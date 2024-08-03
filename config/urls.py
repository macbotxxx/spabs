# ruff: noqa
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from spabs.users import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", views.about_view, name="about",
    ),
    path(
        "contact/", views.contact_view, name="contact",
    ),
    path(
        "projects/", views.projects_view, name="projects",
    ),
    path(
        "job-portal/", views.job_portal_view, name="job_portal",
    ),
    path(
        "enrollment-form/", views.enrollment_view, name="enrollment_form",
    ),
    path(
        "details-verification/", views.formation_verify, name="formation_verify",
    ),
    path(
        "enrolment-verify/", views.enrolment_verify_view, name="enrolment_verify_view",
    ),
    path(
        "completed/", views.payment_verify, name="payment_verify",
    ),
    path(
        "cancelled/", views.cancelled_view, name="cancelled_view",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("spabs.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    # ...
    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
