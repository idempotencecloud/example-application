from django.shortcuts import render
#from django.core import serializers

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

from django.shortcuts import render
from .models import Company, Individual
from .forms import CompanyForm, IndividualForm

def index(request):
    if request.method == 'POST':
        print(request.POST)
        company_form = CompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
    else:
        company_form = CompanyForm({
            'company_name': 'Sample Company',
            'company_contact_email': 'personnel@example.com',
            'company_contact_phone': '1-800-555-5555',
            'accounts_receivable_email': 'ar@example.com',
            'company_type': 'CUSTOMER',
        })

    companies = Company.objects.all().order_by('-id')[0:10]
    context = {
        'company_form': company_form,
        'companies': companies,
    }
    return render(request, 'index.html', context)

def idempotenceAuthenticator(request):
    if(not request.user.is_authenticated):
        return JsonResponse({
            'authenticated': False
        })
    #https://en.wikipedia.org/wiki/ISO_8601
    #print(serializers.serialize("json", [request.user]))
    return JsonResponse({
        'legalName': "{} {}".format(request.user.first_name, request.user.last_name),
        'authenticationTimestamp': request.user.last_login,
        'userIdentifer': request.user.pk,
        'authenticated': True
    })