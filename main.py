from pathlib import Path
from tkinter import *
from subprocess import call

# Menentukan path output dan path assets
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

# Membuat objek Tkinter
window = Tk()

# Fungsi untuk membuka halaman formulir pemesanan tiket
def formPage():
    window.destroy()
    call(["python", "form.py"])

# Mengatur ukuran dan judul jendela
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
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    190.0,
    333.0,
    image=image_image_1
)

# Membuat tombol "BUY NOW"
button_1 = Button(
    window,
    text="BUY NOW",
    command=formPage
)
button_1.place(
    x=97.0,
    y=333.0,
    width=181.0,
    height=48.0
)

# Mengatur agar jendela tidak dapat diubah ukurannya
window.resizable(False, False)
# Mengatur jendela berada di tengah layar
center_window(window)
# Menjalankan event loop
window.mainloop()