from ursina import *
from playsound import playsound
import random
from time import sleep
app = Ursina()
application.development_mode = False
window.fullscreen = True
window.cog_button.enabled = False


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

            self.visible = False
            self.x = random.randint(-7, 7)
            self.y = 5
            self.wynik += 1
            self.visible = True
            self.text.text = f"Wynik: {self.wynik}"
            self.text.color = color.white
            self.szybkosc += 0.1
        if self.y < -6:

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
