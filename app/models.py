from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class crtcompony(models.Model):
    componyname = models.CharField(max_length=50)
    mailingname = models.CharField (max_length=50)
    address = models.CharField (max_length=50)
    state = models.CharField (max_length=50)
    country = models.CharField (max_length=50)
    pincode = models.CharField (max_length=10)
    telphone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    email=models.EmailField()
    website=models.CharField(max_length=100)
    fyearbgn=models.DateField()
    booksbgn=models.DateField()
    curncysymbl=models.CharField(max_length=10)
    crncyname=models.CharField(max_length=10)


class create_payhead(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    pay_type=models.CharField(max_length=225)
    income_type=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    affect_net=models.CharField(max_length=225)
    payslip=models.CharField(max_length=225)
    calculation_of_gratuity=models.CharField(max_length=225)
    cal_type=models.CharField(max_length=225)
    calculation_period=models.CharField(max_length=225)
    leave_withpay=models.CharField(max_length=225)
    leave_with_out_pay=models.CharField(max_length=225)
    production_type=models.CharField(max_length=225)
    opening_balance=models.CharField(max_length=225) 
    



class compute_information(models.Model):
    Pay_head_id = models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    compute=models.CharField(max_length=225,default="Null")
    effective_from=models.CharField(max_length=225,default="NULL")
    amount_greater=models.CharField(max_length=225,default="NULL")
    amount_upto=models.CharField(max_length=225,default="NULL")
    slab_type=models.CharField(max_length=225,default="NULL")
    value=models.CharField(max_length=225,default="NULL")



class Rounding(models.Model):
    pay_head_id = models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)


class gratuity(models.Model):
    pay_head_id=models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    days_of_months=models.CharField(max_length=225)
    number_of_months_from=models.CharField(max_length=225)
    to=models.CharField(max_length=225)
    calculation_per_year=models.CharField(max_length=225)   
