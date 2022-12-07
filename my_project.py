import random
from string import ascii_uppercase
from tkinter import *
from tkinter import messagebox


def main():
    window = Tk()
    window.geometry("800x720")
    window.title("Save the Snow Doll")
    imagen_for_background = PhotoImage(file="01.png")
    background = Label(image=imagen_for_background, text="background")
    background.place(x=0, y=0, relwidth=1, relheight=1)
    images = [PhotoImage(file="h0.png"), PhotoImage(file="h1.png"),
              PhotoImage(file="h2.png"), PhotoImage(file="h3.png"),
              PhotoImage(file="h4.png"), PhotoImage(file="h5.png"),
              PhotoImage(file="h6.png"), PhotoImage(file="h7.png"),
              PhotoImage(file="h8.png"), PhotoImage(file="h9.png")]

    hangman_images = Label(window)
    hangman_images.grid(row=8, column=5, columnspan=5, padx=10, pady=40)
    white_spaces = StringVar()
    Label(window, textvariable=white_spaces, bg="#8bccd3", font='verdana 24 bold').grid(row=7, column=3, columnspan=10,
                                                                                        padx=10)

    def white_spaces_dashboard():
        global dashboard_in_white
        global number_of_guesses
        global the_word
        the_word = pick_secret_word()
        number_of_guesses = 0
        dashboard_in_white = " ".join(the_word)
        white_spaces.set(' '.join("_" * len(the_word)))

    def instructions(en_ventana):
        Label(en_ventana, text="").grid(row=0, column=0)
        Label(en_ventana, text="Welcome To save the Snow-doll",
              bg="#4c7daf", font='verdana 16 bold').grid(row=1, column=1, columnspan=6)
        Label(en_ventana, text="Rules:",
              bg="#2596be", font='verdana 14 bold').grid(row=2, column=1, columnspan=6, )
        Label(en_ventana, text="You have 8 tries before the snow-doll end hangout",
              bg="#2596be", font='verdana 12 bold').grid(row=3, column=1, columnspan=6)
        Label(en_ventana, text="if you lose and you want to repeat again: ",
              bg="#2596be", font='verdana 12 bold').grid(row=4, column=1, columnspan=6)
        Label(en_ventana, text="press 'new Game'",
              bg="#2596be", font='verdana 12 bold').grid(row=5, column=0, columnspan=6)
        Label(en_ventana, text="Hint: The word is a Christmas related word ",
              bg="#2596be", font='verdana 10 bold').grid(row=6, column=1, columnspan=6)
        Label(en_ventana, text="", bg="#2596be", font='verdana 10 bold').grid(row=7, column=0, columnspan=6)
        Label(en_ventana, text="").grid(row=8, column=8)
        Label(en_ventana, text="").grid(row=9, column=9)
        Label(en_ventana, text="").grid(row=10, column=10)

    def keyboard():
        n = 0
        for each_letter in ascii_uppercase:
            Button(window, text=each_letter,
                   command=lambda fill_with_letter=each_letter: guess(fill_with_letter),
                   font='Helvetica 18', width=5).grid(row=9 + n // 9, column=n % 9)
            n += 1

    def new_game_button():
        # set a new game
        Button(window, text="New\nGame",
               command=lambda: white_spaces_dashboard(), font="Helvetica 10 bold").grid(row=11, column=8)

    def guess(letter):
        global number_of_guesses

        if number_of_guesses < 10:
            txt = list(dashboard_in_white)
            guessed = list(white_spaces.get())
            if dashboard_in_white.count(letter) > 0:
                for each_try in range(len(txt)):
                    if txt[each_try] == letter:
                        guessed[each_try] = letter
                    white_spaces.set("".join(guessed))
                    if white_spaces.get() == dashboard_in_white:
                        messagebox.showinfo("Congratulation", "You save the doll!")
            else:
                number_of_guesses += 1
                hangman_images.config(image=images[number_of_guesses], bg="#6daeef")
                if number_of_guesses == 9:
                    messagebox.showwarning("Hangman Game Over", f" The secret word was: \n {the_word}")

    keyboard()
    new_game_button()
    white_spaces_dashboard()
    instructions(window)
    window.mainloop()


def pick_secret_word():
    words = []
    with open("Christmas_words.txt", "rt") as list_of_words:
        for a_word in list_of_words:
            a_word = a_word.strip().upper()
            words.append(a_word)
    randon_word = random.choice(words)
    return randon_word


if __name__ == "__main__":
    main()
