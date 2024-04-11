from django.urls import path

from msngr.views import (
    index,
    UserListView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    UserCreateView
)

urlpatterns = [
    path("", index, name="index"),
    path("user/", UserListView.as_view(), name="users-list"),
    path("user/<int:pk>", UserDetailView.as_view(), name="user-detail"),
    path("user/<int:pk>/update", UserUpdateView.as_view(), name="user-update"),
    path("user/<int:pk>/delete", UserDeleteView.as_view(), name="user-delete"),
    path("user/create", UserCreateView.as_view(), name="user-create")

]

app_name = "msngr"
