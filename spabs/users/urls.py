from django.urls import path

from .views import user_detail_view
from .views import user_redirect_view
from .views import user_update_view
from . import views

app_name = "dashboard"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<int:pk>/", view=user_detail_view, name="detail"),
    path("change-password/", views.change_password, name="change_password"),
    path("index/", views.dashboard_index, name="dashboard_index"),
    path("enrollment-list/", views.enrollment_list, name="enrollment_list"),
    path("transaction-list/", views.transactions_view, name="transactions_view"),
    path("enrollment-details/<str:pk>/", views.enrollment_details, name="enrollment_details"),
]
