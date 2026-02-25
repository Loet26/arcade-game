import play
import random
import os
import subprocess
import pygame

pygame.mixer.init()
wingeluid = pygame.mixer.Sound("win.mp3")
failgeluid = pygame.mixer.Sound("failgalgje.mp3")

words = ["Aansprakelijkheidswaardevaststellingsveranderingen","Jazz","sowieso","informatica","school","huiswerk","python","verveling","olifant","woonkamer","vakantie","winter","galgje","zeewier","sushi","lasagna","auto","vrachtwagen","vijfhonderduizend","chagrijnig","fictief","kritisch","voetbal","walvis","lieveheersbeestje"]

picked = ""
used = []
wrong = 0
maxwrong = 9
done = False

play.screen.color = "white"

txtmenu = play.new_text(words="Terug naar menu", y=280, font_size=25, color="purple")
titel = play.new_text(words="GALGJE", y=220, font_size=50, color="black")
woord = play.new_text(words="", y=-80, font_size=60)
status = play.new_text(words="Typ een letter", y=-180, font_size=30, color="blue")
wrongtxt = play.new_text(words="", x=300, y=250, font_size=30, color="red")
usedtxt = play.new_text(words="Fout geprobeerd: ", y=-250, font_size=25, color="gray")

l1 = play.new_line(color="black", x=-200, y=-150, x1=-50, y1=-150, thickness=5)
l2 = play.new_line(color="black", x=-125, y=-150, x1=-125, y1=150, thickness=5)
l3 = play.new_line(color="black", x=-125, y=150, x1=25, y1=150, thickness=5)
l4 = play.new_line(color="black", x=25, y=150, x1=25, y1=100, thickness=3)
h = play.new_circle(color="black", x=25, y=70, radius=30, border_width=3, border_color="black")
b = play.new_line(color="black", x=25, y=40, x1=25, y1=-40, thickness=3)
a = play.new_line(color="black", x=-10, y=10, x1=60, y1=10, thickness=3)
l11 = play.new_line(color="black", x=25, y=-40, x1=-10, y1=-80, thickness=3)
l22 = play.new_line(color="black", x=25, y=-40, x1=60, y1=-80, thickness=3)

parts = [l1, l2, l3, l4, h, b, a, l11, l22]

def newgame():
    global picked, used, wrong, done
    picked = random.choice(words).upper()
    used = []
    wrong = 0
    done = False
    for p in parts:
        p.hide()
    status.words = "Typ een letter"
    status.color = "blue"
    usedtxt.words = "Fout geprobeerd: "
    update()

def update():
    s = ""
    for c in picked:
        if c in used:
            s += c + " "
        else:
            s += "_ "
    woord.words = s
    wrongtxt.words = "Fouten: " + str(wrong) + " / " + str(maxwrong)
    wl = [x for x in used if x not in picked]
    usedtxt.words = "Fout geprobeerd: " + ", ".join(sorted(wl))

@play.mouse.when_clicked
async def klikmenu():
    if txtmenu.is_touching(play.mouse):
        subprocess.Popen(["python", "menu.py"])
        exit()

@play.when_key_pressed(*"abcdefghijklmnopqrstuvwxyz")
async def key(k):
    global wrong, done
    if done:
        return
    L = k.upper()
    if L not in used:
        used.append(L)
        if L in picked:
            status.words = "Goed! De " + L + " zit erin."
            status.color = "green"
        else:
            wrong += 1
            status.words = "Helaas, geen " + L
            status.color = "red"
            if wrong <= len(parts):
                parts[wrong - 1].show()
        update()
        win = True
        for c in picked:
            if c not in used:
                win = False
        if win:
            wingeluid.play()
            status.words = "GEWONNEN! Klik om opnieuw te spelen."
            done = True
        elif wrong >= maxwrong:
            failgeluid.play()
            status.words = "VERLOREN! Het was: " + picked + ". Klik om opnieuw te spelen."
            done = True

@play.mouse.when_clicked
async def restart():
    if done and not txtmenu.is_touching(play.mouse):
        newgame()

newgame()
play.start_program()
