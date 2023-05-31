import random
import string
import sys
from pathlib import Path
from tkinter import *
from subprocess import call

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")


def formPage():
    window.destroy()
    call(["python", "form.py"])


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

nama = sys.argv[1]
jenis = sys.argv[2]
jml = sys.argv[3]


def generate_booking_code(length):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return code


booking_codes = []
for _ in range(int(jml)):
    code = generate_booking_code(8)  # Change the length as per your requirement
    booking_codes.append(code)

print(booking_codes)

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
label_nama.grid(row=0, column=0, padx=10, pady=(200, 5), sticky='w')
label_n = Label(window, text=nama, font=('Arial bold', 15))
label_n.grid(row=0, column=1, padx=10, pady=(200, 5), sticky='w')

label_jenis = Label(window, text="Jenis. Tiket :", font=('Arial bold', 15))
label_jenis.grid(row=1, column=0, padx=10, pady=5, sticky='w')
label_j = Label(window, text=jenis, font=('Arial bold', 15))
label_j.grid(row=1, column=1, padx=10, pady=5, sticky='w')

label_jumlah = Label(window, text="Jumlah Tiket :", font=('Arial bold', 15))
label_jumlah.grid(row=2, column=0, padx=10, pady=5, sticky='w')
label_jml = Label(window, text=jml, font=('Arial bold', 15))
label_jml.grid(row=2, column=1, padx=10, pady=5, sticky='w')

label_tiket = Label(window, text="Kode Tiket :", font=('Arial bold', 15))
label_tiket.grid(row=3, column=0, padx=10, pady=5, sticky='nw')

text_frame = Frame(window)
text_frame.grid(row=3, column=1, padx=10, pady=5, sticky='w')

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)

text_t = Text(text_frame, font=('Arial bold', 15), height=8, width=15, yscrollcommand=scrollbar.set)
text_t.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=text_t.yview)

for code in booking_codes:
    text_t.insert(END, code + '\n')

print(booking_codes)


def formPage():
    window.destroy()
    call(["python", "form.py"])


button_1 = Button(
    window,
    text="BELI LAGI",
    command=formPage
)
button_1.place(
    x=97.0,
    y=600.0,
    width=181.0,
    height=48.0
)

window.resizable(False, False)
center_window(window)
window.mainloop()
