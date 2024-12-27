from django.urls import path # type: ignore
from .views import UserCreateView, TaskListCreateView, TaskDetailView, MarkTaskComplete

urlpatterns = [
    path("users/", UserCreateView.as_view(), name="user-create"),
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path(
        "tasks/<int:pk>/complete/",
        MarkTaskComplete.as_view(),
        name="mark-task-complete",
    ),
]
