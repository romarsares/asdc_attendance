from django.db import models
from django.conf import settings
from core.models import BaseModel


class Member(BaseModel):

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    class CivilStatus(models.TextChoices):
        SINGLE = 'S', 'Single'
        MARRIED = 'M', 'Married'
        WIDOWED = 'W', 'Widowed'
        SEPARATED = 'SE', 'Separated'

    class Status(models.TextChoices):
        ACTIVE = 'A', 'Active'
        INACTIVE = 'I', 'Inactive'

    # Identity
    member_id = models.CharField(max_length=20, unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    suffix = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    birthdate = models.DateField()
    civil_status = models.CharField(max_length=2, choices=CivilStatus.choices)

    # Contact
    mobile = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    facebook = models.CharField(max_length=255, blank=True)

    # Home Address
    street = models.CharField(max_length=255, blank=True)
    region = models.ForeignKey('chapters.Region', on_delete=models.PROTECT, null=True, blank=True)
    province = models.ForeignKey('chapters.Province', on_delete=models.PROTECT, null=True, blank=True)
    municipality = models.ForeignKey('chapters.Municipality', on_delete=models.PROTECT, null=True, blank=True)
    barangay = models.ForeignKey('chapters.Barangay', on_delete=models.PROTECT, null=True, blank=True)

    # Photo
    id_photo = models.ImageField(upload_to='members/id_photos/', blank=True, null=True)

    # Status
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.ACTIVE)

    # User account (officers only)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def save(self, *args, **kwargs):
        if not self.member_id:
            self.member_id = self._generate_member_id()
        super().save(*args, **kwargs)

    def _generate_member_id(self):
        code = self.region.code.upper() if self.region else 'XX'
        count = Member.objects.filter(member_id__startswith=f"ASDC-{code}-").count()
        return f"ASDC-{code}-{count + 1:04d}"
