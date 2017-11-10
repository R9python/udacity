# coding: utf-8 

class Movie(object):
    """ Movie class, store movie information. """
    def __init__(self, title, poster_image_url, trailer_douban_url, starring, score):
        """ Use some information to initialize movie class.
        --title:                movie title
        --poster_image_url:     local image url
        --trailer_douban_url:   Trailer play address
        --starring:             movie starring
        --score:                movie score,the movie stars will ues it
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_douban_url = trailer_douban_url
        self.starring = starring
        self.score = score

        #count star by movie score
        if score > 0 and score <= 2:
            self.star_count = 1
        elif score > 2 and score <= 4:
            self.star_count = 2
        elif score > 4 and score <= 7:
            self.star_count = 3
        elif score > 7 and score < 8.5:
            self.star_count = 4
        elif score >= 8.5 and score <= 10:
            self.star_count = 5
        else:
            self.star_count = 0
