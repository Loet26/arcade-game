import play
bal = play.new_circle(color='black', radius=20)
batje_1 = play.new_box(color="black", x=250, width= 20, height = 80)
batje_2 = play.new_box(color="black", x=-250, width= 20, height = 80)

batje_1.start_physics(obeys_gravity=False, can_move=False)
batje_2.start_physics(obeys_gravity=False, can_move=False)
bal.start_physics(obeys_gravity=False, x_speed=250)
x_speed = 0
y_speed = 0

#bewegingen 
@play.when_key_pressed("up")
def batje1_omhoog():
    batje_1.y += 10

@play.when_key_pressed("w")
def batje2_omhoog():
    batje_2.y += 10

@play.when_key_pressed("down")
def batje1_omlaag():
    batje_1.y -= 10

@play.when_key_pressed("s")
def batje2_omlaag():
    batje_2.y -= 10

@play.repeat_forever
def bal_tegen_randen():
    global y_speed
    if bal.y > play.screen.top or bal.y < play.screen.bottom:
        y_speed *= -1

@play.repeat_forever
def bal_tegen_batjes():
    global x_speed
    if bal.is_touching(batje_1) or bal.is_touching(batje_2):
        x_speed *= -1

#score
score_links = 0
score_rechts = 0

score_tekst = play.new_text(f"{score_links} - {score_rechts}", font_size=50, y=180)
@play.repeat_forever
async def score_check():
    global score_links, score_rechts, x_speed, y_speed
    if bal.x > (batje_1.x + 120):
        score_links += 1
        bal.x = 0
        bal.y = 0
        x_speed *= -1
        score_tekst.words = f"{score_links} - {score_rechts}"
        await play.timer(seconds=2)

    if bal.x < (batje_2.x - 120):
        score_rechts += 1
        bal.x = 0
        bal.y = 0
        x_speed *= -1
        score_tekst.words = f"{score_links} - {score_rechts}"
        await play.timer(seconds=2)


play.start_program()