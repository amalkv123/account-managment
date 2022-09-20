

from functools import total_ordering
from pickle import FALSE
from django.shortcuts import render,redirect
from .models import CreateStockGrp,group_summary,payhead_crt,create_payhead,tally_ledger,add_voucher,add_voucher2,closebalance

# Create your views here.


def index(request):
    return render(request,'base.html')

def lossandprofit_grp_month(request,pk):
    std=tally_ledger.objects.get(id=pk)
    vouch2=add_voucher2.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch2:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_debit-(int(std.opening_blnc)+total_credit)
    if opening_balance>0 :
        std.credit_period=opening_balance
        std.creditdays_voucher=0

        std.save()
        
    else :
        std.creditdays_voucher=opening_balance*-1
        std.credit_period=0
        std.save()
            
    return render(request,'lossandprofit_grp_month.html',{'std':std,'vouch2':vouch2,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def lossandprofit_sales_month(request,pk):
    std=tally_ledger.objects.get(id=pk)
    
    vouch2=add_voucher2.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch2:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_debit-(int(std.opening_blnc)+total_credit)
    
    # std.ledger_type=opening_balance
    # std.save()
    
    return render(request,'lossandprofit_sales_month.html',{'std':std,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})


def payhead_month(request,pk):
    std=create_payhead.objects.get(id=pk)
    vouch2=add_voucher2.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch2:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_debit-int(std.opening_balance)+total_credit
    return render(request,'month_payhead.html',{'std':std,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def pay_voucher(request,pk):
    std=create_payhead.objects.get(id=pk)
    vouch2=add_voucher2.objects.all()
    total_debit=0
    total_credit=0
    
    for i in vouch2 :
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_debit-int(std.opening_balance)+total_credit
    
    if opening_balance>0 :
        std.leave_withpay=opening_balance
        std.save()
        
    else :
        std.leave_with_out_pay=opening_balance*-1
        std.save()
    
    return render(request,'payhead_voucher.html',{'std':std,'vouch2':vouch2,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def lossandprofit_stock_voucher(request,pk):
    std=group_summary.objects.get(id=pk)
    vouch=add_voucher.objects.all()
    total_value=0
    total_qunity=0
    total_val=int(std.value)
    total_qun=int(std.quantity)
    for i in vouch:
        if (i.voucher_type=='sales'):
            total_value +=int(i.value)
            total_qunity+=int(i.quntity)
        elif (i.voucher_type=='purchase'):
            total_val+=int(i.value) 
            total_qun+=int(i.quntity)
    closing_qun=total_qun-total_qunity  
    closing_val=total_val-total_value 
    
    std.rate_of_duty=closing_val
    std.additional=closing_qun
    std.save()    
    
    context={
        'std':std,
        'vouch':vouch,
        'total_sales_value':total_value,
        'total_sales_quntity':total_qunity, 
        'total_purchase_value':total_val,
        'total_purchase_quntity':total_qun,
        'closing_qun':closing_qun,
        'closing_val':closing_val,
        }        
    return render(request,'lossandprofit_stock_voucher.html',context)


def lossandprofit_profit(request):
    balance=tally_ledger.objects.all()
    balance_py=create_payhead.objects.all()
    balance_le=tally_ledger.objects.all()
    balance_group=group_summary.objects.all()
    total_grp=0
    total_direct=0
    total=0
    total_income=0
    total_purch=0
    total_direct_exp=0
    total_indirect=0
    #sales account total
    for i in balance:
        if(i.under=='Sales_Account'):
            total+=int(i.credit_period)
            total+=int(i.creditdays_voucher)
            
    #indirect income total        
    for i in balance_py:
        if(i.under=='Income(Indirect)'):
            total_income+=int(i.leave_withpay)
            total_income+=int(i.leave_with_out_pay)
    for p in balance_le:
         if(p.under=='income_Indirect'):
             total_income+=int(p.credit_period) 
             total_income+=int(p.creditdays_voucher)
             
    #direct income total
             
    for i in balance_py:
        if(i.under=='Direct Incomes'):
            total_direct+=int(i.leave_withpay) 
            total_direct+=int(i.leave_with_out_pay) 
    
    for p in balance_le:
        if(p.under=='Direct Incomes'):
            total_direct+=int(p.credit_period) 
            total_direct+=int(p.creditdays_voucher)
            
    #closing stock
    for k in  balance_group:
        total_grp+=int(k.value)
        
    #purchase account total 
    
    for i in balance:
        if(i.under=='Purchase_Account'):
            total_purch+=int(i.credit_period)
            total_purch+=int(i.creditdays_voucher)
    
    #direct expenses total
           
    for i in balance_py:
        if(i.under=='Direct Expenses'):
            total_direct_exp+=int(i.leave_withpay) 
            total_direct_exp+=int(i.leave_with_out_pay)     
    
    for p in balance_le:
        if(p.under=='Direct_Expenses'):
            total_direct_exp+=int(p.credit_period) 
            total_direct_exp+=int(p.creditdays_voucher) 
            
    #indirect expenses total   
    
    for i in balance_py:
        if(i.under=='Indirect Expenses'):
            total_indirect+=int(i.leave_withpay)
            total_indirect+=int(i.leave_with_out_pay)
    for p in balance_le:
         if(p.under=='Expences_Indirect'):
            total_indirect+=int(p.credit_period) 
            total_indirect+=int(p.creditdays_voucher)    
            
    #closing stock
    std=group_summary.objects.all()
    vouch=add_voucher.objects.all()
    total_val=0
    total_qun=0
    total_value=0
    total_qunity=0
    
    for i in vouch:
        if (i.voucher_type=='sales'):
            total_value+=int(i.value)
            total_qunity+=int(i.quntity)
        elif (i.voucher_type=='purchase'):
            total_val+=int(i.value) 
            total_qun+=int(i.quntity)
       
    for p in std:
        total_val+=int(p.value)
        total_qun+=int(p.quantity)
                
    closing_value=total_val
    closing_quntity=total_qun-total_qunity        
            
                   
    return render(request,'lossandprofit_profit.html',{'total':total,'total_income':total_income,'total_direct':total_direct,'total_grp':total_grp,'total_purch':total_purch,'total_direct_exp':total_direct_exp,'total_indirect':total_indirect,'closing_value':closing_value,'closing_quntity':closing_quntity,}) 





def  payhead_list(request):
    std=create_payhead.objects.filter(under='Direct Incomes')
    stm=tally_ledger.objects.filter(group_under='Direct Incomes')
    balance=create_payhead.objects.all()
    balance_le=tally_ledger.objects.all()
    total=0
    total_d=0
    for i in balance:
        if(i.under=='Direct Incomes'):
            total+=int(i.leave_withpay)
            total_d+=int(i.leave_with_out_pay)
    for p in balance_le:
         if(p.group_under=='Direct Incomes') :
             total+=int(p.ledger_type) 
             total_d+=int(p.provide_banking_details)
         
    
    
    return render(request,'payhead_items.html',{'std':std,'stm':stm,'total':total,'total_d':total_d}) 



def lossandprofit_direct_exprenses(request):
    std=create_payhead.objects.filter(under='Direct Expenses')
    stm=tally_ledger.objects.filter(under='Direct_Expenses')
    total=0
    total_d=0
    for i in std:
        total+=int(i.leave_withpay)
        total_d+=int(i.leave_with_out_pay)
    for p in stm:
        total+=int(p.credit_period) 
        total_d+=int(p.creditdays_voucher)
    return render(request,'lossandprofit_direct_exprenses.html',{'std':std,'stm':stm,'total':total,'total_d':total_d}) 

def sales(request):
    std=tally_ledger.objects.filter(group_under='Sales_Account')
    balance=v.objects.all()
    total=0
    total_d=0
    for i in balance:
        if (i.group_under=='Sales_Account') :
            total+=int(i.ledger_type)
            total_d+=int(i.provide_banking_details)
        
                 
    return render(request,'sales_accounts.html',{'std':std,'total':total,'total_d':total_d})

def lossandprofit_purchase(request):
    std=tally_ledger.objects.filter(under='Purchase_Account')
    
    total=0
    total_d=0
    for i in std:
        total+=int(i.credit_period)
        total_d+=int(i.creditdays_voucher)
    return render(request,'lossandprofit_purchase_list.html',{'std':std,'total':total,'total_d':total_d})




def lossandprofit_stock_month(request,pk):
    std=group_summary.objects.get(id=pk)
    
    vouch=add_voucher.objects.all()
    total_value=0
    total_qunity=0
    total_val=int(std.value)
    total_qun=int(std.quantity)
    for i in vouch:
        if (i.voucher_type=='sales'):
            total_value +=int(i.value)
            total_qunity+=int(i.quntity)
        elif (i.voucher_type=='purchase'):
            total_val+=int(i.value) 
            total_qun+=int(i.quntity)
    closing_qun=total_qun-total_qunity  
    closing_val=total_val-total_value      
    context={
        'std':std,
        'vouch':vouch,
        'total_sales_value':total_value,
        'total_sales_quntity':total_qunity, 
        'total_purchase_value':total_val,
        'total_purchase_quntity':total_qun,
        'closing_qun':closing_qun,
        'closing_val':closing_val,
        }        
    
    return render(request,'lossandprofit_stock_month.html',context)

def item_list(request,pk):
    std=group_summary.objects.filter(CreateStockGrp_id=pk)
    vouch=add_voucher.objects.all()
    total=0
    total_qty=0
    total_value=0
    total_qunity=0
    
    for p in std:
        total_qun=int(p.quantity)
        total_val=int(p.value)
    # calculation of voucher
    for i in vouch:
        if (i.voucher_type=='sales'):
            total_value +=int(i.value)
            total_qunity+=int(i.quntity)
        elif (i.voucher_type=='purchase'):
            total_val+=int(i.value) 
            total_qun+=int(i.quntity)
            closing_qun=total_qun-total_qunity  
    closing_val=total_val-total_value 
   
    
    for i in std:
        total+=int(i.value)
        total_qty+=int(i.quantity)
        
    return render(request,'items.html',{'std':std,'total':total,'total_qty':total_qty,'closing_val':closing_val,'closing_qun':closing_qun,}) 
 
def lossandprofit_items_2(request,pk):
    ptm=group_summary.objects.filter(CreateStockGrp_id=pk)
    ptc=CreateStockGrp.objects.get(id=pk)
    
    vouch=add_voucher.objects.all()
    total=0
    total_qty=0
    total_value=0
    total_qunity=0
    
    for p in ptm:
        total_qun=int(p.quantity)
        total_val=int(p.value)
    # calculation of voucher
    for i in vouch:
        if (i.voucher_type=='sales'):
            total_value +=int(i.value)
            total_qunity+=int(i.quntity)
        elif (i.voucher_type=='purchase'):
            total_val+=int(i.value) 
            total_qun+=int(i.quntity)
            closing_qun=total_qun-total_qunity  
    closing_val=total_val-total_value 
   
    
    for i in ptm:
        total+=int(i.value)
        total_qty+=int(i.quantity)
        
    ptc.alias=total
    ptc.save()    
        
    return render(request,'lossandprofit_items_2.html',{'ptm':ptm,'closing_val':closing_val,'closing_qun':closing_qun,'total':total})
    
def stockgroup(request):
    ptm=CreateStockGrp.objects.all()
    std=group_summary.objects.all()
    vouch=add_voucher.objects.all()
    total_val=0
    total_qun=0
    total_value=0
    total_qunity=0
    
    for i in vouch:
        if (i.voucher_type=='sales'):
            total_value+=int(i.value)
            total_qunity+=int(i.quntity)
        elif (i.voucher_type=='purchase'):
            total_val+=int(i.value) 
            total_qun+=int(i.quntity)
       
    for p in std:
        total_val+=int(p.value)
        total_qun+=int(p.quantity)
                
    closing_value=total_val-total_value
    closing_quntity=total_qun-total_qunity
    return render(request,'stockgroup.html',{'std':std,'closing_value':closing_value,'closing_quntity':closing_quntity,'ptm':ptm})

def stock_item(request):
    ptm=CreateStockGrp.objects.all()
    std=group_summary.objects.all()
    total_val=0
    total_qun=0
    for p in std:
        total_val+=int(p.value)
        total_qun+=int(p.quantity)
        
    return render(request,'stockgroup_2.html',{'std':std,'opening_value':total_val,'opening_quntity':total_qun,'ptm':ptm})
    

def indirect(request):
    std=create_payhead.objects.filter(under='Income(Indirect)')
    stm=tally_ledger.objects.filter(group_under='income_Indirect')
    
    total=0
    total_d=0
    for i in std:
        total+=int(i.leave_withpay)
        total_d+=int(i.leave_with_out_pay)
    for p in stm:
        total+=int(p.ledger_type) 
        total_d+=int(p.provide_banking_details)
    
    
    return render(request,'indirect_income.html',{'std':std,'stm':stm,'total':total,'total_d':total_d})



def lossandprofit_indirect_expenses(request):
    std=create_payhead.objects.filter(under='Expences_Indirect')
    stm=tally_ledger.objects.filter(under='Expences_Indirect')
    
    total=0
    total_d=0
    for i in std:
        total+=int(i.leave_withpay)
        total_d+=int(i.leave_with_out_pay)
    for p in stm:
        total+=int(p.credit_period) 
        total_d+=int(p.creditdays_voucher)
    
    
    return render(request,'lossandprofit_indirect_expenses.html',{'std':std,'stm':stm,'total':total,'total_d':total_d})



def stock_groups(request):
    und=CreateStockGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        quantities=request.POST['quantities']
        stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities)
        stockgrp.save()
        return redirect('stock_items')
    return render(request,'group_stock.html',{'und':und})    



def lossandprofit_stock_group2(request):
    ptm=CreateStockGrp.objects.all()
    std=group_summary.objects.all()
    total_val=0
    total_qun=0
    for p in std:
        total_val+=int(p.value)
        total_qun+=int(p.quantity)
        
    return render(request,'lossandprofit_stockgroup_2.html',{'std':std,'opening_value':total_val,'opening_quntity':total_qun,'ptm':ptm})
    


def stock_items(request):
    grp=CreateStockGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        grp1=CreateStockGrp.objects.get(id=under)
        # category=request.POST['category',FALSE]
        units=request.POST['units']
        batches=request.POST['batches']
        manufacturing_date=request.POST['manufacturing_date']
        expiry_dates=request.POST['expiry_dates']
        rate_of_duty=request.POST['rate_of_duty']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        per=request.POST['per']
        value=request.POST['value']
        additional=request.POST['additional']
        crt=group_summary(name=name,alias=alias,under=under,units=units,batches=batches,
                           manufacturing_date=manufacturing_date,expiry_dates=expiry_dates,
                           rate_of_duty=rate_of_duty,quantity=quantity,rate=rate,per=per,value=value,additional=additional,CreateStockGrp=grp1)
        crt.save()
        return redirect('stock_items')
    return render(request,'stockitem.html',{'grp':grp})


def payhead(request):
    # att=attendance_crt.objects.all()
    pay=payhead_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        slabtype=request.POST['slab_type']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           compute=compute,
                           effective_from=effective_from,
                           #  amount_greater=amount_greaterthan,
                           amount_upto=amount_upto,
                           slab_type=slabtype,
                           value=value,
                           Rounding_Method=round_method,
                           Round_limit=limit,
                           days_of_months=days_of_months,
                           number_of_months_from=from_date,
                           to=to,
                           calculation_per_year=calculation_per_year,
                           
        )
        std.save()
        return redirect('payhead')
    return render(request,'payhead.html')   

        # std2=compute_information(Pay_head_id=idd,
        #                          compute=compute,
        #                          effective_from=effective_from,
        #                         #  amount_greater=amount_greaterthan,
        #                          amount_upto=amount_upto,
        #                          slab_type=slabtype,
        #                          value=value,
        # )
        # std2.save()

        # std3=Rounding(pay_head_id=idd,
        #              Rounding_Method=round_method,
        #              Round_limit=limit,
        # )
        # std3.save()

        # std4=gratuity(pay_head_id=idd,
        #              days_of_months=days_of_months,
        #              number_of_months_from=from_date,
        #              to=to,
        #              calculation_per_year=calculation_per_year,
        # )
        # std4.save()
        # messages.success(request,'successfully Added !!!')
         

def ledger(request):
    return render(request,'ledger.html')



def create_ledger(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        if request.method=='POST':
            nm=request.POST.get('name')
            als=request.POST.get('alias')
            under=request.POST.get('under')
            mname=request.POST.get('mailingname')
            adr=request.POST.get('address')
            st=request.POST.get('state')
            cntry=request.POST.get('country')
            pin=request.POST.get('pincode')
            pno=request.POST.get('pan_no')
            bdetls=request.POST.get('bank_details')
            rtype=request.POST.get('registration_type')
            gst_uin=request.POST.get('gst_uin')
            opnbn=request.POST.get('opening_blnc')

            spdl=request.POST.get('set_odl')
            achnm=request.POST.get('ac_holder_nm')
            acno=request.POST.get('acc_no')
            ifsc=request.POST.get('ifsc_code')
            scode=request.POST.get('swift_code')
            bn=request.POST.get('bank_name')
            brnch=request.POST.get('branch')
            sacbk=request.POST.get('SA_cheque_bk')
            ecp=request.POST.get('Echeque_p')
            sacpc=request.POST.get('SA_chequeP_con')

            typofled=request.POST.get('type_of_ledger')
            rometh=request.POST.get('rounding_method')
            rolmt=request.POST.get('rounding_limit')

            typdutytax=request.POST.get('type_duty_tax')
            taxtyp=request.POST.get('tax_type')
            valtype=request.POST.get('valuation_type')
            rateperu=request.POST.get('rate_per_unit')
            percalc=request.POST.get('percentage_of_calcution')
            rondmethod=request.POST.get('rond_method')
            roimlit=request.POST.get('rond_limit')

            gstapplicbl=request.POST.get('gst_applicable')
            sagatdet=request.POST.get('setalter_gstdetails')
            typsupply=request.POST.get('type_of_supply')
            asseval=request.POST.get('assessable_value')
            appropto=request.POST.get('appropriate_to')
            methcalcu=request.POST.get('method_of_calculation')

            balbillbybill=request.POST.get('balance_billbybill')
            credperiod=request.POST.get('credit_period')
            creditdaysvouch=request.POST.get('creditdays_voucher')
            
            ldr=tally_ledger(name=nm,alias=als,under=under,mname=mname,address=adr,state=st,country=cntry,
                            pincode=pin,pan_no=pno,bank_details=bdetls,registration_type=rtype,gst_uin=gst_uin,
                            opening_blnc=opnbn,set_odl=spdl,ac_holder_nm=achnm,acc_no=acno,ifsc_code=ifsc,swift_code=scode,
                            bank_name=bn,branch=brnch,SA_cheque_bk=sacbk,Echeque_p=ecp,SA_chequeP_con=sacpc,
                            type_of_ledger=typofled,rounding_method=rometh,rounding_limit=rolmt,type_duty_tax=typdutytax,tax_type=taxtyp,
                            valuation_type=valtype,rate_per_unit=rateperu,percentage_of_calcution=percalc,rond_method=rondmethod,rond_limit=roimlit,
                            gst_applicable=gstapplicbl,setalter_gstdetails=sagatdet,type_of_supply=typsupply,assessable_value=asseval,
                            appropriate_to=appropto,method_of_calculation=methcalcu,balance_billbybill=balbillbybill,credit_period=credperiod,
                            creditdays_voucher=creditdaysvouch,company_id=t_id)
            
            ldr.save()
            return render(request,'ledger.html',{'tally':tally})
    return redirect('/')