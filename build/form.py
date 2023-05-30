from pathlib import Path
from tkinter import *
from subprocess import call
from tkinter import ttk, messagebox
from payment import on_submit

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

def validate_entry(text):
    return text.isalpha() or " " in text

def capitalize_entry(event):
    entry_text = entryNama.get()
    if validate_entry(entry_text):
        capitalized_text = entry_text.upper()
        entryNama.delete(0, END)
        entryNama.insert(0, capitalized_text)
    else:
        entryNama.delete(0, END)

def validate_numeric(value):
    if value.isdigit() or value == "":
        return True
    else:
        messagebox.showerror("Invalid Input", "Please enter a numeric value.")
        return False

def mainPage():
    window.destroy()
    call(["python", "main.py"])

def submit_form():
    nama_pembeli = entryNama.get()
    jenis_tiket = combo.get()
    jumlah_tiket = jumlah.get()

    # Panggil fungsi on_submit di file payment.py
    on_submit(nama_pembeli, jenis_tiket, jumlah_tiket)

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

namaLabel = Label(window, text="Nama", font=('Arial bold', 15))
jenisLabel = Label(window, text="Tiket", font=('Arial bold', 15))
jumlahLabel = Label(window, text="Jumlah", font=('Arial bold', 15))

namaLabel.grid(row=2, column=0, padx=30, pady=(150,10))
jenisLabel.grid(row=3, column=0, padx=10, pady=10)
jumlahLabel.grid(row=4, column=0, padx=0, pady=5)

entryNama = Entry(window, width=20, font=('Arial bold', 15))
combo = ttk.Combobox(
    state="readonly",
    values=["BRONZE - 50.000","GOLD - 100.000","PLATINUM - 150.000"],
    font=('Arial bold', 15),
    width=18
)
jumlah = Spinbox(window, from_=1, to=100, width=19, font=('Arial bold', 15),
                 validate="key",
                 validatecommand=(window.register(validate_numeric), "%P")
                 )

entryNama.bind("<KeyRelease>", capitalize_entry)
entryNama.grid(row=2, column=1, columnspan=2, padx=0, pady=(150,5))
combo.grid(row=3, column=1, columnspan=2, padx=0, pady=5)
jumlah.grid(row=4, column=1, columnspan=2, padx=0, pady=5)

button_submit = Button(
    window,
    text="SUBMIT",
    command=submit_form
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
    command=mainPage
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
