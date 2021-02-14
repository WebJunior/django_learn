import requests
from .models import TeleSettings


def send_telegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat_id)
        text = str(settings.tg_text)
        text = f'{text}\nИмя: {tg_name}\nТелефон: {tg_phone}'
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': text
        }

        r = requests.post(url, data=params)
        r.raise_for_status()


