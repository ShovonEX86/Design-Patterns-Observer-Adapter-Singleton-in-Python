# -*- coding: utf-8 -*-
"""Observer_Pattern2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QUUzAoRpHUE7fZL_B-oy-Naezz8Ngsao
"""

class FilmCelebrity(Celebrity):
    def __init__(self):
        super().__init__()
        self.state = None

    def set_state(self, new_state):
        self.state = new_state
        self.notify_fans()

    def get_state(self):
        return self.state


class FilmFan(Fan):
    def __init__(self, name):
        super().__init__(name)
        self.film_celebrities = []

    def update(self, film_celebrity):
        if film_celebrity in self.film_celebrities:
            print(f"{self.name}, notification for you! {film_celebrity.get_state()}")

    def add_celebrity(self, film_celebrity):
        self.film_celebrities.append(film_celebrity)
        film_celebrity.attach(self)

    def remove_celebrity(self, film_celebrity):
        self.film_celebrities.remove(film_celebrity)
        film_celebrity.remove(self)


f1 = FilmFan("Leo")
f2 = FilmFan("Brad")
f3 = FilmFan("Lee")

fc1 = FilmCelebrity()

f1.add_celebrity(fc1)
f2.add_celebrity(fc1)
f3.add_celebrity(fc1)

fc1.set_state("FilmCelebrity posted a new photo")    #Leo, notification for you! FilmCelebrity posted a new photo
                                                     #Brad, notification for you! FilmCelebrity posted a new photo
                                                     #Lee, notification for you! FilmCelebrity posted a new photo