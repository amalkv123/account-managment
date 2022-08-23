from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('changecompany',views.changecompany,name='changecompany'),
    path('createcompony',views.createcompony,name='createcompony'),
    path('crtecompony',views.crtecompony,name='crtecompony'),
    path('selectcompony',views.selectcompony,name='selectcompony'),
    path('stockgroup',views.stockgroup,name='stockgroup'),
    path('profit',views.profit,name='profit'),
    path('payheads2',views.payheads2,name='payheads2'),
    path('add_payhead',views.add_payhead,name='add_payhead'),
    path('profitgroup',views.profitgroup,name='profitgroup'),
    path('expence',views.expence,name='expence'),
    path('expensemonth/<int:pk>',views.expensemonth,name='expensemonth'),
   




    
]