import play 
menu = play.new_box(color= "white", border_radius= 10, border_color="black", width = 200, height= 100)
tekst = play.new_text("Welkom in de arcade")

spel_1 = play.new_box (color= "black", width = 100, height= 100, x=-200, y=100)
spel_2 = play.new_box (color= "blue", width = 100, height= 100, x=200, y=100)
spel_3 = play.new_box (color= "green", width = 100, height= 100, x=-200, y=-100)
spel_4 = play.new_box (color= "red", width = 100, height= 100, x=200, y=-100)

@play.when_mouse_clicked()
#wanneer een van de vierkantjes wordt geklikt moet je naar een spelletje gaan

play.start_program()
