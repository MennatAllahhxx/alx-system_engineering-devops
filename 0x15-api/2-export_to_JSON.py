#!/usr/bin/python3
"""2-export_to_JSON module"""

import json
import requests
import sys


def emp_info_json():
    """for a given ID, returns information about progress"""
    api_url = 'https://jsonplaceholder.typicode.com/users'
    usr_id = sys.argv[1]
    response = requests.get(f'{api_url}/{usr_id}').json()
    tasks = requests.get(f'{api_url}/{usr_id}/todos').json()
    usr_name = response.get('username')

    tasks_dict = []

    for task in tasks:
        tasks_dict.append({'task': task.get('title'),
                           'completed': task.get('completed'),
                           'username': usr_name})

    filename = f'{usr_id}.json'

    with open(filename, mode='w') as f:
        json.dump({usr_id: tasks_dict}, f)


if __name__ == '__main__':
    emp_info_json()
