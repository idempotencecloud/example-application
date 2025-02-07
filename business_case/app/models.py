from django.db import models

# Create your models here.
class Company(models.Model):
    def __str__(self):
        return self.company_name
    company_name = models.CharField(max_length=200)
    company_contact_email = models.EmailField(max_length=254)
    company_contact_phone = models.CharField(max_length=200)
    accounts_receivable_email = models.EmailField(max_length=254)
    company_type = models.CharField(
        max_length=20,
        choices=[
		('SUPPLIER', 'Supplier'),
		('VENDOR', 'Vendor'),
		('CUSTOMER', 'Customer')
	],
        default='SUPPLIER',
    )



class Individual(models.Model):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    interested_in_marketing_email = models.BooleanField()
    customer_email = models.EmailField(max_length=254)
    company = models.ForeignKey('Company',
			 on_delete=models.CASCADE)
