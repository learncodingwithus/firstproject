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

slack_token = 'xoxb-1363198843266-1386254372261-TjSF4PKGiv4GYcNaHIrAh0KV'
sc = WebClient(slack_token)

# result = sc.api_call("chat.postMessage", channel=channel, text=message)

result = sc.api_call(
  api_method='chat.postMessage',
  json={'channel': '#automateslack', 'text': 'Hello world!'}
)

# print result
