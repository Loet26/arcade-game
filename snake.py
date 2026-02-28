import play
import random
import pygame
import os
import subprocess

pygame.mixer.init()
pygame.mixer.music.load("arcadesound.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

eat=pygame.mixer.Sound("eating.mp3")
fail=pygame.mixer.Sound("fail.wav")

box=20
dir="right"
nextdir="right"
score=0
dead=False

snake=[]

bg=play.new_box(color="black",width=play.screen.width,height=play.screen.height)
play.screen.color="black"

head=play.new_box(color="lime",width=box,height=box)
apple=play.new_circle(color="red",radius=box/2)

t1=play.new_text(words="SCORE: 0",x=0,y=250,font_size=40,color="white")
t2=play.new_text(words="GAME OVER",y=40,font_size=80,color="red")
t3=play.new_text(words="CLICK TO RESTART",y=-40,font_size=30,color="yellow")
t4=play.new_text(words="EXIT",y=-120,font_size=40,color="orange")

t2.hide()
t3.hide()
t4.hide()

def newapple():
    ok=False
    while ok==False:
        apple.x=random.randint(-12,12)*box
        apple.y=random.randint(-8,8)*box
        if not head.is_touching(apple) and not any(p.is_touching(apple) for p in snake):
            ok=True

newapple()

def changedir(d):
    global nextdir,dir
    opp={"up":"down","down":"up","left":"right","right":"left"}
    if d!=opp[dir]:
        nextdir=d

@play.when_key_pressed("up","w")
def u(k):
    changedir("up")

@play.when_key_pressed("down","s")
def d(k):
    changedir("down")

@play.when_key_pressed("left","a")
def l(k):
    changedir("left")

@play.when_key_pressed("right","d")
def r(k):
    changedir("right")

async def restart():
    global score,dir,nextdir,dead,snake
    score=0
    t1.words="SCORE: 0"
    dir="right"
    nextdir="right"
    head.x=0
    head.y=0
    dead=False
    t2.hide()
    t3.hide()
    t4.hide()
    for p in snake:
        p.hide()
    snake=[]
    newapple()

@play.mouse.when_clicked
async def click1():
    if dead and t3.is_touching(play.mouse):
        await restart()

@play.mouse.when_clicked
async def click2():
    if dead and t4.is_touching(play.mouse):
        subprocess.Popen(["python","menu.py"])
        exit()

@play.repeat_forever
async def blink():
    if dead:
        t3.show()
        await play.timer(seconds=0.4)
        t3.hide()
        await play.timer(seconds=0.4)

@play.repeat_forever
async def game():
    global dir,score,dead

    if dead:
        return

    dir=nextdir

    ox=head.x
    oy=head.y

    if dir=="up":
        head.y+=box
    elif dir=="down":
        head.y-=box
    elif dir=="left":
        head.x-=box
    elif dir=="right":
        head.x+=box

    hit=any(head.is_touching(p) for p in snake)

    if head.x>play.screen.right or head.x<play.screen.left or head.y>play.screen.top or head.y<play.screen.bottom or hit:
        fail.play()
        dead=True
        t2.show()
        t3.show()
        t4.show()
        return

    np=play.new_box(color="lime",width=box-2,height=box-2,x=ox,y=oy)
    snake.append(np)

    if head.is_touching(apple):
        eat.play()
        score+=1
        t1.words="SCORE: "+str(score)
        newapple()
    else:
        if len(snake)>0:
            t=snake.pop(0)
            t.hide()

    await play.timer(seconds=0.12)

play.start_program()
