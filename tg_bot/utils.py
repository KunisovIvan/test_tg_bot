import requests


def send_phone_to_nova(phone: str, username: str) -> None:
    """Отправляет данные о контакте в Nova"""

    url_send_to_nova = 'https://s1-nova.ru/app/private_test_python/'
    requests.post(
        url_send_to_nova,
        json={
            'phone': phone,
            'login': username
        }
    )
