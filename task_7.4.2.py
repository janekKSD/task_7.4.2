import random
import datetime

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        #variables
        self.views = 0

    def __str__(self):
        return f'{self.title} \tyear {self.year}'

    def __repr__(self):
        return f'{self.title} views: {self.views}'

    def play(self):
        self.views =+ 1
        print(self)

class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        #variables
        self._available_episode = 0

    def __str__(self):
        return f'{self.title} \tS{self.season:02d}E{self.episode:02d}'

    def __eq__(self, other):
        return all(
            (
            self.title == other.title,
            self.year == other.year,
            self.genre == other.genre,
            self.episode == other.episode,
            self.season == other.season
            )
        )

    def show_available_episode(self):
        for episode in collection:
            if episode.title == self.title:
                self._available_episode += 1
        print(f'Biblioteka zawiera {self._available_episode} odcinków serialu {self.title}')
    
reksio = Movie(title='Reksio', year=2000, genre='animated movie')
puchatek = Movie(title='Puchatek', year=2010, genre='animated movie')
krecik = Movie(title='Krecik', year=1970, genre='animated movie')
pila = Movie(title='Piła', year=2002, genre='horror')
terminator = Movie(title='Terminator', year=1950, genre='action')
matrix = Movie(title='Matrix', year=2001, genre='action')

klan = Series(title='Klan', year=2000, genre='drama', episode=4, season=1)
friends = Series(title='Friends', year=1990, genre='musical', episode=5, season=1)
zlotopolscy = Series(title='Zlotopolscy', year=2010, genre='drama', episode=10, season=2)
nocnik_krolewski = Series(title='Nocnik królewski', year=2003, genre='musical', episode=8, season=3)
narty_na_plazy= Series(title='Narty na plazy', year=2022, genre='comedy', episode=4, season=2)
rowerem_przez_swiat = Series(title='Rowerem przez świat', year=1940, genre='drama', episode=7, season=2)

collection = [reksio, puchatek, krecik, pila, terminator, matrix, klan, friends, zlotopolscy, nocnik_krolewski, narty_na_plazy, rowerem_przez_swiat]
movies = []
series = []

def get_kind(collection, kind):
    new_movies = []
    if kind == 1:
        movies.clear()
        for data in collection:
            if type(data) == Movie:
                new_movies.append(data)        
        new_movies = sorted(new_movies, key= lambda x:x.title)
        movies.extend(new_movies)
    elif kind == 2:
        series.clear()
        for movie in collection:
            if isinstance(movie, Series):
                new_movies.append(movie)
        new_movies = sorted(new_movies, key=lambda x:x.title)
        series.extend(new_movies)

def search():
    title = input('Podaj tytuł filmu\n')
    for movie in collection:
        if movie.title == title:
            print(movie)


def generate_views(times):
    for _ in range(times):
        random_movie = random.randint(0, (len(collection) -1))
        random_views = random.randint(1, 100)
        collection[random_movie].views += random_views

def top_titles(content_type):
    times = 3
    if content_type == 1:
        collection.sort(key=lambda x: x.views, reverse=True)
        for number in range(times):
            print(collection[number].title, '\tviews: ', collection[number].views)
    elif content_type == 2:
        get_kind(collection, 1)
        movies.sort(key=lambda x: x.views, reverse=True)
        for number in range(times):
            print(movies[number].title, '\tviews: ', movies[number].views)
    elif content_type == 3:
        get_kind(collection, 2)
        series.sort(key=lambda x: x.views, reverse=True)
        for number in range(times):
            print(series[number].title, '\tviews ', series[number].views)

def print_collection():
    print('\tBiblioteka filmów\n', 30*'_' )
    lp = 1
    for data in collection:
        print('  ', lp, '\t.', data)
        lp += 1
print_collection()

generate_views(10)

def print_top():
    now = datetime.date.today().strftime('%m.%d.%Y')
    print(f'\nNajpopularniejsze filmy dnia {now}:')
    top_titles(2)
    print(f'\nNajpopularniejsze seriale dnia {now}:')
    top_titles(3)
print_top()

def add_season(series):
    for data in series:
        max_episode = data.episode
        max_season = data.season
        title = data.title
        year = data.year
        genre = data.genre
        number_season = 1
        number_add_episode = 0
        for _ in range(max_season):
            number_episode = 1
            for _ in range(max_episode):
                episode = Series(title=title, year=year, genre=genre, episode=number_episode, season=number_season)
                if episode in series:
                    pass
                else:
                    collection.append(episode)
                    number_add_episode += 1
                number_episode += 1
            number_season += 1
        print(f'Dodano {number_add_episode} odcinków serialu {data.title}')
    get_kind(collection, 2)

add_season(series)
print_collection()

friends.show_available_episode()
rowerem_przez_swiat.show_available_episode()
