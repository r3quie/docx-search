import customtkinter
from docxsearch import main as docxsearch
from local_variables import pathtofolder
import threading

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1320x680")
root.title("Vyhledávání")

frame = customtkinter.CTkFrame(master=root)
frame.grid(pady=30, padx=60, row=0, column=0)

frame2 = customtkinter.CTkFrame(master=root)
frame2.grid(pady=30, padx=180,  row=1, column=0)

def case_in_zivre(zvire):
    if zvire == "Kozy/Ovce":
        return "O"
    elif zvire == "Tuři":
        return "T"
    elif zvire == "Koně":
        return "K"
    elif zvire == "Prasata":
        return "P"

def testy():
    def test():
        case = case_in_zivre(zvire.get())
        yielding = ""
        if rcic.get() == "IČ":
            person = False
        elif rcic.get() == "RČ":
            person = True
        else:
            person = None
        for ii in docxsearch(pathtofolder + case, paragrafy.entry.get("1.0", "end-1c"), person): 
            if yielding == "":
                yielding = ii
                result.configure(text = yielding)
                continue
            yielding += "\n" + ii
            result.configure(text = yielding)
    threading.Thread(target=test).start()

class Entry:
    def __init__(self, text, colnum, rownum, pl_text):
        self.entry = customtkinter.CTkTextbox(master=frame)
        self.entry.grid(column=colnum+1, row=rownum, pady=12, padx=14)
        self.entry.insert("1.0", pl_text)

        self.label = customtkinter.CTkLabel(master=frame, text=text, font=("Arial", 12))
        self.label.grid(column=0 if colnum == 0 else 3, row=rownum, pady=12, padx=10)

class OptionMenu:
    def __init__(self, text, options, colnum, rownumm):
        self.optionmenu = customtkinter.CTkOptionMenu(master=frame, values=options)
        self.optionmenu.set(text)
        self.optionmenu.grid(column=colnum, row=rownumm, pady=12, padx=12)
    
    def get(self):
        return self.optionmenu.get()
    

paragrafy = Entry("Zadejte vyhledávané ustanovení", 0, 2, "§ 15 odst. 4 písm c)\n§ 23 odst. 1 písm. c)\n§ 24 odst. 2 písm. b)\n§ 15 odst. 4 písm c)")

label = customtkinter.CTkLabel(master=frame, text="Vyhledávání", font=("Arial", 24))
label.grid(pady=12, padx=10, columnspan=4, row=0)

result = customtkinter.CTkLabel(master=frame2, text =f"Výsledek", justify="left")
result.grid(pady=12, padx=10, column=6, row=0)

zvire = OptionMenu("Zvíře", ["Kozy/Ovce", "Tuři", "Koně", "Prasata"], 0, 1)
rcic = OptionMenu("RČ nebo IČ?", ["IČ", "RČ", "Oba"], 1, 1)

button = customtkinter.CTkButton(master=frame, text="Vyhledat", command=testy)
button.grid(pady=12, padx=10, columnspan=4, row=5)


root.mainloop()