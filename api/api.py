import json
from typing import Union

import requests


def get_events(api_key: str, text: str = '', year: Union[int, str] = '',
               month: Union[int, str] = '', day: Union[int, str] = '', offset: Union[int, str] = ''):
    api_url = f'https://api.api-ninjas.com/v1/historicalevents?text={text}&year={year}&month={month}&day={day}&offset={offset}'.replace(' ', '%20').replace('None', '')
    print(api_url)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        return {'events': json.loads(response.text)}
    else:
        return {'code': response.status_code, 'text': response.text}
