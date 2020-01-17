from logging import Handler

from opsas.utils.HttpSession import HttpSession


class SlackMessager(HttpSession):

    def __init__(self, logger, token, channel):
        super().__init__(logger, endpoint='https://slack.com/api')
        self.session.headers.setdefault('Authorization', 'Bearer ' + token)
        self.session.headers.setdefault('Content-Type', 'application/json')
        self.channel = channel

    def post_payload(self, payload):
        response = self.request_conn(method='post', path='/chat.postMessage', data=payload).json()
        self.logger.info(response)
        return response

    def send_text_message(self, message):
        payload = {
            'channel': self.channel,
            'text': message,
            'type': 'text'
        }
        return self.post_payload(payload)

    def send_message(self, message, infolevel="debug", thread_ts=None):
        payload = self.make_payload(message, infolevel, thread_ts=thread_ts)
        return self.post_payload(payload)

    def make_payload(self, message, loglevel, thread_ts=None):
        self.logger.debug(loglevel)
        payload = {
            'channel': self.channel,
            'blocks': [
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "image",
                            "image_url": f"http://img.justcalm.ink/{loglevel}.png",
                            "alt_text": f"{loglevel} icon"
                        },
                        {
                            "type": "mrkdwn",
                            "text": message
                        }
                    ]
                }
            ]
        }
        if thread_ts is not None:
            payload['thread_ts'] = thread_ts
        return payload


class SlackLogHandler(Handler):
    def __init__(self, token, channel, logger, title):
        super().__init__()
        self.bot = SlackMessager(token=token, channel=channel, logger=logger)
        self.msg_ts = self.start_slack_thread(title)

    def start_slack_thread(self, title):
        response = self.bot.send_text_message(title)
        return response['ts']

    def emit(self, record):
        msg = self.format(record)
        return self.bot.send_message(message=msg, infolevel=record.levelname.lower(), thread_ts=self.msg_ts)
