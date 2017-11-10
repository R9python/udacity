# coding: utf-8 
# flake8: noqa
import media
import fresh_tomatoes

def generate_movie_library():
    """ Generate a movie library and return movie list """
    movies = []

    #创建instance
    #https://movie.douban.com/subject/26593587/
    gifted = media.Movie("Gifted", "img/p2458752531.jpg", "http://vt1.doubanio.com/201710301436/f4a9b55cf83130f756e1c8bcd8baccf4/view/movie/M/302090128.mp4", ['Chris Evans','Mckenna Grace'],8.1)

    #https://movie.douban.com/subject/24753477/
    spiderman = media.Movie("Spider-Man: Homecoming", "img/p2497756471.jpg", "http://vt1.doubanio.com/201710301656/61eb17d0a7c7c68b5c626eb19ae91f3f/view/movie/M/302180454.mp4", ['Tom Holland','Robert Downey','Marisa Tomei'],7.4)

    #https://movie.douban.com/subject/26607693/
    dunkirk = media.Movie("Dunkirk", "img/p2494950714.jpg", "http://vt1.doubanio.com/201710301659/fa14ab64478ab173c7138d3711b4d104/view/movie/M/302190088.mp4", ['Fionn Whitehead','Tom Glynn-Carney','Jack Lowden','Harry Styles'],8.6)

    #https://movie.douban.com/subject/10512661/
    blade = media.Movie("Blade Runner 2049", "img/p2501623796.jpg", "http://vt1.doubanio.com/201710302042/cdbeddadf15d03dc5da545e34c79c2c8/view/movie/M/302220132.mp4", ['Ryan Gosling','Ana de Armas','Sylvia Hoeks'],8.5)

    #https://movie.douban.com/subject/25821634/
    thor = media.Movie("Thor: Ragnarok","img/p2501853635.jpg","http://vt1.doubanio.com/201710302047/d104ef5f56c5b10a18f8af6ce9a3a893/view/movie/M/302190596.mp4", ['Chris Hemsworth','Tom Hiddleston'],7.8)

    #https://movie.douban.com/subject/26378579/
    kingsman = media.Movie("Kingsman: The Golden Circle", "img/p2502467299.jpg", "http://vt1.doubanio.com/201710302051/5f27e324693b6cb19340e3b8dedfb9ee/view/movie/M/302220803.mp4", ['Taron Egerton','Colin Firth','Mark Strong','Julianne Moore','Elton John'],6.9)# noqa

    #加入到movies list
    movies.append(gifted)
    movies.append(spiderman)
    movies.append(dunkirk)
    movies.append(blade)
    movies.append(thor)
    movies.append(kingsman)

    return movies

movies = generate_movie_library()
fresh_tomatoes.open_movies_page(movies)

