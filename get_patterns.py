import re
import requests
from bs4 import BeautifulSoup


def get_first_patttern(main_url, main_sauce):
    first_pattern = r'^(Episode)+\s+\d+$'  # e.g. Episode 01
    first_param = re.compile(first_pattern)
    for data in main_url:
        href = data['href']
        text = data.get_text()
        check = re.match(first_param, text)
        try:
            if check.group() in text:
                main_sauce.append({'title': text, 'link': href})
        except AttributeError:
            continue


def get_second_pattern(main_url, main_sauce):
    second_pattern = r'^(Episode)\s+\d+(-)\d+'  # e.g Episode 01-10
    second_param = re.compile(second_pattern)
    for data in main_url:
        href = data['href']
        text = data.get_text()
        check = re.match(second_param, text)
        try:
            if check.group() in text:
                url = data['href']
                director = url[0:24]
                req = requests.get(url)
                soup = BeautifulSoup(req.content, 'html.parser')
                data_link = soup.select('a[href*=mkv]')
                data_text = soup.select('div.flex-1.truncate')
                for x, y in zip(data_link, data_text[1:]):
                    link = x['href']
                    text = y.get_text()
                    href = f'{director}{link}'
                    main_sauce.append(
                        {'title': text.strip()[0:-4], 'link': href.strip()})
            else:
                pass
        except AttributeError:
            continue
