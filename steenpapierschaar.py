import play 
import random
keuze = None
steen = play.new_image('steen.png', y = -100, x= -150)
papier = play.new_image('papier.png', y= -100, x= 0)
schaar = play.new_image('schaar.png', y=-100, x= 150)

opties = steen, papier, schaar

keuze_tekst = play.new_text("Welke kies je?", font_size=50, y=180)
aftel_tekst = play.new_text("Rock, paper, scissors, shoot!", font_size=100, y =100).hide()

score_computer = 0
score_speler = 0  

@play.when_mouse_clicked(steen) 
def keuze1():
    global keuze
    keuze = steen 
    keuze_tekst.hide()
    aftel_tekst.show()

@play.when_mouse_clicked(papier)
def keuze2():
    global keuze
    keuze = papier
    keuze_tekst.hide()
    aftel_tekst.show()

@play.when_mouse_clicked(schaar)
def keuze3():
    global keuze
    keuze = schaar 
    keuze_tekst.hide()
    aftel_tekst.show()


def uitslag():
    global score_computer, score_speler
    computer_keuze = play.random(opties)
    computer_keuze.x = -150
    keuze.x=150
    if computer_keuze == keuze: 
        play.new_text("Niemand wint")
    elif computer_keuze == steen and keuze == schaar:
        play.new_text("Computer wint een punt")
        score_computer += 1
    elif computer_keuze == steen and keuze== papier: 
        play.new_text("Jij wint een punt")
        score_speler +=1
    elif computer_keuze == papier and keuze == schaar:
        play.new_text("Jij wint een punt")
        score_speler += 1
    elif computer_keuze == papier and keuze == steen: 
        play.new_text("Computer wint een punt")
        score_computer += 1
    elif computer_keuze == schaar and keuze == papier: 
        play.new_text("Computer wint een punt")
        score_computer += 1
    elif computer_keuze == schaar and keuze == steen: 
        play.new_text("Jij wint een punt")
        score_speler += 1
        
score_tekst = play.new_text(f"{score_computer} - {score_speler}", font_size=50, y=180)

play.start_program()
