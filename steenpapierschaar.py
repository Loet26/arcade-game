import play 
import random

def potje():
    def add_extension(objectnaam):
        return objectnaam+'.png'

    keuze = None
    keuzenaam = None
    steen = play.new_image('steen.png', y = -100, x= -200, size=30)
    papier = play.new_image('papier.png', y= -100, x= 0, size = 50)
    schaar = play.new_image('schaar.png', y=-100, x= 170, size =50)
    steen.show()
    papier.show()
    schaar.show()

    opties = [steen, papier, schaar]
    opties_names = ['steen', 'papier', 'schaar']
    keuze_tekst = play.new_text("Welke kies je?", font_size=50, y=180)
    aftel_tekst = play.new_text("Rock, paper, scissors, shoot!", font_size=50, y =100)
    aftel_tekst.hide()

    score_computer = 0
    score_speler = 0  

    @steen.when_clicked
    def geklikt():
        global keuze, keuzenaam, steen, papier, schaar
        steen = play.new_box(height = 200, width = 730, color='white', y=-100)
        keuze = steen
        keuzenaam = "steen"
        keuze_tekst.hide()
        aftel_tekst.show()
        uitslag()

    @papier.when_clicked
    def geklikt():
        global keuze, keuzenaam, steen, papier, schaar
        papier = play.new_box(height = 200, width = 730, color='white', y=-100)
        keuze = papier
        keuzenaam = 'papier'
        keuze_tekst.hide()
        aftel_tekst.show()
        uitslag()

    @schaar.when_clicked
    def geklikt():
        global keuze, keuzenaam, steen, papier, schaar
        schaar = play.new_box(height = 200, width = 730, color='white', y=-100)
        keuze = schaar
        keuzenaam = 'schaar'
        keuze_tekst.hide()
        aftel_tekst.show()
        uitslag()

    def uitslag():
        global keuze, keuzenaam
        global score_computer, score_speler
        if keuzenaam!= None:
            computer_keuze = random.choice(opties_names)
            computer_afbeelding = play.new_image(add_extension(computer_keuze), y = -100, x= 150, size=30)
            speler_afbeelding = play.new_image(add_extension(keuzenaam), y = -100, x= -150, size=30)
            if computer_keuze == keuzenaam: 
                play.new_text("Niemand wint")
            elif computer_keuze == "steen" and keuzenaam == 'schaar':
                play.new_text("Computer wint een punt")
                score_computer += 1
            elif computer_keuze == 'steen' and keuzenaam== 'papier': 
                play.new_text("Jij wint een punt")
                score_speler +=1
            elif computer_keuze == 'papier' and keuzenaam == 'schaar':
                play.new_text("Jij wint een punt")
                score_speler += 1
            elif computer_keuze == 'papier' and keuzenaam == 'steen': 
                play.new_text("Computer wint een punt")
                score_computer += 1
            elif computer_keuze == 'schaar' and keuzenaam == 'papier': 
                play.new_text("Computer wint een punt")
                score_computer += 1
            elif computer_keuze == 'schaar' and keuzenaam == 'steen': 
                play.new_text("Jij wint een punt")
                score_speler += 1
                
        score_tekst = play.new_text(f"{score_computer} - {score_speler}", font_size=30, y=220)

@play.repeat_forever
def herhaling():
    if score_computer < 10 and score_computer <10: 
        return potje 

play.start_program()
