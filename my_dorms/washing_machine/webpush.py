from django.contrib.auth import get_user_model

from webpush import send_user_notification
from webpush.utils import send_to_subscription
from webpush import send_group_notification

import json # https://github.com/safwanrahman/django-webpush/issues/71

def episode_webpush(episode):
    User = get_user_model()
    users = User.objects.all()

    payload = {"head": f"hi", "body": f"hi", 
            "url": f"123"}
     
    payload = json.dumps(payload) # json으로 변환 https://github.com/safwanrahman/django-webpush/issues/71

    for user in users:
        send_user_notification(user=user, payload=payload)
