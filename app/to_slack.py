
# -*- coding: utf-8 -*-

import json
import requests

from .url_slack import NIKL_SLACK_CH_URL


def send_to_slack(json_data):
    webhook_url = get_slack_channels_url(json_data["topicCategory"])

    # create message
    payload = create_slack_message(json_data)

    requests.post(
        webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'}
    )


def create_slack_message(json_data):
    payload = {
        "username": '[' + json_data["topicCategory"] + '] ' + json_data["topicRequester"],
        "text": "",
        "attachments": [
            {
                "text": "",
                "fields": [
                    {
                        "title": "사용자 ID",
                        "value": json_data["topicRequester"],
                        "short": False
                    },
                    {
                        "title": "문장 ID",
                        "value": json_data["taskName"],
                        "short": True
                    },
                    {
                        "title": "어절",
                        "value": json_data["context"]["word"],
                        "short": True
                    },
                    {
                        "title": "문장",
                        "value": "```" + json_data["context"]["sentence"] + "```",
                        "short": False
                    },
                    {
                        "title": "문의 내용",
                        "value": "```" + json_data["topicContent"] + "```",
                        "short": False
                    }

                ],
                "color": "#5C6EA3",
                "attachment_type": "default",
                "actions": [
                    {
                        "type": "button",
                        "text": "작업도구 바로가기",
                        "url": "https://app.deepnatural.ai/"
                    },
                    {
                        "type": "button",
                        "text": "답변하기",
                        "url": ""
                    }
                ]
            }
        ]
    }
    return payload


def get_slack_channels_url(channel_name):
    """
    return Slack channel webhook url
    :param channel_name:
    :return:
    """
    if channel_name in NIKL_SLACK_CH_URL:
        return NIKL_SLACK_CH_URL[channel_name]

    # need exception
    return None
