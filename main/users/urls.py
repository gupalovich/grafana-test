from django.urls import path

from main.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    task_trigger_view,
    task_trigger_fail_view
)

app_name = "users"
urlpatterns = [
    path("~task-trigger/", view=task_trigger_view, name="task-trigger"),
    path("~task-trigger-fail/", view=task_trigger_fail_view, name="task-trigger-fail"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
