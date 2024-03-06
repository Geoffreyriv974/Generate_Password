import tkinter as tk
import random
import verif


def main():
    root = tk.Tk()
    root.title("password generator")
    root.geometry("1000x500")
    root.resizable(height=False, width=False)

    len_password = 0
    tab_password = []

    name_windows = tk.Label(root, background="gray", foreground="white", text="password generator",
                            font=("Arial", 20, 'bold'), width=120, border=2, relief=tk.RAISED, borderwidth=5, height=2)
    name_windows.pack()

    windows_Frame = tk.Frame(root, bg="gray", relief=tk.SUNKEN, border=2, borderwidth=5)
    windows_Frame.pack()

    generate_name = tk.Label(windows_Frame, text="Generate", font=("Arial", 18, 'bold'), background="gray",
                             foreground="white", width=120)
    generate_name.pack()

    def update_label():
        input_length.config(text=len_password)
        password.config(text="".join(tab_password))

    def click_on_btn_spe():
        nonlocal len_password
        len_password = len_password + 1

        tab_spe = "!@#$%^&*()_+-={}[|;:'\<>,./?~"

        spe_random = random.choice(tab_spe)
        tab_password.append(spe_random)

        update_label()

    def click_on_btn_maj_min():
        nonlocal len_password
        len_password = len_password + 1

        tab_min_maj = "AZERTYUIOPMLKJHGFDSQWXCVBN"

        if random.choice([True, False]):
            tab_min_maj = tab_min_maj.lower()
        else:
            tab_min_maj = tab_min_maj.upper()

        min_maj_random = random.choice(tab_min_maj)
        tab_password.append(min_maj_random)

        update_label()

    def click_on_btn_number():
        nonlocal len_password
        len_password = len_password + 1

        tab_number = "1234567890"

        number_random = random.choice(tab_number)
        tab_password.append(number_random)

        update_label()

    frame_1 = tk.Frame(windows_Frame, bg="gray")
    frame_1.pack()
    btn_spe = tk.Button(frame_1, text="X", font=("Arial", 15), borderwidth=5, relief=tk.RAISED, fg="white", bg="gray",
                        command=click_on_btn_spe)
    btn_spe.pack(side="left")
    text_spe = tk.Label(frame_1, text="Caractères spéciaux", bg='gray', foreground="white", font=("Arial", 15))
    text_spe.pack(side="left")

    frame_2 = tk.Frame(windows_Frame, bg="gray")
    frame_2.pack()
    btn_maj_min = tk.Button(frame_2, text="X", font=("Arial", 15), borderwidth=5, relief=tk.RAISED, fg="white",
                            background="gray", command=click_on_btn_maj_min)
    btn_maj_min.pack(side="left")
    text_maj_min = tk.Label(frame_2, text="Majuscule ou minusule", bg='gray', foreground="white", font=("Arial", 15))
    text_maj_min.pack(side="left")

    frame_3 = tk.Frame(windows_Frame, bg="gray")
    frame_3.pack()
    btn_number = tk.Button(frame_3, text="X", font=("Arial", 15), borderwidth=5, relief=tk.RAISED, fg="white",
                           background="gray", command=click_on_btn_number)
    btn_number.pack(side="left")
    text_number = tk.Label(frame_3, text="Chiffre", bg='gray', foreground="white", font=("Arial", 15))
    text_number.pack(side="left")

    frame_4 = tk.Frame(windows_Frame, bg="gray")
    frame_4.pack()
    text_length = tk.Label(frame_4, text="Longueur mot de passe :", font=("Arial", 15), fg="white", bg="gray")
    text_length.pack(side="left")
    input_length = tk.Label(frame_4, font=("Arial", 10), width=10, text=len_password, borderwidth=5)
    input_length.pack(side="left")

    password = tk.Label(windows_Frame, font=("Arial", 15), width=10, borderwidth=5)
    password.pack(ipadx=150, ipady=10, padx=50, pady=10)

    btn_valid_password = tk.Button(windows_Frame, borderwidth=3, text="Valider", fg="white", bg="gray", font=("Arial", 15), command=verif.verif)
    btn_valid_password.pack(pady=48)

    root.mainloop()


if __name__ == '__main__':
    main()
