from .views import IndexView, LoginView, LogoutView
from common.japan_stock_logs import DailyStockLogs, MonthlyStockLogs
from common.pak_stock_logs import PakDailyStockLogs, PakMonthlyStockLogs
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('japan/logs/daily', DailyStockLogs.as_view(), name='daily_logs'),
    path('japan/logs/monthly', MonthlyStockLogs.as_view(), name='monthly_logs'),
    path('pak/logs/daily', PakDailyStockLogs.as_view(), name='pak_daily_logs'),
	path('pak/logs/monthly', PakMonthlyStockLogs.as_view(), name='pak_monthly_logs'),
]
