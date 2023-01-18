from django.urls import path

from .views import DepositMoneyView, WithdrawMoneyView, transactionRepostView

app_name='transaction'

urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name='deposit_money'),
    path("repost/", transactionRepostView.as_view(),name='transaction_report'),
    path("withdraw/", WithdrawMoneyView.as_view(),name='withdraw_money'),
]



