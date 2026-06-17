from abc import ABC, abstractmethod
import pygame

class Car:

    def __init__(self, brand, model, year, for_sale):
        self.brand=brand
        self.model=model
        self.year=year
        self.for_sale=for_sale


    def honk(self):
        pygame.mixer.init()

        if self.year <= 1940:
            pygame.mixer.music.load("sounds/vintage_carhorn.mp3")
        else:
            pygame.mixer.music.load("sounds/modern_carhorn.mp3")    

        pygame.mixer.music.play()
    