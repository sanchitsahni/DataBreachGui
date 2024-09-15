import tkinter as tk
import customtkinter as ctk
import requests as rq

# window intialization
def windowDesign():
    root.title("Enigma Breach Checker")
    root.iconbitmap("images/favicon-16x16.ico")
    root.geometry("480x480")
    root.eval("tk::PlaceWindow . center")
    root.resizable(False, False)
    ctk.set_default_color_theme("blue")


def api_call(email):
    root = ctk.CTk()
    windowDesign()
    url = "https://api.xposedornot.com/v1/check-email/{0}".format(email)
    print(url)
    response = rq.get(url)
    data = response.json()
    error = 0
    if "breaches" in data :
        data = data.get("breaches", [[]])
    else:    
        error = data.get("Error",[])
    num_breaches = len(data)
    num_lines = 3  
    window_height = 400 + 100 * num_breaches 
    root.geometry(f"480x{window_height}")
    root.eval("tk::PlaceWindow . center")
    message = f"Your data has been found in: \n"
    if error:
        message = "No breaches found."
        message_label = ctk.CTkLabel(root, text=message, font=("Inter", 40, "bold"))
        message_label.place (x=110,y=20)
    elif data:
        for breach in data:
            for element in breach[:20:]:
                message += f"\n- {element}"
        message_label = ctk.CTkLabel(root, text=message, font=("Inter", 24))
        message_label.place (x=80,y=20,)   

    root.mainloop()

def mainWindow():
    windowDesign()
    label1 = ctk.CTkLabel(
        root, text="Breach Detector ", font=("Inter", 56,"bold"),text_color="#209ffc"
    ).place(x=25, y=20)
    label2 = ctk.CTkLabel(
        root,
        text=" Data Breaches :  563 \n Exposed Records :  9,988,721,591 \n Exposed Emails :  4,511,047,726  \n Exposed Passwords : 835,955,029  ",
        font=(
            "Inter",
            24,
        ),
        justify="center",
    text_color="#209ffc",
    ).place(x=40, y=120)
    emailEntry = ctk.CTkEntry(root, font=("Inter", 24), width=400, height=8)
    emailEntry.place(
        x=40,
        y=260,
    )
    def getemail():
        email = emailEntry.get()
        if email:
         api_call(email)
    searchbtn = ctk.CTkButton(
        root, text="search", command=getemail, font=("Inter", 24), width=80, height=16
    ).place(x=90, y=340)

root =""
# window
def main():
    global root
    root = ctk.CTk()
    mainWindow()

    root.mainloop()


if __name__ == "__main__":
    main()
