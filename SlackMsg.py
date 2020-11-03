from slack import WebClient
import sys
import json

# Slack message

# if len(sys.argv)<1:
#    print
#    "Usage: python SlackMsg.py <channel> \"message\""

# channel = sys.argv[1]
# message = sys.argv[2]

# channel = '#automateslack'
# message = "How are you"

slack_token = 'Slack_token'
sc = WebClient(slack_token)

# result = sc.api_call("chat.postMessage", channel=channel, text=message)

result = sc.api_call(
  api_method='chat.postMessage',
  json={'channel': 'channel', 'text': 'Hello world!'}
)

# print result
