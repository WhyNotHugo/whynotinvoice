from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.static import serve

from invoicing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '^invoices/pdf/<int:pk>$',
        views.SafeReceiptPDFDisplayView.as_view(),
        name='receipt_pdf_view',
    ),
    path(
        '^invoices/html/<int:pk>\d+)$',
        views.SafeReceiptHTMLView.as_view(),
        name='receipt_html_view',
    ),
    path(
        '^media/<str:path>$',
        serve,
        {'document_root': settings.MEDIA_ROOT},
    ),
]
