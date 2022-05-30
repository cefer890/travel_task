from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class CustomerInformations(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    surname = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, null=True, blank=True)
    phone = PhoneNumberField(region='AZ')

    def __str__(self):
        return self.name


class PassportInformations(models.Model):
    KISI = 0
    QADIN = 1
    GENDER_TYPE = (
        (KISI, 'Kisi'),
        (QADIN, 'Qadin')
    )
    customer = models.ForeignKey(CustomerInformations, on_delete=models.CASCADE, related_name='customer')
    scan_file = models.FileField()
    document_number = models.CharField(max_length=9, blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    patronymic = models.CharField(max_length=60, blank=True, null=True)
    nationality = models.CharField(max_length=60, blank=True, null=True)
    birth_date = models.DateField()
    personal_number = models.CharField(max_length=7, blank=True, null=True)
    gender = models.SmallIntegerField(choices=GENDER_TYPE)
    issue_date = models.DateField()
    expire_date = models.DateField()
    issuing_authority = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.first_name