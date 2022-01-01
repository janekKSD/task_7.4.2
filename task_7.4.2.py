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

    def __str__(self):
        return f'{self.title} \tS{self.season:02d}E{self.episode:02d}'

Reksio = Movie(title='Reksio', year=2000, genre='animated movie')
Puchatek = Movie(title='Puchatek', year=2010, genre='animated movie')
Krecik = Movie(title='Krecik', year=1970, genre='animated movie')
Piła = Movie(title='Piła', year=2002, genre='horror')
Terminator = Movie(title='Terminator', year=1950, genre='action')
Matrix = Movie(title='Matrix', year=2001, genre='action')
#Reksio.play()

Klan = Series(title='Klan', year=2000, genre='drama', episode=4, season=2)
Friends = Series(title='Friends', year=1990, genre='musical', episode=1398, season=3)
Zlotopolscy = Series(title='Zlotopolscy', year=2010, genre='drama', episode=4, season=2)
Nocnik_krolewski = Series(title='Nocnik królewski', year=2003, genre='musical', episode=1398, season=3)
Narty_na_plazy= Series(title='Narty na plazy', year=2022, genre='comedy', episode=4, season=2)
Rowerem_przez_swiat = Series(title='Rowerem przez świat', year=1940, genre='drama', episode=1398, season=3)
#Klan.play()

collection = [Reksio, Puchatek, Krecik, Piła, Terminator, Matrix, Klan, Friends, Zlotopolscy, Nocnik_krolewski, Narty_na_plazy, Rowerem_przez_swiat]
movies = []
series = []

def get_movies(collection):
    movies.clear()
    new_movies = []
    for _ in collection:
        if isinstance(_, Series): #jaka jest funkcja, która wykrywa konkretnie instancje danej klasy bez instancji utowrzonych z dziedziczonych klas??
            pass
        else:
            new_movies.append(_)
    new_movies = sorted(new_movies, key= lambda x:x.title)
    movies.extend(new_movies)
#get_movies(collection)

def get_series(collection):
    series.clear()
    new_movies =[]
    for _ in collection:
        if isinstance(_, Series):
            new_movies.append(_)
    new_movies = sorted(new_movies, key=lambda x:x.title)
    series.extend(new_movies) 
#get_series(collection)

def search():
    title = input('Podaj tytuł filmu\n')
    for _ in collection:
        if _.title == title:
            print(_)
#search()

def generate_views(times):
    for _ in range(times):
        random_movie = random.randint(0, (len(collection) -1))
        #print(collection[random_movie])
        random_views = random.randint(1, 100)
        collection[random_movie].views += random_views
        #print(collection[random_movie].views)
#generate_views(100)

def top_titles(content_type):
    #print('1 - Filmy i seriale\n2 - Filmy\n3- Seriale')
    #content_type = int(input('Podaj zakres wyszukiwania filmów:\n'))
    times = 3 #int(input('Podaj długość listy:\n'))
    #print('Top views:')
    if content_type == 1:
        top = sorted(collection, key=lambda x:-x.views)
        for _ in range(times):
            print(top[_].title, '\tviews: ', top[_].views)
    elif content_type == 2:
        get_movies(collection)
        top = sorted(movies, key=lambda x:-x.views)
        for _ in range(times):
            print(top[_].title, '\tviews: ', top[_].views)
    elif content_type == 3:
        get_series(collection)
        top = sorted(series, key=lambda x:-x.views)
        for _ in range(times):
            print(top[_].title, '\tviews ', top[_].views)
#top_titles()

def print_collection():
    print('\tBiblioteka filmów\n', 30*'_' )
    lp = 1
    for _ in collection:
        print('  ', lp, '\t.', _)
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
