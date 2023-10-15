from django.urls import path
from .views import CreateAccount, AllUsers, CurrentUser, UserDetail

app_name = "users"

urlpatterns = [
    path("create/", CreateAccount.as_view(), name="create_user"),
    path('users/', AllUsers.as_view(), name="all_users"),
    path('currentUser/', CurrentUser.as_view(), name="current_user"),
    path('user/<int:pk>/', UserDetail.as_view(), name="user_detail"),

]
