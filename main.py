import os
import random
import re

from flask import jsonify, make_response
from slackclient import SlackClient


def emoji_random(request):
    slack_token = os.environ.get('SLACK_TOKEN')
    if slack_token is None:
        print('SLACK_TOKEN is not set.')
        return
    client = SlackClient(slack_token)
    emojis = list(client.api_call('emoji.list')['emoji'].keys())

    text = request.form.get('text')

    print(f'text: {text}')
    r = text.split()

    if len(r) > 2:
        return "Usage: /emoji-random [pattern] [count]"
    elif len(r) == 2:
        cnt = min([int(r[1]), 100])
        selected = [e for e in emojis if re.search(r[0], e)]
        ret = f':{"::".join(random.choices(selected, k=cnt))}:'
    elif len(r) == 1:
        cnt = min([int(r[0]), 100])
        ret = f':{"::".join(random.choices(emojis, k=cnt))}:'
    else:
        ret = f':{random.choice(emojis)}:'

    d = {'response_type': 'in_channel', 'text': ret}
    return make_response(jsonify(d))
