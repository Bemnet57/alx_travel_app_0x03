# alx_travel_app_0x03

## Background Task Management with Celery and Email Notifications

### Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Start RabbitMQ:

bash
Copy code
sudo systemctl start rabbitmq-server
Start Django server:

bash
Copy code
python manage.py runserver
Run Celery worker:

bash
Copy code
celery -A alx_travel_app worker -l info
Features
Celery configured with RabbitMQ.

Background task for sending booking confirmation emails.

BookingViewSet triggers async email task on booking creation.

Files
alx_travel_app/settings.py → Celery settings

alx_travel_app/celery.py → Celery app config

listings/tasks.py → Email task

listings/views.py → Task trigger