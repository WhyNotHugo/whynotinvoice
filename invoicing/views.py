from django.contrib.auth.mixins import LoginRequiredMixin
from django_afip import views


class SafeReceiptPDFView(
    LoginRequiredMixin,
    views.ReceiptPDFView,
):
    pass
