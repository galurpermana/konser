from tkinter import *
from tkinter import messagebox
from pathlib import Path
from subprocess import call
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")

# Fungsi untuk mengubah path relatif ke path dalam assets
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Fungsi untuk mengatur jendela berada di tengah layar
def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Fungsi untuk validasi input hanya angka
def validate_numeric(value):
    if value.isdigit() or value == "":
        return True
    else:
        messagebox.showerror("Invalid Input", "Please enter a numeric value.")
        return False

# Fungsi untuk membuka halaman formulir pemesanan tiket
def formPage():
    window.destroy()
    call(["python", "form.py"])

# Fungsi untuk menampilkan total pembayaran
def display_total(total):
    label_t.config(text=str(total) + " IDR")

# Fungsi untuk melakukan pembayaran
def submit_payment():
    nama = sys.argv[2]
    jenis = sys.argv[3]
    jml = sys.argv[4]
    rekening = entry_rekening.get()
    pin = entry_pin.get()

    if rekening.strip() == "" or pin.strip() == "":
        messagebox.showerror("Invalid Input", "Please fill in all fields.")
    else:
        window.destroy()
        call(["python", "tiket.py", nama, jenis, jml])

total = sys.argv[1]

# Membuat objek Tkinter
window = Tk()
window.geometry("375x667")
window.title("Aplikasi Pemesanan Tiket Konser BTS")
window.configure(bg="#FFFFFF")

# Membuat canvas dan menambahkan gambar background
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

# Membuat label total
label_total = Label(window, text="Total", font=('Arial bold', 15))
label_total.grid(row=0, column=0, padx=10, pady=(200, 5), sticky='w')

# Menampilkan total pembayaran
label_t = Label(window, text=total, font=('Arial bold', 15))
label_t.grid(row=0, column=1, padx=10, pady=(200, 5), sticky='w')

# Membuat label dan input nomor rekening
label_rekening = Label(window, text="No. Rekening:", font=('Arial bold', 15))
label_rekening.grid(row=1, column=0, padx=10, pady=5)
entry_rekening = Entry(
    window,
    font=('Arial bold', 15),
    width=15,
    validate="key",
    validatecommand=(window.register(validate_numeric), "%P")
)
entry_rekening.grid(row=1, column=1, padx=10, pady=5)

# Membuat label dan input PIN
label_pin = Label(window, text="PIN:", font=('Arial bold', 15))
label_pin.grid(row=2, column=0, padx=10, pady=5, sticky='w')
entry_pin = Entry(window, show="*", font=('Arial bold', 15), width=15)  # Mask the PIN input with asterisks
entry_pin.grid(row=2, column=1, padx=10, pady=5)

# Membuat tombol "Submit"
button_submit = Button(
    window,
    text="Submit",
    command=submit_payment,
    font=('Arial bold', 15),
    bg="#3D5A80",
    fg="#FFFFFF",
    width=10
)
button_submit.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Mengatur jendela berada di tengah layar
center_window(window)
# Menjalankan event loop
window.mainloop()