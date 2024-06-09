# summarization/urls.py

from django.urls import path
from .views import SummarizeTextView, SummarizeResultView

urlpatterns = [
    path('', SummarizeTextView.as_view(), name='summarize-text'),
    path('result/<task_id>/', SummarizeResultView.as_view(),
         name='summarize-result'),
]
