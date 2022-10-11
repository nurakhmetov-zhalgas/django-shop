from io import BytesIO

import weasyprint
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from orders.models import Order


@shared_task
def payment_completed(order_id):
    order = Order.objects.get(pk=order_id)
    subject = f"PLEAKLEY SHOP - Счет фактуры # {order.pk}"
    message = "Счет-фактуры за Вашу недавнюю покупку"
    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [order.email])
    html = render_to_string("orders/order/pdf.html", {"order": order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / "css/pdf.css")]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f"заказ_{order.pk}.pdf", out.getvalue(), "application/pdf")
    email.send()
