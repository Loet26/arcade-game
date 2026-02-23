import play
import pygame
import os
import sys

pygame.mixer.init()
pygame.mixer.music.load("arcademuziek.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

bg = play.new_image(image="2Q.png", x=0, y=0)
bg.size = 360

titelGlow = play.new_text(words="ARCADE", y=220, font_size=72, color="magenta", transparency=0.3)
titel = play.new_text(words="ARCADE", y=218, font_size=70, color="cyan")

snakeBoxRand = play.new_box(color="cyan", width=210, height=70, x=-120, y=80)
snakeBox = play.new_box(color="black", width=200, height=60, x=-120, y=80)
snakeTxt = play.new_text(words="SNAKE", x=-120, y=80, font_size=35, color="cyan")

pongRand = play.new_box(color="green", width=210, height=70, x=120, y=80)
pongBox = play.new_box(color="black", width=200, height=60, x=120, y=80)
pongTxt = play.new_text(words="PONG", x=120, y=80, font_size=35, color="green")

boterRand = play.new_box(color="yellow", width=210, height=110, x=-120, y=-20)
boterBox = play.new_box(color="black", width=200, height=100, x=-120, y=-20)
boterTxt1 = play.new_text(words="BOTER KAAS", x=-120, y=-10, font_size=30, color="yellow")
boterTxt2 = play.new_text(words="EN EIEREN", x=-120, y=-40, font_size=30, color="yellow")

galgjeRand = play.new_box(color="magenta", width=210, height=70, x=120, y=-20)
galgjeBox = play.new_box(color="black", width=200, height=60, x=120, y=-20)
galgjeTxt = play.new_text(words="GALGJE", x=120, y=-20, font_size=35, color="magenta")

leaveRand = play.new_box(color="red", width=210, height=70, x=0, y=-130)
leaveBox = play.new_box(color="black", width=200, height=60, x=0, y=-130)
leaveTxt = play.new_text(words="LEAVE", x=0, y=-130, font_size=35, color="red")

@play.mouse.when_clicked
async def clickDing():
    if play.mouse.is_touching(snakeBox):
        pygame.mixer.music.stop()
        os.system("python snake.py")
        sys.exit()

    if play.mouse.is_touching(galgjeBox):
        pygame.mixer.music.stop()
        os.system("python galgje.py")
        sys.exit()

    if play.mouse.is_touching(boterBox):
        pygame.mixer.music.stop()
        os.system("python boterkaasenerien.py")
        sys.exit()

    if play.mouse.is_touching(pongBox):
        pygame.mixer.music.stop()
        os.system("python pong.py")
        sys.exit()

    if play.mouse.is_touching(leaveBox):
        pygame.mixer.music.stop()
        sys.exit()

@play.repeat_forever
async def hoverDing():
    if play.mouse.is_touching(snakeBox):
        snakeBox.color = "cyan"
        snakeTxt.color = "black"
    else:
        snakeBox.color = "black"
        snakeTxt.color = "cyan"

    if play.mouse.is_touching(galgjeBox):
        galgjeBox.color = "magenta"
        galgjeTxt.color = "black"
    else:
        galgjeBox.color = "black"
        galgjeTxt.color = "magenta"

    if play.mouse.is_touching(boterBox):
        boterBox.color = "yellow"
        boterTxt1.color = "black"
        boterTxt2.color = "black"
    else:
        boterBox.color = "black"
        boterTxt1.color = "yellow"
        boterTxt2.color = "yellow"

    if play.mouse.is_touching(pongBox):
        pongBox.color = "green"
        pongTxt.color = "black"
    else:
        pongBox.color = "black"
        pongTxt.color = "green"

    if play.mouse.is_touching(leaveBox):
        leaveBox.color = "red"
        leaveTxt.color = "black"
    else:
        leaveBox.color = "black"
        leaveTxt.color = "red"

play.start_program()
