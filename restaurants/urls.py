from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

# router = routers.DefaultRouter()
# router.register('restaurants', views.RestaurantView)
# router.register('menu', views.MenuView)

urlpatterns = [
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('restaurants/', views.RestaurantListView.as_view(), name='restaurants'),
    path('menu/', views.MenuListView.as_view(), name='menu'),
    path('create_restaurant/', views.CreateRestaurantView.as_view(), name='create-restaurant'),
    path('register_manager/', views.RegisterUserManagerView.as_view(), name='register-manager'),
    path('managers/', views.ManagerListView.as_view(), name='managers'),
    path('create_employee/', views.CreateEmployeeView.as_view(), name='create-employee'),
    path('employee/', views.EmployeeListView.as_view(), name='employee'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('today_menu/', views.CurrentDayMenuList.as_view(), name="today-menu-list"),
    path('vote/<int:menu_id>/', views.VoteView.as_view(), name="menu-vote"),
    path('results/', views.ResultsView.as_view(), name="results"),
    path('upload_menu/', views.UploadMenuView.as_view(), name="upload-menu"),
]
