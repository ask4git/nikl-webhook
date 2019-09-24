"""
to_slack.py
"""
# -*- coding: utf-8 -*-

import json
import requests

from conllu import parse
from collections import OrderedDict
from .url_slack import NIKL_SLACK_CH_URL
from .url_slack import FALLBACK_SLACK_CH_URL

import logging

logger = logging.getLogger()


def send_to_slack(json_data):
    """
    :param json_data:
    :return:
    """
    webhook_url = get_slack_channels_url(json_data["topicCategory"])

    # create message
    payload = create_slack_message(json_data)

    requests.post(
        webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'}
    )


def create_slack_message(json_data):
    """

    :param json_data:
    :return:
    """
    print(json.dumps(json_data))
    logging.warn(json.dumps(json_data))
    payload = {
        "username": '[{topicCategory}] [사용자이름]'.format(**json_data),
        "text": "",
        "attachments": [
            {
                "text": "",
                "fields": [
                    {
                        "title": "사용자",
                        "value": '[사용자이름] <{topicRequester}>'.format(**json_data),
                        "short": False
                    },
                    {
                        "title": "문장 ID",
                        "value": json_data["taskName"],
                        "short": True
                    },
                    {
                        "title": "어절",
                        "value": json_data["topicContext"]["word"],
                        "short": True
                    },
                    {
                        "title": "문장",
                        "value": "```{}```".format(json_data["topicContext"]["sentence"]),
                        "short": False
                    },
                    {
                        "title": "구문/의미역 분석결과",
                        "value": "```{}```".format(parse_simple_conllu(json_data["topicContext"]["source"])),
                        "short": False
                    },
                    {
                        "title": "내용",
                        "value": "```{}```".format(json_data["topicContent"]),
                        "short": False
                    }
                ],
                "color": "#5C6EA3",
                "attachment_type": "default",
                # "actions": [
                #     {
                #         "type": "button",
                #         "text": "작업도구 바로가기",
                #         "url": "https://app.deepnatural.ai/"
                #     },
                #     {
                #         "type": "button",
                #         "text": "답변하기",
                #         "url": ""
                #     }
                # ]
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

    channel_name = NIKL_SLACK_CH_URL.get(channel_name) or FALLBACK_SLACK_CH_URL
    return channel_name


def parse_simple_conllu(sentence):
    """

    :param sentence:
    :return:
    """
    token_list = parse(sentence)
    result = ''
    for token in token_list[0]:
        result += '\t'.join([str(token["id"]), token["form"], token["lemma"],
                             token["xpostag"], str(token["head"]), token["deprel"]])
        if type(token["misc"]) == OrderedDict:
            for key in token["misc"].keys():
                result += '\t' + key
        else:
            result += '\t_'
        result += '\n'
    return result
