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
    path('expensemonth2/<int:pk>',views.expensemonth2,name='expensemonth2'),
    path('purchase',views.purchase,name='purchase'),
    path('purchasemonth/<int:pk>',views.purchasemonth,name='purchasemonth'),
    path('purchasemonth2/<int:pk>',views.purchasemonth2,name='purchasemonth2'),
    path('indirect',views.indirect,name='indirect'),
    path('indirectmonth/<int:pk>',views.indirectmonth,name='indirectmonth'),
    path('indirectmonth2/<int:pk>',views.indirectmonth2,name='indirectmonth2'),
    path('stockgroup',views.stockgroup,name='stockgroup'),
    path('stock_groups',views.stock_groups,name='stock_groups'),
    path('stockitem',views.stockitem,name='stockitem'),
    path('stock_items',views.stock_items,name='stock_items'),
    path('ledger',views.ledger,name='ledger'),
    path('save_ledger',views.save_ledger,name='save_ledger'),
    path('item_list/<int:pk>',views.item_list,name='item_list'),
    path('sales',views.sales,name='sales'),
    path('simon',views.simon,name='simon'),
    path('sales_month/<int:pk>',views.sales_month,name='sales_month'),
    path('grp_month/<int:pk>',views.grp_month,name='grp_month'),
    path('payhead_list',views.payhead_list,name='payhead_list'),
    path('stock_month/<int:pk>',views.stock_month,name='stock_month'),
    path('stock_month2/<int:pk>',views.stock_month2,name='stock_month2'),
    
    
   




    
]