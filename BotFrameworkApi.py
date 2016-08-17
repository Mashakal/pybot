# Constants.
_API_STRINGS = {
    'api': 'v3'
}


# Functions.
def _get_conversation_path(conversation_id):
    items = [
        _API_STRINGS['api'],
        'conversations',
        conversation_id,
        'activities'
    ]
    return '/'.join(items)

def _get_conversation_state_path(channel_id, conversation_id):
    items = [
        _API_STRINGS['api'],
        'botstate',
        channel_id,
        'conversations',
        conversation_id
    ]
    return '/'.join(items)


def build_message_url(data):
    base = data['serviceUrl']
    convo_id = data['conversation']['id']
    path = _get_conversation_path(convo_id)
    return '/'.join(p.rstrip('/') for p in [base, path])


def build_state_url(data):
    base = data['serviceUrl']
    channel_id = data['channelId']
    convo_id = data['conversation']['id']
    path = _get_conversation_state_path(channel_id, convo_id)
    return '/'.join(p.rstrip('/') for p in [base, path])



def main():
    data = {
        'serviceUrl': 'http://localhost:9000',
        'conversation': {
            'id': '8a684db8'
        },
        'channelId': 'emulator'
    }

    print(build_state_url(data))
    print(build_message_url(data))

if __name__ == "__main__":
    main()