import play
bord = play.new_box(height= 200, width = 200, color="white", border_color="black", border_radius=10)
vak1 = play.new_box(height = 50, width = 50, color="white", border_color="black", border_radius=10)
tekst = play.new_text("boter, kaas en eieren", y=250)
speler1 = "X"
speler2 = "O"

@play.when_mouse_clicked
def pictogram(): 
    print(speler1) 


play.start_program()
#wat hier onder staat komt van chat. maar is om te kijken welke onderdelen we nodig hebben. 
def toon_bord():
    print()
    print(bord[0], "|", bord[1], "|", bord[2])
    print("--+---+--")
    print(bord[3], "|", bord[4], "|", bord[5])
    print("--+---+--")
    print(bord[6], "|", bord[7], "|", bord[8])
    print()

def check_winst(speler):
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combinatie in win:
        if all(bord[i] == speler for i in combinatie):
            return True
    return False

def spel():
    global speler
    zetten = 0

    while True:
        toon_bord()
        zet = int(input(f"Speler {speler}, kies een vakje (1-9): ")) - 1

        if bord[zet] != " ":
            print("❌ Vakje bezet!")
            continue

        bord[zet] = speler
        zetten += 1

        if check_winst(speler):
            toon_bord()
            print(f"🎉 Speler {speler} wint!")
            break

        if zetten == 9:
            toon_bord()
            print("🤝 Gelijkspel!")
            break

        speler = "O" if speler == "X" else "X"

spel()
play.start_program
