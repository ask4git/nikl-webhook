
# -*- coding: utf-8 -*-

import json
import requests

from .url_slack import TEST_URL


def send_to_slack(json_data):
    webhook_url = get_slack_channels_url(json_data["topicCategory"])

    # json 가공
    # ==================
    content = json_data
    # ==================

    payload = {"text": content}
    requests.post(
        webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'}
    )


def get_slack_channels_url(channel_name):
    """
    return Slack channel webhook url
    :param channel_name:
    :return:
    """
    test_url = TEST_URL    # test url
    url_nikl_0_notice = ''
    url_nikl_1_raw_corpus = ''
    url_nikl_2_pos = ''
    url_nikl_3_parsing = ''
    url_nikl_4_srl = ''
    url_nikl_5_tool = ''
    url_nikl_6_etc = ''

    if channel_name == "구문분석 문의":
        return test_url
    return ''
