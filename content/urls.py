from django.urls import path

from . import views

urlpatterns = [
    path("jobs/", views.jobs_list, name="api-jobs"),
    path("testimonials/", views.testimonials_list, name="api-testimonials"),
    path("stats/", views.stats_list, name="api-stats"),
    path("settings/", views.settings_dict, name="api-settings"),
    path("chatbot/", views.chatbot_reply, name="api-chatbot"),
    path("inquiries/", views.submit_project_inquiry, name="api-project-inquiries"),
]
