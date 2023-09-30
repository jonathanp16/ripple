from django.urls import path

from ripple.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    user_references_view,
    reference_detail_view
)

app_name = "users"
urlpatterns = [

    # User views
    path("redirect/", view=user_redirect_view, name="redirect"),
    path("update/", view=user_update_view, name="update"),
    path("<int:pk>/references/", view=user_references_view, name="references"),    
    path("<int:pk>/", view=user_detail_view, name="detail"),

    # Reference views
    path("references/<int:pk>/", view=reference_detail_view, name="reference_detail"),
]
