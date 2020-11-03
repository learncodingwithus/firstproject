from slack import WebClient
import sys
import json

# Slack message

slack_token = 'Slack_token'
sc = WebClient(slack_token)

# result = sc.api_call("chat.postMessage", channel=channel, text=message)

result = sc.api_call(
  api_method='chat.postMessage',
  json={'channel': 'channel', 'text': 'Hello world!'}
)

# print result
