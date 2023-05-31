from pathlib import Path
from tkinter import *
from subprocess import call
from tkinter import ttk, messagebox

# Path untuk assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")

# Fungsi untuk mengembalikan path relatif ke assets
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Fungsi untuk mengatur jendela di tengah layar
def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Fungsi untuk validasi input nama
def validate_entry(text):
    return text.isalpha() or " " in text

# Fungsi untuk mengubah teks nama menjadi huruf kapital
def capitalize_entry(event):
    entry_text = entryNama.get()
    if validate_entry(entry_text):
        capitalized_text = entry_text.upper()
        entryNama.delete(0, END)
        entryNama.insert(0, capitalized_text)
    else:
        entryNama.delete(0, END)

# Fungsi untuk validasi input jumlah tiket
def validate_numeric(value):
    if value.isdigit() or value == "":
        return True
    else:
        messagebox.showerror("Invalid Input", "Please enter a numeric value.")
        return False

# Fungsi untuk mengirimkan formulir
def submit_form():
    nama = entryNama.get()
    jenis = combo.get()
    jml = jumlah.get()

    if not nama or not jenis or not jml:
        messagebox.showerror("Error", "Silakan isi semua field.")
        return

    total = calculate_total()
    window.destroy()
    call(["python", "payment.py", str(total), nama, jenis, jml])

# Fungsi untuk menghitung total harga tiket
def calculate_total():
    ticket_price = 0
    selected_ticket = combo.get()
    if selected_ticket == "BRONZE - 50.000":
        ticket_price = 50000
    elif selected_ticket == "GOLD - 100.000":
        ticket_price = 100000
    elif selected_ticket == "PLATINUM - 150.000":
        ticket_price = 150000

    quantity = int(jumlah.get())
    total = ticket_price * quantity
    return total

# Fungsi untuk kembali ke halaman utama
def mainPage():
    window.destroy()
    call(["python", "main.py"])

# Inisialisasi jendela utama
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

# Membuat label dan field untuk input nama, jenis tiket, dan jumlah tiket
namaLabel = Label(window, text="Nama", font=('Arial bold', 15))
jenisLabel = Label(window, text="Tiket", font=('Arial bold', 15))
jumlahLabel = Label(window, text="Jumlah", font=('Arial bold', 15))

namaLabel.grid(row=2, column=0, padx=10, pady=(150,10), sticky='w')
jenisLabel.grid(row=3, column=0, padx=10, pady=10, sticky='w')
jumlahLabel.grid(row=4, column=0, padx=10, pady=5, sticky='w')

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

# Tombol untuk mengirimkan formulir dan kembali ke halaman utama
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

# Mengatur agar jendela tidak dapat diubah ukurannya
window.resizable(False, False)
# Mengatur jendela berada di tengah layar
center_window(window)
# Menjalankan event loop
window.mainloop()
