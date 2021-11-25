from django.db import models

# Create your models here.
class Company():
    company_name = models.CharField(max_length=200)
    company_contact_email = EmailField(max_length=254)
    company_contact_phone = models.CharField(max_length=200)
    accounts_receivable_email = EmailField(max_length=254)
    company_type = models.CharField(
        max_length=2,
        choices=[
		('SUPPLIER', 'Supplier'),
		('VENDOR', 'Vendor'),
		('CUSTOMER', 'Customer')
	],
        default='SUPPLIER',
    )



class Individual(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    interested_in_marketing_email = models.BooleanField()
    customer_email = EmailField(max_length=254)
    company = ForeignKey('Company',
			 on_delete='models.CASCADE')
