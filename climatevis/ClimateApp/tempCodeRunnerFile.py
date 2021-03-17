from django.urls import path

urlpatterns = [
    path(' ',views.IndexView,name="home"),
    path('dashboard/', views.dashboardView,name="dashboard"),
    path('login/',),
    path('register/',),
    path('logout/',),