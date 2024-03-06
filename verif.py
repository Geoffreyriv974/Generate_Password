import tkinter as tk
import main


def verif():

    windows_verif = tk.Toplevel()
    windows_verif.title("confirm password")
    windows_verif.geometry("1000x500")
    windows_verif.resizable(height=False, width=False)

    name_windows = tk.Label(windows_verif, background="gray", foreground="white", text="password generator", font=("Arial", 20, 'bold'), width=120, border=2, relief=tk.RAISED, borderwidth=5, height=2)
    name_windows.pack()

    windows_Frame = tk.Frame(windows_verif, bg="gray", relief=tk.SUNKEN, border=2, borderwidth=5)
    windows_Frame.pack()

    generate_name = tk.Label(windows_Frame, text="Validate", font=("Arial", 18, 'bold'), background="gray",foreground="white", width=120)
    generate_name.pack()

    password = tk.Label(windows_Frame, text="password :", bg="gray", foreground="white", font=("Arial", 15, ' bold'))
    password.pack(anchor="w", padx=15)

    password_valid = tk.Label(windows_Frame, font=("Arial", 15), width=10, borderwidth=5, text="TEST")
    password_valid.pack(anchor="w", ipadx=150, ipady=10, padx=10, pady=10)

    windows_verif.mainloop()
