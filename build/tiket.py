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

label_nama = Label(window, text="Nama:", font=('Arial bold', 15))
label_nama.grid(row=0, column=0, padx=10, pady=(200,5), sticky='e')
label_n = Label(window, text="nama", font=('Arial bold', 15))
label_n.grid(row=0, column=1, padx=10, pady=(200,5),sticky='w')

label_jenis = Label(window, text="Jenis. Tiket :", font=('Arial bold', 15))
label_jenis.grid(row=1, column=0, padx=10, pady=5, sticky='e')
label_j = Label(window, text="jenis tiket", font=('Arial bold', 15))
label_j.grid(row=1, column=1, padx=10, pady=5, sticky='w')

label_tiket = Label(window, text="No. Tiket :", font=('Arial bold', 15))
label_tiket.grid(row=2, column=0, padx=10, pady=5, sticky='e')
label_t = Label(window, text="no. tiket", font=('Arial bold', 15))
label_t.grid(row=2, column=1, padx=10, pady=5, sticky='w')



window.resizable(False, False)
center_window(window)
window.mainloop()