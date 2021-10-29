from datetime import *
import requests
import time


def get_questions(param):
    url = 'https://api.stackexchange.com/2.3/questions'
    response = requests.get(url, params=param)
    response.raise_for_status()
    return response.json()


def get_title(questions_list):
    out_list = []
    for elem in questions_list:
        out_list.append(elem.get("title"))
        # print(f'Question {i} - {elem.get("title")}')
    return out_list

day_now = int(time.mktime(datetime.now().timetuple()))
day_before = int(time.mktime((datetime.now() - timedelta(2)).timetuple()))
params = {
    'fromdate': f'{day_before}',
    'todate': f'{day_now}',
    'order': 'desc',
    'sort': 'activity',
    'tagged': 'python',
    'site': 'stackoverflow'
}

if __name__ == "__main__":
    print(get_title(get_questions(params).get('items')))
