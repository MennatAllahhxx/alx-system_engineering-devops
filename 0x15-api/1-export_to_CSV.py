#!/usr/bin/python3
"""1-export_to_CSV module"""

import csv
import requests
import sys


def emp_info_csv():
    """for a given ID, returns information about progress"""
    api_url = 'https://jsonplaceholder.typicode.com/users'
    usr_id = sys.argv[1]
    response = requests.get(f'{api_url}/{usr_id}').json()
    tasks = requests.get(f'{api_url}/{usr_id}/todos').json()
    usr_name = response.get('username')

    filename = f'{usr_id}.csv'

    with open(filename, mode='w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([usr_id, usr_name,
                             task.get('completed'),
                             task.get('title')])


if __name__ == '__main__':
    emp_info_csv()
