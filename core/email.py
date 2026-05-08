import logging

from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def send_transactional_email(subject, message, recipient_list, from_email=None, html_message=None):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
    except Exception:
        logger.error(
            "Failed to send transactional email",
            extra={
                "subject": subject,
                "recipients": recipient_list,
            },
            exc_info=True,
        )
