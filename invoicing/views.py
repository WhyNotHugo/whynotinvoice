from django.contrib.auth.mixins import LoginRequiredMixin
from django_afip import views


class SafeReceiptPDFDisplayView(
    LoginRequiredMixin,
    views.ReceiptPDFDisplayView,
):
    pass


class SafeReceiptHTMLView(
    LoginRequiredMixin,
    views.ReceiptHTMLView,
):
    pass
