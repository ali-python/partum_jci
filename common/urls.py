from .views import IndexView, LoginView, LogoutView
from common.japan_stock_logs import DailyStockLogs, MonthlyStockLogs
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('logs/daily', DailyStockLogs.as_view(), name='daily_logs'),
    path('logs/monthly', MonthlyStockLogs.as_view(), name='monthly_logs'),


]
