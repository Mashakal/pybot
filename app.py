import os
import sys

import requests
from bottle import get, post, request, auth_basic

import BotFrameworkApi as api


if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    import bottle
    bottle.debug(True)


APP_ID = os.getenv("APP_ID", "YourAppId")
APP_SECRET = os.getenv("APP_SECRET", "YourAppSecret")


def check_auth(id, secret):
    return id == APP_ID and secret == APP_SECRET


_SENTINEL = object()


class MessageList:
    def __init__(self, d):
        self._d = d

    def __iter__(self):
        return map(Message.wrap, self._d)

    def __len__(self):
        return len(self._d)

    def __getitem__(self, index):
        return Message.wrap(self._d[index])

    def __setitem__(self, index, value):
        self._d[index] = value

    def __delitem__(self, index):
        del self._d[index]


class Message(dict):
    @classmethod
    def wrap(cls, obj):
        if isinstance(obj, dict):
            return cls(obj)
        if isinstance(obj, (list, tuple)):
            return MessageList(obj)
        return obj

    def __init__(self, d):
        object.__setattr__(self, '_d', dict(d) if d else None)

    def __getitem__(self, key):
        r = self.get(key, _SENTINEL)
        if r is _SENTINEL:
            raise KeyError(key)
        return self.wrap(r)

    def __setitem__(self, key, value):
        self._d[key] = value

    def __delitem__(self, key):
        del self._d[key]

    def get(self, key, default=None):
        if not self._d:
            return self
        r = self._d.get(key, _SENTINEL)
        if r is _SENTINEL:
            return default
        return self.wrap(r)

    def __getattr__(self, attr):
        r = self.get(attr, _SENTINEL)
        if r is _SENTINEL:
            return Message(None)
        return self.wrap(r)

    def __setattr__(self, attr, value):
        self._d[attr] = value

    def __delattr__(self, attr):
        del self._d[attr]

    def __dir__(self):
        return list(self) + object.__dir__(self)

    def __iter__(self):
        return self._d

    def __len__(self):
        return len(self._d)


import bot

@get('/')
def home():
    try:
        bot.home
    except AttributeError:
        pass
    else:
        return bot.home()
    
    return "TODO: home page"


@post('/api/messages')
#@auth_basic(check_auth)
def root():
    msg = Message(request.json)

    state_data = get_state_info(msg)

    try:
        state_data['data']
    except KeyError:
        print("Did not find any state data.")
        state_data['data'] = {}
    else:
        last_message = state_data['data']['last_message']

    print("Your last message was: {}".format(last_message))

    state_data['data']['last_message'] = msg.text

    try:
        handler = getattr(bot, msg.type)
    except AttributeError:
        res = "TODO: " + msg.type
    else:
        res = handler(msg)

    if isinstance(res, str):
        print("{}\n{}".format(msg.text, res))
        reply(msg, res)

    # Update the state data.
    send_state_data(msg, state_data)
    
    return


def reply(msg, text):
    """Sends text as a reply to msg in a conversation."""
    reply_data = format_message_for_reply(msg, text)
    path = api.build_message_url(reply_data)
    requests.post(path, json=reply_data)


def format_message_for_reply(message, response):
    """Constructs a dict from message and readies it for replying."""
    r = dict(message._d)
    r['from'], r['recipient'] = r['recipient'], r['from']
    r['text'] = response
    return r


def get_state_info(message):
    data = dict(message._d)
    path = api.build_state_url(data)
    response = requests.get(path)
    return response.json()

def send_state_data(message, state_data):
    data = dict(message._d)
    path = api.build_state_url(data)
    response = requests.post(path, json=state_data)


if __name__ == '__main__':
    import bottle

    # Starts a local test server.
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    bottle.run(server='wsgiref', host=HOST, port=PORT)
else:
    import bottle

    wsgi_app = bottle.default_app()
