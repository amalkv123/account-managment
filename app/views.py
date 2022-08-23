from django.shortcuts import render,redirect
import os
from app.models import crtcompony,create_payhead,compute_information,Rounding,gratuity
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.

def base(request):
    return render(request, 'base.html')

def changecompany(request):
    return render(request, 'changecompany.html')

def createcompony(request):
    return render(request, 'createcompony.html')

def createcompony(request):
    return render(request, 'createcompony.html')

def createcompony(request):
    return render(request, 'createcompony.html')

def crtecompony(request):
    if request.method=='POST':
        comname=request.POST['componyname']
        mailingname=request.POST['mailingname']
        address=request.POST['address']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pincode']
        telphone=request.POST['telphone']
        mobile=request.POST['mobile']
        fax=request.POST['fax']
        email=request.POST['email']
        website=request.POST['website']
        fyearbgn=request.POST['fyearbgn']
        booksbgn=request.POST['booksbgn']
        curncysymbl=request.POST['curncysymbl']
        crncyname=request.POST['crncyname']
        # items=request.FILES['file']
        data=crtcompony(componyname=comname,
                    mailingname=mailingname,
                    address=address,
                    state=state,
                    country=country,
                    pincode=pincode,
                    telphone=telphone,
                    mobile=mobile,
                    fax=fax,
                    email=email,
                    website=website,
                    fyearbgn=fyearbgn,
                    booksbgn=booksbgn,
                    curncysymbl=curncysymbl,
                    crncyname=crncyname)
        data.save()
        messages.success(request,"Compony added successfully!")
        
        return redirect('/')

def selectcompony(request):
    data=crtcompony.objects.all()
    return render(request,'selectcompony.html',{'data':data})


#payroll




def profit(request):
    return render(request, 'profit.html')

def profitgroup(request):
    return render(request, 'profitgroup.html')

def expence(request):
    data=create_payhead.objects.all()
    return render(request, 'expence.html',{'p':data})

def expensemonth(request,pk):
    data=create_payhead.objects.get(id=pk)
    return render(request,'expensemonth.html',{'p':data})

def stockgroup(request):
    return render(request, 'stockgroup.html')

def ledger(request):
    return render(request,'ledger.html')





     #payheads





def payheads2(request):
    return render(request,'payheads.html')   


def add_payhead(request):
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
                           
        )
        std.save()
        idd=std

        std2=compute_information(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 slab_type=slabtype,
                                 value=value,
        )
        std2.save()

        std3=Rounding(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        messages.success(request,'successfully Added !!!')
        return redirect('payheads2')


def payhead_edit2(request,pk):
    if request.method=='POST':
        data=create_payhead.objects.get(id=pk)
        data.name=request.POST.get('name')
        data.alias=request.POST.get('alias')
        data.pay_type=request.POST.get('payhead')
        data.income_type=request.POST.get('income')
        data.under=request.POST.get('under')
        data.affect_net=request.POST.get('netsalary')
        data.payslip=request.POST.get('payslip')
        data.calculation_of_gratuity=request.POST.get('caltype')
        data.cal_type=request.POST.get('ctype')
        data.calculation_period=request.POST.get('caltype')
        data.leave_withpay=request.POST.get('attendence with pay')
        data.leave_with_out_pay=request.POST.get('Attendance with out pay')
        data.production_type=request.POST.get('ptype')
        data.opening_balance=request.POST.get('balance')
        data.save()

        idd=data

        data2=compute_information.objects.get(id=pk)
        data2.compute=request.POST.get('compute')
        data2.effective_from=request.POST.get('effective_from')
        data2.amount_upto=request.POST.get('amount_upto')
        data2.slab_type=request.POST.get('slab_type')
        data2.value=request.POST.get('value')
        data2.Pay_head_id=idd

        data2.save()


        data3=Rounding.objects.get(id=pk)
        data3.Rounding_Method=request.POST.get('roundmethod')
        data3.Round_limit=request.POST.get('limit')
        data3.pay_head_id=idd
        data3.save()

        data4=gratuity.objects.get(id=pk)
        data4.days_of_months=request.POST.get('days_of_months')
        data4.number_of_months_from=request.POST.get('from')
        data4.to=request.POST.get('to')
        data4.calculation_per_year=request.POST.get('eligiibility')
        data4.pay_head_id=idd
        data4.save()
        return redirect('payheads')
    return render(request,'payhead_edit.html')
    

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')



