# Gets all the main data to download
import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
import json
from get_patterns import get_first_patttern, get_second_pattern


with open('sauce.json') as doc:
    data = json.load(doc)
    links = data["links"]
    for link in links:
        url = link['url']
        image_url = link['image_url']
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        data = soup.select(
            "ul.uk-switcher.donws_link > li:nth-child(1).uk-active")
        get_title = soup.find('title')
        Title = get_title.get_text()

        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        def slug(name):
            name = name.replace(':', '-')
            name = name.replace('?', '')
            name = name.replace('(', '')
            name = name.replace(')', '')
            name = name.replace('  ', ' ')
            name = name.replace(' ', '-')
            return name.lower()

        story = soup.select('.story')
        story_data = story[0].getText().strip()

        get_genre = soup.select(
            'ul > li:nth-child(9) > span.single-aside__item.single-aside__item--value')
        filter_genre = get_genre[0].getText()
        genre = "".join(filter_genre.split())

        get_number_of_episodes = soup.select(
            'ul > li:nth-child(4) > span:nth-child(2)')
        number_of_episodes = get_number_of_episodes[0].getText()

        get_air_date = soup.select(
            'div.single-aside__specs > ul > li:nth-child(2) > span:nth-child(2)')
        aired_from = get_air_date[0].getText()

        get_status = soup.select(
            ' ul > li:nth-child(6) > span.single-aside__item.single-aside__item--value')
        status = get_status[0].getText().strip()
        try: 
            get_content_type = soup.select(
                'ul > li:nth-child(10) > span.single-aside__item.single-aside__item--value')
            content_type = get_content_type[0].getText()
        except IndexError:
            content_type = 'Not Specified'

        alter = soup.select(
            'div > div.puplar > div:nth-child(3) > span.puplar__val')
        alternative_name = alter[0].getText()

        get_producers = soup.select(
            'div.single-aside__specs > ul > li:nth-child(5) > span.single-aside__item.single-aside__item--value')
        filter_producers = get_producers[0].getText().strip()
        producers = " ".join(filter_producers.split())

        get_broadcast_date = soup.select(
            ' div.single-aside__specs > ul > li:nth-child(3) > span:nth-child(2)')
        broadcasting_date = get_broadcast_date[0].getText()

        # #############
        main_sauce = []
        # #############

        # #############
        sorted_main_sauce = {}
        # #############

        new_soup = BeautifulSoup(str(data), 'html.parser')
        main_url = new_soup.find_all('a')

        get_first_patttern(main_url, main_sauce)
        get_second_pattern(main_url, main_sauce)

        for link_dict in main_sauce:
            episode, link = link_dict.values()
            if not sorted_main_sauce.get(episode):
                sorted_main_sauce[episode] = [link]
                continue
            sorted_main_sauce[episode].append(link)

        new_sauce = {
            "id": None,
            "title": Title,
            "slug": slug(Title),
            "added on": str(today),
            "updated on": str(today),
            "time": current_time,
            "alternative_title": alternative_name,
            "status": status,
            "genre": genre,
            "producers": producers,
            "image_url": image_url,
            "rating": content_type,
            "broadcasting_date": broadcasting_date,
            "summary": story_data,
            "aired_from": aired_from,
            "number_of_episodes": number_of_episodes,
            "number_of_episodes_released": len(sorted_main_sauce),
            "episodes": [sorted_main_sauce]
        }

        # function to add to JSON

        def write_json(data, filename='anime_data.json'):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)

        with open('anime_data.json') as json_file:
            data = json.load(json_file)
            temp = data['anime_list']
            length = len(temp)
            all_title = []
            for i in range(length):
                all_title.append(temp[i]['title'])
            if new_sauce['title'] not in all_title:
                try:  # adding an id to it
                    new_sauce['id'] = all_title.index(all_title[-1])+1
                    new_sauce['updated on'] = str(today)
                except IndexError:
                    new_sauce['id'] = 0
                temp.append(new_sauce)
                write_json(data)
            elif new_sauce['title'] == temp[i]['title']:
                new_temp = temp[i]['episodes']
                old_episodes = new_temp[0].keys()
                new_episodes = new_sauce['episodes'][0].keys()
                for new_episode in new_episodes:
                    if new_episode not in old_episodes:
                        new_temp[0].update(new_sauce['episodes'][0])
                        write_json(data)
                    if temp[i]['number_of_episodes_released'] < new_sauce['number_of_episodes_released']:
                        temp[i]['number_of_episodes_released'] = new_sauce['number_of_episodes_released']
                        write_json(data)
