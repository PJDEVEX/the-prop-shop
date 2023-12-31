from django.urls import path
from .views import CreateAccount, AllUsers, CurrentUser

app_name = "users"

urlpatterns = [
    path("create/", CreateAccount.as_view(), name="create-user"),
    path('all-users/', AllUsers.as_view(), name="all-users"),
    path('currentUser/', CurrentUser.as_view(), name="current-user"),
    # path('users/<int:pk>/', UserDetail.as_view(), name="user_detail"),

]
