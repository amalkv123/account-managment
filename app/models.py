from django.db import models


    
    
    
    
class CreateStockGrp(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    quantities=models.CharField(max_length=50)


class group_summary(models.Model):
    CreateStockGrp=models.ForeignKey(CreateStockGrp, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    under=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,null=True)
    units=models.CharField(max_length=100,null=True)
    batches=models.CharField(max_length=100,null=True)
    manufacturing_date=models.CharField(max_length=100,null=True)
    expiry_dates=models.CharField(max_length=100,null=True)
    rate_of_duty=models.CharField(max_length=100,null=True)
    quantity=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    per=models.CharField(max_length=100,null=True)
    value=models.CharField(max_length=100,null=True)
    additional=models.CharField(max_length=100,null=True)
    
    
    
class payhead_crt(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    payhead_type=models.CharField(max_length=100,null=True)
    income_type=models.CharField(max_length=100,null=True)
    under_name=models.CharField(max_length=100,null=True)
    net_salary=models.CharField(max_length=100,null=True)
    pay_slip_name=models.CharField(max_length=100,null=True)
    currency_ledger=models.CharField(max_length=100,null=True)
    calculation_type=models.CharField(max_length=100,null=True)
    attendance_type=models.CharField(max_length=100,null=True)
    production_type=models.CharField(max_length=100,null=True)   
    
    
    
    

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
    compute=models.CharField(max_length=225,default="Null")
    effective_from=models.CharField(max_length=225,default="NULL")
    amount_greater=models.CharField(max_length=225,default="NULL")
    amount_upto=models.CharField(max_length=225,default="NULL")
    slab_type=models.CharField(max_length=225,default="NULL")
    value=models.CharField(max_length=225,default="NULL")
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)
    days_of_months=models.CharField(max_length=225)
    number_of_months_from=models.CharField(max_length=225)
    to=models.CharField(max_length=225)
    calculation_per_year=models.CharField(max_length=225)
    
class Companies(models.Model):
    d_path=models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=255)
    mailing_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=20,null=True)
    mobile = models.CharField(max_length=15,null=True)
    fax = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=240, null=True)
    website = models.CharField(max_length=100,null=True)
    currency_symbol = models.CharField(max_length=20)
    formal_name = models.CharField(max_length=20)
    fin_begin = models.DateField()
    books_begin = models.DateField()
    fin_end = models.DateField()
    status=models.BooleanField(default=True)

    
        
class tally_ledger(models.Model):
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255,null=True)
    under = models.CharField(max_length=255)
    
    mname = models.CharField(max_length=255,null=True,default=None)
    address = models.CharField(max_length=255,null=True,default=None)
    state = models.CharField(max_length=255,null=True,default=None)
    country = models.CharField(max_length=255,null=True,default=None)
    pincode = models.CharField(max_length=6,null=True,default=None)
    bank_details = models.CharField(max_length=20,null=True,default=None)
    pan_no = models.CharField(max_length=100,null=True,default=None)
    registration_type = models.CharField(max_length=100,null=True,default=None)
    gst_uin = models.CharField(max_length=100,null=True,default=None)
    set_alter_gstdetails = models.CharField(max_length=100,null=True,default=None)
    opening_blnc = models.IntegerField(null=True)

    set_odl = models.CharField(max_length=255,null=True,default=None)
    ac_holder_nm = models.CharField(max_length=255,null=True,default=None)
    acc_no = models.CharField(max_length=255,null=True,default=None)
    ifsc_code = models.CharField(max_length=255,null=True,default=None)
    swift_code = models.CharField(max_length=255,null=True,default=None)
    bank_name = models.CharField(max_length=255,null=True,default=None)
    branch = models.CharField(max_length=255,null=True,default=None)
    SA_cheque_bk = models.CharField(max_length=20,null=True,default=None)
    Echeque_p = models.CharField(max_length=20,null=True,default=None)
    SA_chequeP_con = models.CharField(max_length=20,null=True,default=None)
    
    type_of_ledger = models.CharField(max_length=100,null=True,default=None)
    rounding_method = models.CharField(max_length=100,null=True,default=None)
    rounding_limit = models.IntegerField(blank=True, null=True, default=None)

    type_duty_tax = models.CharField(max_length=100,null=True,default=None)
    tax_type = models.CharField(max_length=100,null=True,default=None)
    valuation_type = models.CharField(max_length=100,null=True,default=None)
    rate_per_unit = models.IntegerField(blank=True, null=True, default=None)
    percentage_of_calcution = models.CharField(max_length=100,null=True,default=None)
    rond_method = models.CharField(max_length=100,null=True,default=None)
    rond_limit = models.IntegerField(blank=True, null=True, default=None)

    gst_applicable = models.CharField(max_length=100,null=True,default=None)
    setalter_gstdetails = models.CharField(max_length=20,null=True,default=None)
    type_of_supply = models.CharField(max_length=100,null=True,default=None)
    assessable_value = models.CharField(max_length=100,null=True,default=None)
    appropriate_to = models.CharField(max_length=100,null=True,default=None)
    method_of_calculation = models.CharField(max_length=100,null=True,default=None)

    balance_billbybill = models.CharField(max_length=100,null=True,default=None)
    credit_period = models.CharField(max_length=100,default=0)
    creditdays_voucher = models.CharField(max_length=100,default=0)

class closebalance(models.Model):
    ledger_id = models.ForeignKey(tally_ledger, on_delete=models.CASCADE, null=True, blank=True)
    debit=models.CharField(max_length=225,default="0",blank=True)
    credit=models.CharField(max_length=225,default="0",blank=True)
    
class add_voucher(models.Model):
    date=models.CharField(max_length=225)
    particular=models.CharField(max_length=225)
    voucher_type=models.CharField(max_length=225)
    voucher_number=models.CharField(max_length=225)
    quntity=models.CharField(max_length=225)
    value=models.CharField(max_length=225)   
        
    def __str__(self):
        return self.particular    
    
    

class add_voucher2(models.Model):
    date=models.CharField(max_length=225,default="Null",blank=True)
    particular=models.CharField(max_length=225,default="Null",blank=True)
    voucher_type=models.CharField(max_length=225,default="Null",blank=True)
    voucher_number=models.CharField(max_length=225,default="Null",blank=True)
    debit=models.CharField(max_length=225,default="Null",blank=True)
    credit=models.CharField(max_length=225,default="Null",blank=True)

    def _str_(self):
        return self.particular    


