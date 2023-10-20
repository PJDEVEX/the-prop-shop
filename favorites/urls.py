from django.urls import path
from favorites import views

app_name = "favorites"

urlpatterns = [
    path("favorites/", views.FavoriteListCreate.as_view()),
    path(
        "favorites/<int:pk>/", views.FavoriteRetrieveDestroy.as_view()
    ),
]
