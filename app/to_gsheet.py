"""
to_gsheet.py
"""
# -*- coding: utf-8 -*-

from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from .url_gsheet import NIKL_GSHEET_URL
from .url_gsheet import FALLBACK_GSHEET_URL

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def send_to_gsheet(json_data):
    """
    :param json_data:
    :return:
    """
    gsheet_url = get_gsheet_url(json_data["topicCategory"])
    body = create_row_data(json_data)

    # json 파일로 서비스 계정 credential 정의
    credentials = ServiceAccountCredentials.from_json_keyfile_name('app/nikl-gsheet-key.json', SCOPES)
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
    data = {
        "values": [
            ['tq', '문장 id', '원시문장', '어절 id', 'word', '작업자', '작업자 계', '내용', '비고'],
        ]
    }
    return data


def get_gsheet_url(category_name):
    """

    :param sheet_file:
    :return:
    """
    gsheet_url = NIKL_GSHEET_URL.get(category_name) or FALLBACK_GSHEET_URL
    return gsheet_url
