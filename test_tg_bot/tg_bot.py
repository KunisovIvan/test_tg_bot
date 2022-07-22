from typing import Optional

import requests


class TgBot:
    """Класс для работы с телеграм ботом."""

    def __init__(self, token: str, req: dict):
        self.base_url = f'https://api.telegram.org/bot{token}/'
        self.chat_id = req['message']['chat']['id']
        self.username = req['message']['chat']['username']
        self.msg = req['message'].get('text')
        self.contact = req['message'].get('contact')

    def start(self, chat_id: int) -> None:
        """Описывает действия при старте бота."""

        reply_markup = {
            "keyboard": [[
                {
                    "text": "Отправить телефон",
                    "request_contact": True
                },
            ]]
        }
        #
        self.send_massage(chat_id, 'Привет, а дай номер', reply_markup)

    def send_massage(
            self, chat_id: int,
            text: str,
            reply_markup: Optional[dict] = {}
    ) -> None:
        """Отправляет сообщение в чат."""

        url_send_msg = self.base_url + 'sendMessage'
        #
        requests.post(
            url_send_msg,
            json={
                'chat_id': chat_id, 'text': text, "reply_markup": reply_markup
            },
        )
