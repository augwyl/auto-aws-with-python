# coding: utf-8
import json
import os
import requests

def post_to_slack(event, context):
    slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']

    print(slack_webhook_url)
    print(event)

    slack_message = "From {source} at {detail[StartTime]}: {detail[Description]}".format(**event)
    data = { "text": slack_message }
    requests.post(slack_webhook_url, json=data)

    return
