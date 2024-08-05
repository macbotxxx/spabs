import uuid

from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db.models import EmailField
from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _
from helpers.basemodels import BaseModel
from helpers.choices import ModelChoices

from .managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for spabs.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore[assignment]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})


class JobPortal(BaseModel):

    job_title = models.CharField(
        verbose_name=_("Job Title"),
        max_length=250,
        null=True,
    )

    fee = models.DecimalField(
        verbose_name=_("Enrollment Fee"),
        max_digits=20,
        decimal_places=2,
        null=True,
        help_text=_("this hold the fee")
    )

    description = models.TextField(
        verbose_name=_("Job Description"),
    )

    def __str__(self):
        return f"{self.job_title}"

    class Meta:
        ordering = [
            "-created_date",
        ]
        verbose_name = _("Job Portal")
        verbose_name_plural = _("Job Portal")


class JobEnrollment(BaseModel):
    names = models.CharField(
        verbose_name=_("Full Name"),
        max_length=250,
        null=True,
    )

    gender = models.CharField(
        choices=ModelChoices.GENDER,
        verbose_name=_("Gender"),
        max_length=10,
        null=True,
    )

    passport = models.ImageField(
        verbose_name=_("Passport"),
        upload_to='passport/',
        null=True
    )

    residential_address = models.CharField(
        verbose_name=_("Residential Address"),
        max_length=350,
        null=True,
    )

    state_of_residential = models.CharField(
        choices=ModelChoices.NIGERIAN_STATES,
        verbose_name=_("State Of Residential"),
        max_length=40,
        null=True,
    )

    local_gov_area = models.CharField(
        choices=ModelChoices.LOCAL_GOV,
        verbose_name=_("Local Gov Area"),
        max_length=100,
        null=True,
    )

    phone_number = models.CharField(
        verbose_name=_("Phone Number"),
        max_length=15,
        null=True,
    )

    date_of_birth = models.DateField(
        verbose_name=_("Job Title"),
        null=True,
    )

    place_of_birth = models.CharField(
        verbose_name=_("Place Of Birth"),
        max_length=250,
        null=True,
    )

    state_of_origin = models.CharField(
        choices=ModelChoices.NIGERIAN_STATES,
        verbose_name=_("State Of Origin"),
        max_length=40,
        null=True,
    )

    means_of_identification = models.CharField(
        choices=ModelChoices.IDENTIFICATION,
        verbose_name=_("Means Of Identification"),
        max_length=70,
        null=True,
    )

    identification_number = models.CharField(
        verbose_name=_("Identification Number"),
        max_length=150,
        null=True,
    )

    next_of_kin = models.CharField(
        verbose_name=_("Name Of Next Of Kin"),
        max_length=100,
        null=True,
    )

    referee = models.CharField(
        verbose_name=_("Name Of Referee"),
        max_length=100,
        null=True,
    )

    referee_phone_number = models.CharField(
        verbose_name=_("Referee Phone Number"),
        max_length=100,
        null=True,
    )

    job_categories = models.ForeignKey(
        JobPortal, on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Job Categories"),
    )

    completed_enrollment = models.BooleanField(
        verbose_name=_("Enrollment Completed"),
        default=False,
        null=True,
        help_text=_("this indicates if the enrollment process has been confirmed if the payment is completed")
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        ordering = [
            "-created_date",
        ]
        verbose_name = _("Job Enrollment")
        verbose_name_plural = _("Job Enrollment")


class Transactions(BaseModel):
    job_aplicant = models.ForeignKey(
        JobEnrollment, on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Job Aplicant"),
        help_text=_("this hold the aplicant details")
    )

    amount_paid = models.DecimalField(
        verbose_name=_("Amount Paid"),
        max_digits=20,
        decimal_places=2,
        null=True,
        help_text=_("this hold the amount paid")
    )

    payment_ref = models.CharField(
        verbose_name=_("Transaction Ref"),
        max_length=100,
        null=True,
        help_text=_("this hold the Transaction Ref for the current transaction")
    )

    voter_name = models.CharField(
        verbose_name=_("Voter Name"),
        max_length=100,
        null=True,
        help_text=_("this hold the Voter name of the contestant ")
    )

    settled = models.BooleanField(
        verbose_name=_("Payment Settled"),
        default=False,
        null=True
    )

    status = models.CharField(
        verbose_name=_("Status"),
        max_length=100,
        null=True,
        help_text=_("this hold the Voter name of the contestant ")
    )

    # def verify_payment_flutterwave(self):
    #     # paystack = PayStack()
    #     flutterwave = FlutterWave()
    #     status, result = flutterwave.verify_payment_flutterwave(self.payment_ref, self.amount_paid)
    #     if status == 'success':
    #         self.settled = True
    #         self.status = result['status']
    #         self.amount_paid = result['amount']

    #     self.save()

    #     return True

    class Meta:
        ordering = [
            "-created_date",
        ]
        verbose_name = _("Transactions")
        verbose_name_plural = _("Transactions")
