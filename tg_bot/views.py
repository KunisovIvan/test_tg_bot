import logging

from rest_framework.request import Request
from rest_framework.views import APIView, Response

from test_tg_bot import settings
from tg_bot.tg_bot import TgBot
from tg_bot.utils import send_phone_to_nova

log = logging.getLogger(__name__)


class IndexView(APIView):
    """Отвечает за работу с данными на главной странице."""

    def post(self, request: Request) -> Response:
        """Принимает post запросы"""

        log.info(f'view: IndexView, method: post, req: {request.data}')
        #
        bot = TgBot(settings.TG_TOKEN, request.data)
        #
        if bot.msg and bot.msg == '/start':
            bot.start(bot.chat_id)
        #
        if bot.contact:
            send_phone_to_nova(bot.contact['phone_number'], bot.username)
        #
        return Response(status=200)

    def get(self, request: Request) -> Response:
        """Принимает get запросы"""

        log.info(f'view: IndexView, method: get')
        return Response(status=200, data="Test tg bot.")
