from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(user_email, booking_id):
    subject = "Booking Confirmation"
    message = f"Your booking with ID {booking_id} has been confirmed. Thank you for choosing us!"
    from_email = settings.DEFAULT_FROM_EMAIL

    try:
        send_mail(subject, message, from_email, [user_email])
        return f"Email sent to {user_email} for booking {booking_id}"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
