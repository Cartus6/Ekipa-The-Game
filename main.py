from ursina import *
import pygame
import random
from time import sleep
pygame.init()
app = Ursina()
application.development_mode = False
window.fullscreen = True
window.cog_button.enabled = False

music = pygame.mixer.music.load("assets/Star Commander1.wav")
punkt = pygame.mixer.Sound("assets/mixkit-quick-jump-arcade-game-239.wav")
gmover = pygame.mixer.Sound("assets/gmover.wav")
pygame.mixer.music.play(-1)


class Lod(Entity):
    szybkosc = 3
    wynik = 0
    text = Text(text=f"Wynik: {wynik}")

    def __init__(self):
        super().__init__(
            model='quad',
            texture="assets/0327-ekipa3.png",
            collider='box',
            y=5,
            x=0
        )

    def update(self):
        if self.intersects().hit:
            punkt.play()
            self.visible = False
            self.x = random.randint(-7, 7)
            self.y = 5
            self.wynik += 1
            self.visible = True
            self.text.text = f"Wynik: {self.wynik}"
            self.text.color = color.white
            self.szybkosc += 0.1
        if self.y < -6:
            pygame.mixer.music.pause()

            gmover.play()
            sleep(0.5)
            pygame.mixer.music.play(-1)

            self.wynik = 0
            self.szybkosc = 3
            self.text.text = f"Wynik: {self.wynik}"
            self.y = 5

        self.y -= self.szybkosc * time.dt


bckground = Entity(model='quad', scale=Vec2(23, 15),
                   texture="assets/sean-oulashin-KMn4VEeEPR8-unsplash.jpg", z=10)
friz = Entity(model='quad', texture="assets/twarz.png",
              scale=(2.7, 2.7), y=-3.2, x=0, collider='box')


lod = Lod()


def update():

    if held_keys['a']:
        friz.x -= 5.5 * time.dt

    if held_keys['d']:
        friz.x += 5.5 * time.dt


app.run()
