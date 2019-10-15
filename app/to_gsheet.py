"""
to_gsheet.py
"""
# -*- coding: utf-8 -*-

from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from app.keys.url_gsheet import NIKL_GSHEET_URL
from app.keys.url_gsheet import FALLBACK_GSHEET_URL
from datetime import datetime, timedelta
from .to_slack import id2name

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def send_to_gsheet(json_data):
    """
    :param json_data:
    :return:
    """
    gsheet_url = get_gsheet_url(json_data["topicCategory"])
    body = create_row_data(json_data)

    # json 파일로 서비스 계정 credential 정의
    credentials = ServiceAccountCredentials.from_json_keyfile_name('app/keys/nikl-gsheet-key.json', SCOPES)
    http_auth = credentials.authorize(Http())
    service = build('sheets', 'v4', http=http_auth)

    # request update
    request = service.spreadsheets().values().append(spreadsheetId=gsheet_url,
                                                     range='Sheet1!A:I',
                                                     valueInputOption='RAW',
                                                     body=body)

    # execute
    request.execute()


def create_row_data(json_data):
    """
    :param json_data:
    :return:
    """
    word = json_data["topicContext"]["word"].strip().split('] ')[1]
    word_id = str(json_data["topicContext"]["word"].strip().split('] ')[0][1:])
    data = {
        "values": [
            [str(datetime.now() + timedelta(hours=9)), json_data["taskName"], json_data["topicContext"]["sentence"],
             word_id, word, id2name(json_data["topicRequester"]),
             json_data["topicRequester"], json_data["topicContent"]],
        ]
    }
    return data


def get_gsheet_url(category):
    """
    :param category:
    :return:
    """
    gsheet_url = NIKL_GSHEET_URL.get(category) or FALLBACK_GSHEET_URL
    return gsheet_url
    # return FALLBACK_GSHEET_URL
