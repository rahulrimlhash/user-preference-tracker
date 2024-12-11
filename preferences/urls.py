from django.urls import path
from .views import RecordInteractionView, FetchPreferencesView

urlpatterns = [
    path('api/interaction', RecordInteractionView.as_view(), name='record_interaction'),
    path('api/preferences', FetchPreferencesView.as_view(), name='fetch_preferences'),
]
