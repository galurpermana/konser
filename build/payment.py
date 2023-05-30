from tkinter import Tk, Label, Button, Entry, messagebox

def generate_invoice(nama_pembeli, jenis_tiket, jumlah_tiket, no_rekening):
    # Proses pembuatan invoice dan pengiriman ke email atau penyimpanan ke database
    # Kode ini akan menghasilkan nomor pembayaran (contoh: no_pembayaran = "12345678")

    # Mengembalikan nomor pembayaran yang dihasilkan
    return no_pembayaran

def generate_ticket(no_pembayaran, password_rekening):
    # Proses pembuatan tiket berdasarkan nomor pembayaran dan password rekening
    # Kode ini akan menghasilkan nomor tiket (contoh: no_tiket = "TICKET123")

    # Mengembalikan nomor tiket yang dihasilkan
    return no_tiket

def on_submit(nama_pembeli, jenis_tiket, jumlah_tiket, no_rekening):
    no_pembayaran = generate_invoice(nama_pembeli, jenis_tiket, jumlah_tiket, no_rekening)

    payment_window = Tk()
    payment_window.geometry("375x667")
    payment_window.title("Halaman Pembayaran")
    payment_window.configure(bg="#FFFFFF")

    no_pembayaran_label = Label(payment_window, text="Nomor Pembayaran:", font=('Arial', 15))
    no_pembayaran_label.pack(pady=30)

    no_pembayaran_entry = Entry(payment_window, font=('Arial', 12))
    no_pembayaran_entry.pack()

    def check_payment():
        input_pembayaran = no_pembayaran_entry.get()
        if input_pembayaran == no_pembayaran:
            no_tiket = generate_ticket(no_pembayaran, password_rekening_entry.get())
            messagebox.showinfo("Pembayaran Berhasil", f"Nomor Tiket Anda: {no_tiket}")
            payment_window.destroy()
        else:
            messagebox.showerror("Pembayaran Gagal", "Nomor Pembayaran Salah")

    password_rekening_label = Label(payment_window, text="Password Rekening:", font=('Arial', 15))
    password_rekening_label.pack()

    password_rekening_entry = Entry(payment_window, font=('Arial', 12), show='*')
    password_rekening_entry.pack()

    submit_button = Button(payment_window, text="Cek Pembayaran", command=check_payment)
    submit_button.pack(pady=20)

    payment_window.mainloop()
