from django .urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('lossandprofit_profit',views.lossandprofit_profit,name='lossandprofit_profit'),
    path('stockgroup',views.stockgroup,name='stockgroup'),
    path('stock_item',views.stock_items,name='stock_items'),
    path('group',views.stock_groups,name="stock_groups"),
    path('payhead',views.payhead,name='payhead'),
    path('items/<int:pk>',views.item_list,name='item_list'),
    path('payhead_list',views.payhead_list,name='payhead_list'),
    path('ledger',views.ledger,name='ledger'),
    path('create_ledger',views.create_ledger,name='create_ledger'),
    path('sales',views.sales,name='sales'),
    path('indirect',views.indirect,name='indirect'),
    path('lossandprofit_grp_month/<int:pk>',views.lossandprofit_grp_month,name='lossandprofit_grp_month'),
    path('lossandprofit_sales_month/<int:pk>',views.lossandprofit_sales_month,name='lossandprofit_sales_month'),
    path('payhead/<int:pk>',views.payhead_month,name='payhead_month'),
    path('lossandprofit_stock_month/<int:pk>',views.lossandprofit_stock_month,name='lossandprofit_stock_month'),
    path('voucher/<int:pk>',views.pay_voucher,name='pay_voucher'),
    path('lossandprofit_stock_voucher/<int:pk>',views.lossandprofit_stock_voucher,name='lossandprofit_stock_voucher'),
    path('lossandprofit_purchase',views.lossandprofit_purchase,name='lossandprofit_purchase'),
    path('lossandprofit_direct_exprenses',views.lossandprofit_direct_exprenses,name='lossandprofit_direct_exprenses'),
    path('lossandprofit_indirect_expenses',views.lossandprofit_indirect_expenses,name='lossandprofit_indirect_expenses'),
    path('lossandprofit_stock_group2',views.lossandprofit_stock_group2,name='lossandprofit_stock_group2'),
    path('lossandprofit_items_2/<int:pk>',views.lossandprofit_items_2,name='lossandprofit_items_2')
]