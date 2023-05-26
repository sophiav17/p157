from tkinter import*
from PIL import ImageTk, Image
import random

root = Tk()

root.title("Endlesss Pokemon Game")
root.geometry("400x400")
root.configure(background = "pink")

abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
iyvasour = ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))

display_player_1_label = Label(root, text = "Player 1", bg = "red", fg = "white")
display_player_1_label.place(relx = 0.1, rely = 0.3, anchor = CENTER)

display_player_2_label = Label(root, text = "Player 2", bg = "red", fg =  "white")
display_player_2_label.place(relx = 0.9, rely = 0.3, anchor = CENTER)

display_player_1_score = Label(root, bg = "blue", fg = "white")
display_player_1_score.place(relx = 0.1, rely = 0.4, anchor = CENTER)

display_player_2_score = Label(root, bg = "blue", fg = "white")
display_player_2_score.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_card_label = Label(root)
random_card_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

pokemon_list = [abra, bulbasour, charmender, iyvasour, jigglypuff, kadabra, meowth, nidoking, paras, persion, pikachu, ratata, squirtle]
power_pokemon = [30, 60, 50, 100, 70, 70, 60, 90, 40, 70, 200, 40, 50]

player1_score = 0
def player1() :
    global player1_score
    random_no = random.randint(1, 13)
    random_pokemon = pokemon_list(random_no)
    random_card_label["image"] = random_pokemon
    random_power_list = pokemon_list(random_no)
    player1_score = player1_score + random_power_list
    display_player_1_score["text"] = player1_score
    
player2_score = 0
def player2() :
    global player2_score
    random_no2 = random.randint(1, 13)
    random_pokemon2 = pokemon_list(random_no2)
    random_card_label["image"] = random_pokemon2
    random_power_list = pokemon_list(random_no2)
    player2_score = player2_score + random_power_list
    display_player_2_score["text"] = player2_score
    
player1_btn = Button(root, image = button, command = player1)
player1_btn.place(relx = 0.1, rely = 0.6, anchor = CENTER)

player2_btn = Button(root, image = button, command = player2)
player2_btn.place(relx = 0.9, rely = 0.6, anchor = CENTER)

root.mainloop()