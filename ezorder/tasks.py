from django.conf import settings
from background_task import background
import pusher

@background(schedule=0)
def track_order(channel):
    schedule_message(channel, 'Order received, we\'re picking the best vegetables for you', schedule=0)
    schedule_message(channel, 'We\'re on our way, we\'ll be there in 15 minutes', schedule=5)
    schedule_message(channel, 'Knock knock, Neo.', schedule=10)

_pusher = None
def get_pusher():
    global _pusher
    if not _pusher:
        _pusher = pusher.Pusher(
            app_id=settings.PUSHER_APP_ID,
            key=settings.PUSHER_KEY,
            secret=settings.PUSHER_SECRET,
            ssl=True,
            port=443
        )
    return _pusher

@background(schedule=3)
def schedule_message(channel, message):
    p = get_pusher()
    p.trigger(channel, 'notify', {'message': message})
