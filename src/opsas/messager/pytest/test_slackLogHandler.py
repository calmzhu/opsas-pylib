import logging
import time

import pytest

from ..SlackLogHandler import SlackLogHandler
from ..SlackLogHandler import SlackMessager


@pytest.fixture(scope='class')
def bot(pytestConfiger, pytestLogger) -> SlackMessager:
    bot = SlackMessager(logger=pytestLogger, channel='opsas', token=pytestConfiger.get('slack_channel_token'))
    yield bot
    bot.session.close()


def pytest_namespace():
    return {"ts": None}


class TestSlackMessager:

    def test_send_message(self, bot: SlackMessager):
        res = bot.send_text_message("Hello Slack")
        pytest.ts = res['ts']
        return res['ts']

    def test_send_thread_message(self, bot: SlackMessager):
        res = bot.send_message(thread_ts=pytest.ts, message="Hello")
        assert res['ok'] is True


@pytest.fixture(scope="class")
def slackLogHandler(pytestConfiger, pytestLogger):
    slackLogHandler = SlackLogHandler(logger=pytestLogger, channel=pytestConfiger.get('slack_channel'),
                                      token=pytestConfiger.get('slack_channel_token'))
    return slackLogHandler


class TestSlackLogHandler:
    def test_log_levels(self, slackLogHandler):
        main = logging.getLogger('MainSlackLogHandler')
        main.addHandler(slackLogHandler)
        for log_method_name in ["info", "debug", "warning", "error", "critical"]:
            log_method = getattr(main, log_method_name)
            time.sleep(1)
            log_method(log_method_name)

    def test_thread_log_levels(self, slackLogHandler):
        thread = logging.getLogger('SubSlackLogHandler')
        slackLogHandler.create_session(thread.name)
        thread.addHandler(slackLogHandler)
        for log_method_name in ["info", "debug", "warning", "error", "critical"]:
            log_method = getattr(thread, log_method_name)
            time.sleep(1)
            log_method(log_method_name)
