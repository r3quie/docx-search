import customtkinter
from docxsearch import main as docxsearch

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1320x680")
root.title("Vyhledávání")

frame = customtkinter.CTkFrame(master=root)
frame.grid(pady=30, padx=60)

def testy():
    result.configure(text=f"{globals()['paragrafy.entry%s.get()' % 1]}")

class Entry:
    def __init__(self, text, colnum, rownum, pl_text):
        i = 0
        for holder in pl_text:
            globals()['self.entry%s' % i] = customtkinter.CTkEntry(master=frame, placeholder_text=holder)
            globals()['self.entry%s.grid(column=colnum+1, row=rownum+i, pady=12, padx=14)' % i]
            i += 1

        self.label = customtkinter.CTkLabel(master=frame, text=text, font=("Arial", 12))
        self.label.grid(column=0 if colnum == 0 else 3, row=rownum, pady=12, padx=10)

class OptionMenu:
    def __init__(self, text, options, colnum, rownumm):
        self.optionmenu = customtkinter.CTkOptionMenu(master=frame, values=options)
        self.optionmenu.set(text)
        self.optionmenu.grid(column=colnum, row=rownumm, pady=12, padx=12)
    
    def get(self):
        return self.optionmenu.get()
    

paragrafy = Entry("Zadejte vyhledávané ustanovení", 0, 1, ("§ 15 odst. 4 písm c)", "§ 23 odst. 1 písm. c)", "§ 24 odst. 2 písm. b)", "§ 15 odst. 4 písm c)"))

label = customtkinter.CTkLabel(master=frame, text="Vyhledávání", font=("Arial", 24))
label.grid(pady=12, padx=10, columnspan=4, row=0)

result = customtkinter.CTkLabel(master=frame, text =f"yelllllllllloooooooo")
result.grid(pady=12, padx=10, columnspan=6, row=6)

button = customtkinter.CTkButton(master=frame, text="Vygenerovat", command=testy)
button.grid(pady=12, padx=10, columnspan=4, row=5)


root.mainloop()