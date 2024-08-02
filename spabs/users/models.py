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
        help_text=_("this hold the Job title of the current job")
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
        help_text=_("this hold the Job Description of the current job post ")
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
        help_text=_("this hold the first , last and maiden name")
    )

    gender = models.CharField(
        choices=ModelChoices.GENDER,
        verbose_name=_("Gender"),
        max_length=10,
        null=True,
        help_text=_("the gender of the applicant is required")
    )

    residential_address = models.CharField(
        verbose_name=_("Residential Address"),
        max_length=350,
        null=True,
        help_text=_("the current residential address of the applicant")
    )

    state_of_residential = models.CharField(
        choices=ModelChoices.NIGERIAN_STATES,
        verbose_name=_("State Of Residential"),
        max_length=40,
        null=True,
        help_text=_("current state of residential is needed")
    )

    local_gov_area = models.CharField(
        verbose_name=_("Local Gov Area"),
        max_length=100,
        null=True,
        help_text=_("local gov area of the residential state")
    )

    phone_number = models.CharField(
        verbose_name=_("Phone Number"),
        max_length=15,
        null=True,
        help_text=_("the applicant mobile number will be inputted")
    )

    date_of_birth = models.DateField(
        verbose_name=_("Job Title"),
        max_length=25,
        null=True,
        help_text=_("the applicant date of birth")
    )

    place_of_birth = models.CharField(
        verbose_name=_("Place Of Birth"),
        max_length=250,
        null=True,
        help_text=_("input the place of birth")
    )

    state_of_origin = models.CharField(
        choices=ModelChoices.NIGERIAN_STATES,
        verbose_name=_("State Of Origin"),
        max_length=40,
        null=True,
        help_text=_("current state of origin is needed")
    )

    means_of_identification = models.CharField(
        verbose_name=_("Means Of Identification"),
        max_length=40,
        null=True,
        help_text=_("kindly submit the means of identification which is needed")
    )

    next_of_kin = models.CharField(
        verbose_name=_("Name Of Next Of Kin"),
        max_length=100,
        null=True,
        help_text=_("the name of next of kin which will be passed by the applicant")
    )

    referee = models.CharField(
        verbose_name=_("Name Of Referee and Phone Number"),
        max_length=100,
        null=True,
        help_text=_("ythe name of the refree and phone number")
    )

    job_categories = models.ForeignKey(
        JobPortal, on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Job Categories"),
        help_text=_("the job categories should be selected by the applicant")
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
