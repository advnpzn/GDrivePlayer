from typing import Union
from bs4 import BeautifulSoup as bs
import requests
from .exceptions import StatusCodeError

def _scrapAnimeList(query:str, url: str) -> list:
    
    """
    Scraps The Anime results obtained from query.
    """

    res = requests.get(url+"s="+query)
    if res.status_code != 200:
        raise StatusCodeError(res.status_code)
    res = res.text
    soup = bs(res, 'lxml')
    t_result = soup.find_all('tr')[1:]
    _list = []
    for row in t_result:
        columns = row.find_all('td')
        if (columns != []):
            num = columns[0].text
            poster = columns[1].find('img').get('src')
            title = columns[2].find('a').text
            id = columns[2].find('a').get('href').split("=")[-1]
            total_episodes = columns[3].text
            status = columns[4].text
            type = columns[5].text
            link = url+"id="+id

            _dict = {
                'num': num,
                'id': id,
                'poster': poster,
                'title': title,
                'total_episodes': total_episodes,
                'status': status,
                'type': type,
                'link': link,
            }

            _list.append(_dict)
    return _list
    

def _scrapMovieList(query:str, url: str) -> list:

    """
    Scraps The Movie results obtained from query.
    """

    res = requests.get(url+"s="+query)
    if res.status_code != 200:
        raise StatusCodeError(res.status_code)
    res = res.text
    soup = bs(res, 'lxml')
    t_result = soup.find_all('tr')[1:]
    _list = []
    for row in t_result:
        columns = row.find_all('td')
        if (columns != []):
            num = columns[0].text
            poster = columns[1].find('img').get('src')
            title = columns[2].find('a').text
            id = columns[2].find('a').get('href').split("=")[-1]
            year = columns[3].text
            imdb = columns[4].find('a').get('href')
            themoviedb = columns[5].find('a').get('href')
            quality = columns[6].text
            subtitles = columns[7].text

            p_soup = columns[8].find_all('a')
            p_imdb = "https:" + p_soup[0].get('href')
            p_tmdb = "https:" + p_soup[1].get('href')
            p_gdid = "https:" + p_soup[2].get('href')
            player_links = {
                "imdb": p_imdb,
                "tmdb": p_tmdb,
                "gdid": p_gdid
            }

            date_added = columns[10].text

            _dict = {
                'num': num,
                'id': id,
                'poster': poster,
                'title': title,
                'year': year,
                'imdb': imdb,
                'themoviedb': themoviedb,
                'quality': quality,
                'subtitles': subtitles,
                'player_links': player_links,
                'date_added': date_added
            }

            _list.append(_dict)
    return _list


def _scrapAnime(id: Union[str, int], url: str) -> list:
    if type(id) == int:
        id = str(id)
    res = requests.get(url+id).text
    soup = bs(res, 'lxml')
    t_result = soup.find_all('tr')[1:]
    title = t_result[1].find_all('td')[1].text
    _list = [
        {
            "title": title
        },
    ]
    for row in t_result:
        columns = row.find_all('td')
        if (columns != []):
            num = columns[0].text
            episode = columns[2].text
            subtitle = columns[3].text
            date_added = columns[4].text
            player_link = "https:" + columns[5].find('a').get('href')
        _dict = {
            "num": num,
            "episode": episode,
            "subtitle": subtitle,
            "date_added": date_added,
            "player_link": player_link
        }
        _list.append(_dict)
    
    return _list
