from django.urls import path

from main.users.views import (
    task_trigger_fail_view,
    task_trigger_long_view,
    task_trigger_short_view,
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~task-trigger/", view=task_trigger_long_view, name="task-trigger-long"),
    path("~task-trigger-short/", view=task_trigger_short_view, name="task-trigger-short"),
    path("~task-trigger-fail/", view=task_trigger_fail_view, name="task-trigger-fail"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
