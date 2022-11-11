# __GDrivePlayer__

 Python module for fetching data from databasegdriveplayer.co

## __How this works__

 Scraps the information from the HTML of the page using `beautifulsoup4` .
 
 ## __Requirements__

 `pip install bs4`<br/><br/>
 `pip install requests`

## __Installation__

 `pip install GDrivePlayer`

## __Usage__

### __Anime__

 ```python
 from GDrivePlayer import GDrivePlayer
 from pprint import pprint

 obj = GDrivePlayer()

 anime = obj.searchAnimeList(query="jojo")
 pprint(anime)
 ```

 Output

 ```python
    [{'id': '2334',
  'link': 'https://databasegdriveplayer.co/anime.php?id=2334',
  'num': '1',
  'poster': 'https://cdnimg.xyz/cover/jojo-no-kimyou-na-bouken-diamond-wa-kudakenai.jpg',
  'status': 'Completed',
  'title': 'JoJo no Kimyou na Bouken: Diamond wa Kudakenai',
  'total_episodes': '39',
  'type': 'Spring 2016 Anime'},
 {'id': '2335',
  'link': 'https://databasegdriveplayer.co/anime.php?id=2335',
  'num': '2',
  'poster': 'https://cdnimg.xyz/images/spring/JoJo no Kimyou na Bouken '
            'Stardust Crusaders.jpg',
  'status': 'Completed',
  'title': 'JoJo no Kimyou na Bouken: Stardust Crusaders',
  'total_episodes': '24',
  'type': 'Spring 2014 Anime'},
 {'id': '2336',
  'link': 'https://databasegdriveplayer.co/anime.php?id=2336',
  'num': '3',
  'poster': 'https://cdnimg.xyz/images/upload/65907.jpg',
  'status': 'Completed',
  'title': 'JoJo no Kimyou na Bouken: Stardust Crusaders - Egypt Hen',
  'total_episodes': '24',
  'type': 'Winter 2015 Anime'},
 {'id': '2337',
  'link': 'https://databasegdriveplayer.co/anime.php?id=2337',
  'num': '4',
  'poster': 'https://cdnimg.xyz/images/anime/J/JoJo-Bizarre-Adventure.jpg',
  'status': 'Completed',
  'title': 'JoJo`s Bizarre Adventure',
  'total_episodes': '26',
  'type': 'TV Series'},
 {'id': '96249',
  'link': 'https://databasegdriveplayer.co/anime.php?id=96249',
  'num': '5',
  'poster': 'https://cdnimg.xyz/cover/jojo-no-kimyou-na-bouken-ougon-no-kaze.png',
  'status': 'Ongoing',
  'title': 'JoJo no Kimyou na Bouken: Ougon no Kaze',
  'total_episodes': '39',
  'type': 'Fall 2018 Anime'}]
  ```

### __Movie__

```python
 from GDrivePlayer import GDrivePlayer
 from pprint import pprint

 obj = GDrivePlayer()

 movie = obj.searchMovieList("hangover")
 pprint(movie)
```

Output

```python
    [{'date_added': '2021-06-13 13:55:15',
  'id': 'tt1951261',
  'imdb': 'https://www.imdb.com/title/tt1951261',
  'num': '1.',
  'player_links': {'gdid': 'https://databasegdriveplayer.co/player.php?imdb=tt1951261&id=28387',
                   'imdb': 'https://databasegdriveplayer.co/player.php?imdb=tt1951261',
                   'tmdb': 'https://databasegdriveplayer.co/player.php?tmdb=109439'},
  'poster': 'https://m.media-amazon.com/images/M/MV5BMTA0NjE1MzMzODheQTJeQWpwZ15BbWU3MDY4MTQ3Mzk@._V1_.jpg',
  'quality': 'HD 720',
  'subtitles': 'none',
  'themoviedb': 'https://www.themoviedb.org/movie/109439',
  'title': 'The Hangover Part 3',
  'year': '2013'},
 {'date_added': '2021-06-13 13:55:15',
  'id': 'tt1119646',
  'imdb': 'https://www.imdb.com/title/tt1119646',
  'num': '2.',
  'player_links': {'gdid': 'https://databasegdriveplayer.co/player.php?imdb=tt1119646&id=28386',
                   'imdb': 'https://databasegdriveplayer.co/player.php?imdb=tt1119646',
                   'tmdb': 'https://databasegdriveplayer.co/player.php?tmdb=18785'},
  'poster': 'https://image.tmdb.org/t/p/w300//jjCPcxw7QCmFPYM1t3BThdEawJK.jpg',
  'quality': 'HD 720',
  'subtitles': 'English, Indonesia',
  'themoviedb': 'https://www.themoviedb.org/movie/18785',
  'title': 'The Hangover',
  'year': '2009'},
 {'date_added': '2021-06-13 13:55:15',
  'id': 'tt1411697',
  'imdb': 'https://www.imdb.com/title/tt1411697',
  'num': '3.',
  'player_links': {'gdid': 'https://databasegdriveplayer.co/player.php?imdb=tt1411697&id=28388',
                   'imdb': 'https://databasegdriveplayer.co/player.php?imdb=tt1411697',
                   'tmdb': 'https://databasegdriveplayer.co/player.php?tmdb=45243'},
  'poster': 'https://m.media-amazon.com/images/M/MV5BMTM2MTM4MzY2OV5BMl5BanBnXkFtZTcwNjQ3NzI4NA@@._V1_.jpg',
  'quality': 'HD',
  'subtitles': 'none',
  'themoviedb': 'https://www.themoviedb.org/movie/45243',
  'title': 'The Hangover Part 2',
  'year': '2011'},
 {'date_added': '2021-06-13 13:55:15',
  'id': 'tt8655858',
  'imdb': 'https://www.imdb.com/title/tt8655858',
  'num': '4.',
  'player_links': {'gdid': 'https://databasegdriveplayer.co/player.php?imdb=tt8655858&id=16833',
                   'imdb': 'https://databasegdriveplayer.co/player.php?imdb=tt8655858',
                   'tmdb': 'https://databasegdriveplayer.co/player.php?tmdb=585154'},
  'poster': 'https://m.media-amazon.com/images/M/MV5BMDgzY2YwOWQtYjY5NS00YTZiLTlkYmItYmZmZDFlZTk4MzMyXkEyXkFqcGdeQXVyMTc0ODg5NTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'quality': 'HD Rip',
  'subtitles': 'English',
  'themoviedb': 'https://www.themoviedb.org/movie/585154',
  'title': 'Hangover in Death Valley',
  'year': '2018'}]
  ```

## __Disclaimer__

 I'm in no way related to that website / person behind it / the kind of information hosted on it. The author of this library isn't responsible for what you do with this library.
