import tkinter as tk
import random
import verif
import clipboard


def main():
    specialChar = "!@#$%^&*()_+-={}[|;:<>,./?~"
    letter = "AaBbCcDdEeFfFgGhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxZz"
    number = "1234567890"

    def getLongueur():
        return longueur.get()

    def getVar_carac():
        return var_caractere.get()

    def getVar_chiffres():
        return var_chiffres.get()

    def getVar_lettres():
        return var_lettres.get()

    def copy_password():
        clipboard.copy(passwordLabel.cget("text"))

    def OpenVerif():
        verif.windows_verif()

    def generatePassword():
        FinalList = ''
        password = []
        if getVar_carac() == 1:
            FinalList += specialChar
        if getVar_chiffres() == 1:
            FinalList += number
        if getVar_lettres() == 1:
            FinalList += letter
        for i in range(getLongueur()):
            index = random.randint(0, len(FinalList)-1)
            password.append(FinalList[index])
        passwordLabel.config(text="".join(password))
        btnCopy.config(state=tk.NORMAL)
        BtnVerifPassword = tk.Button(WindowsPassword, text="Verification", bg="lightgray", command=OpenVerif)
        BtnVerifPassword.pack(pady=20)

    root = tk.Tk()
    root.title("password verification")
    root.geometry("1000x540")
    root.resizable(height=False, width=False)
    root.config(background="lightgray")

    longueur = tk.IntVar()
    var_caractere = tk.IntVar()
    var_lettres = tk.IntVar()
    var_chiffres = tk.IntVar()

    NameWindows = tk.Frame(root, bg="lightgray", relief="raised", borderwidth=5)
    NameWindows.pack(fill="both")
    LabelNameWindows = tk.Label(NameWindows, text="PassGenerator", bg="lightgray", font=('arial', 20, 'bold'))
    LabelNameWindows.pack(side="left", padx=10)

    WindowsPassword = tk.Frame(root, bg="lightgray", relief="sunken", borderwidth=5)
    WindowsPassword.pack(fill="both")

    LabelTypePassword = tk.Label(WindowsPassword, text="Generation", bg="lightgray", font=('Arial', 15, 'bold'))
    LabelTypePassword.pack()

    BtnCaractSpe = tk.Checkbutton(WindowsPassword, text='Caractéres spéciaux', variable=var_caractere, command=getVar_carac,  bg="lightgray")
    BtnCaractSpe.pack()
    BtnLetter = tk.Checkbutton(WindowsPassword, text='Lettres majuscules et minuscules', variable=var_lettres, command=getVar_lettres,  bg="lightgray")
    BtnLetter.pack()
    BtnNumber = tk.Checkbutton(WindowsPassword, text='Chiffres', variable=var_chiffres, command=getVar_chiffres,  bg="lightgray")
    BtnNumber.pack()

    FrameLenghtPassword = tk.Label(WindowsPassword, bg="lightgray")
    FrameLenghtPassword.pack(pady=20)

    labelLenghtPassword = tk.Label(FrameLenghtPassword, text='Longueur du mot de passe : ',  bg="lightgray")
    labelLenghtPassword.pack()
    lenghtScale = tk.Scale(FrameLenghtPassword, from_=1, to=50, length=200, variable=longueur, orient=tk.HORIZONTAL,  bg="lightgray")
    lenghtScale.pack()

    passwordLabel = tk.Label(WindowsPassword, font=("Arial", 15), width=5, text='')
    passwordLabel.pack(ipadx=300, ipady=10, padx=50, pady=10)

    btnCopy = tk.Button(WindowsPassword, text='Copier dans le press papier', command=copy_password,  bg="lightgray", state=tk.DISABLED)
    btnCopy.pack(pady=20)

    BtnGenerate = tk.Button(WindowsPassword, text='Générer le mot de passe', command=generatePassword, bg="lightgray")
    BtnGenerate.pack(pady=20)

    root.mainloop()


if __name__ == '__main__':
    main()
