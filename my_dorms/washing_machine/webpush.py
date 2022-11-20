from django.contrib.auth import get_user_model
from .models import Washing_Machine, Usage_Status, Reservation
from webpush import send_user_notification
from webpush.utils import send_to_subscription
from webpush import send_group_notification

import json # https://github.com/safwanrahman/django-webpush/issues/71

def machine_done_webpush(state, reserve_lst):
    # User = get_user_model()
    # users = User.objects.all()

    users = []
    users.append(state.user_id)

    for reserve in reserve_lst:
        users.append(reserve.user_id)

    payload = {"head": f"세탁완료", "body": f"{state.machine_id}의 세탁이 완료되었습니다."}

    for user in users:
        send_user_notification(user=user, payload=payload)
