from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from django_afip import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^invoices/pdf/(?P<pk>\d+)$',
        views.ReceiptPDFDisplayView.as_view(),
        name='receipt_pdf_view',
    ),
    url(
        r'^invoices/html/(?P<pk>\d+)$',
        views.ReceiptHTMLView.as_view(),
        name='receipt_html_view',
    ),
    url(
        r'^media/(?P<path>.*)$',
        serve,
        {'document_root': settings.MEDIA_ROOT},
    ),
]
