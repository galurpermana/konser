from pathlib import Path
from tkinter import *
from subprocess import call
from tkinter import ttk, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\py\konser\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")



def validate_numeric(value):
    if value.isdigit() or value == "":
        return True
    else:
        messagebox.showerror("Invalid Input", "Please enter a numeric value.")
        return False

def formPage():
    window.destroy()
    call(["python", "form.py"])



window = Tk()
window.geometry("375x667")
window.title("Aplikasi Pemesanan Tiket Konser BTS")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=667,
    width=375,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("bg2.png"))
image_1 = canvas.create_image(
    187.0,
    337.0,
    image=image_image_1
)

label_rekening = Label(window, text="No. Rekening:", font=('Arial bold', 15))
label_rekening.grid(row=0, column=0, padx=10, pady=(200,5))

label_pin = Label(window, text="PIN:", font=('Arial bold', 15))
label_pin.grid(row=1, column=0, padx=10, pady=5)

# Create the entry forms
entry_rekening = Entry(window,font=('Arial bold', 15), width=15)
entry_rekening.grid(row=0, column=1, padx=10, pady=(200,5))

entry_pin = Entry(window, show="*",font=('Arial bold', 15),width=15)  # Mask the PIN input with asterisks
entry_pin.grid(row=1, column=1, padx=10, pady=5)


button_submit = Button(
    window,
    text="SUBMIT",

)
button_submit.place(
    x=97.0,
    y=500.0,
    width=181.0,
    height=48.0
)
button_back = Button(
    window,
    text="<BACK",
    command=formPage
)
button_back.place(
    x=10.0,
    y=10.0,
    width=50.0,
    height=20.0
)

window.resizable(False, False)
center_window(window)
window.mainloop()