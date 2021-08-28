from typing import Union
from .scrap import _scrapAnimeList, _scrapMovieList, _scrapAnime
from pprint import pprint

class GDrivePlayer:
    def __init__(self) -> None:
        self.baseUrl = "https://databasegdriveplayer.co/"

    def searchAnimeList(self, query: str) -> list:
        return _scrapAnimeList(query, self.baseUrl+"anime.php?")

    def Anime(self, id: Union[int, str]):
        return _scrapAnime(id, self.baseUrl+"anime.php?id=")

    def searchMovieList(self, query: str) -> list:
        return _scrapMovieList(query, self.baseUrl+"movie.php?")
