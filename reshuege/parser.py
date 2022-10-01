import json

import requests

from reshuege.academic_subjects import AcademicSubject
from reshuege.headers import headers


def parse_themes(subject: AcademicSubject) -> list:
    response = requests.get(subject.main_page_url + '/newapi/general', headers=headers, verify=False)
    data = json.loads(response.text)
    constructor = data['constructor']
    themes = []
    for item in constructor:
        themes.append({
            'title': item['title'].replace('\xad', ''),
            'name': item['name'],
        })
    return themes


def parse_constructor_item(item):
    if item['subtopics']:
        for sub_item in item['subtopics']:
            parse_constructor_item(sub_item)
    print(item)
