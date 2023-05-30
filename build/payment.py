from tkinter import *
from tkinter import messagebox
from pathlib import Path
from subprocess import call
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")

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

def display_total(total):
    label_t.config(text=str(total) + " IDR")

def submit_payment():
    # Perform payment processing here
    # After successful payment, you can redirect to a success page or perform other actions
    messagebox.showinfo("Payment Successful", "Payment has been processed successfully.")
    window.destroy()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        total = int(sys.argv[1])
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

        label_total = Label(window, text="Total", font=('Arial bold', 15))
        label_total.grid(row=0, column=0, padx=10, pady=(200, 5))

        label_t = Label(window, text="", font=('Arial bold', 15))
        label_t.grid(row=0, column=1, padx=10, pady=(200, 5), sticky='w')
        display_total(total)

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

        label_pin = Label(window, text="PIN:", font=('Arial bold', 15))
        label_pin.grid(row=2, column=0, padx=10, pady=5)
        entry_pin = Entry(window, show="*", font=('Arial bold', 15), width=15)  # Mask the PIN input with asterisks
        entry_pin.grid(row=2, column=1, padx=10, pady=5)

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

        center_window(window)
        window.mainloop()

