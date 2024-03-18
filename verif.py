import tkinter as tk


def windows_verif():

    windows_verfication = tk.Toplevel()
    windows_verfication.title("password verification")
    windows_verfication.geometry("1000x500")
    windows_verfication.resizable(height=False, width=False)
    windows_verfication.config(background="lightgray")

    NameWindows = tk.Frame(windows_verfication, bg="lightgray", relief="raised", borderwidth=5)
    NameWindows.pack(fill="both")
    LabelNameWindows = tk.Label(NameWindows, text="PassGenerator", bg="lightgray", font=('arial', 20, 'bold'))
    LabelNameWindows.pack(side="left", padx=10)

    WindowsPassword = tk.Frame(windows_verfication, bg="lightgray", relief="sunken", borderwidth=5)
    WindowsPassword.pack(fill="both")

    LabelTypePassword = tk.Label(WindowsPassword, text="Vérification", bg="lightgray", font=('Arial', 15, 'bold'))
    LabelTypePassword.pack()

    FramePassword = tk.Frame(WindowsPassword, bg="lightgray")
    FramePassword.pack(pady=50)

    passwordLabel = tk.Label(FramePassword, text="Password :", bg="lightgray", font=('Arial', 15, 'bold'))
    passwordLabel.pack()
    password = tk.Entry(FramePassword, font=("Arial", 15), width=5, justify="center")
    password.pack(ipadx=300, ipady=10, padx=50, pady=10)

    def ValidPasswordFonction():
        FrameEnd = tk.Frame(WindowsPassword, bg="lightgray")
        FrameEnd.pack()

        FrameViewScore = tk.Frame(FrameEnd, bg="lightgray")
        FrameViewScore.pack(side="left", padx=100, pady=40)
        FrameScore = tk.Frame(FrameEnd, bg="lightgray")
        FrameScore.pack(side="right", padx=100, pady=40)

        length_password = len(password.get())
        specialChar = "!@#$%^&*()_+-={}[|;:<>,./?~"
        GetPassword = password.get()

        valid_special_characters = "NO"
        valid_liste = "NO"

        score_password = 0

        if length_password > 8:
            valid_character = "OK"
            score_password = score_password + 2
        else:
            valid_character = "NO"

        for i in GetPassword:
            if i in specialChar:
                valid_special_characters = "OK"
                score_password = score_password + 3
                break

        file_name = "list"

        with open(file_name, 'r') as file:
            for line in file:
                if GetPassword.strip() != line.strip():
                    valid_liste = "OK"
                    score_password = score_password + 5
                    break

        text_character = f"{valid_character} - {length_password} characters"
        text_special_characters = f"{valid_special_characters} - Special characters presents"
        text_list = f"{valid_liste} - Not Present on database list"

        text_score = f"{score_password} / 10"

        Number_character = tk.Label(FrameViewScore, text=text_character, bg="lightgray", font=("arial", 15))
        Number_character.pack()
        Special_character = tk.Label(FrameViewScore, text=text_special_characters, bg="lightgray", font=("arial", 15))
        Special_character.pack()
        NotDatabase = tk.Label(FrameViewScore, text=text_list, bg="lightgray", font=("arial", 15))
        NotDatabase.pack()

        Score = tk.Label(FrameScore, text=text_score, bg="lightgray", font=("Arial", 40, "bold"))
        Score.pack()

        if score_password < 3:
            Score.config(fg="red")
        elif 3 <= score_password < 7:
            Score.config(fg="orange")
        else:
            Score.config(fg="green")

    btnVerifPassword = tk.Button(FramePassword, text="Verify", font=("Arial", 15), relief="raised", bg="lightgray", borderwidth=5, command=ValidPasswordFonction)
    btnVerifPassword.pack()

    windows_verfication.mainloop()
