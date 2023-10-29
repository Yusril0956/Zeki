import tkinter as tk
from tkinter import messagebox

# Daftar informasi akun
user_accounts = {
    'apa lah': 'halo',
    'username2': 'password2'
}

# Fungsi untuk memeriksa login
def daftar():
    
    user_info = {
       input('Username : '): input('Password : ')
    }
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    logged_in = False



    username = username_entry.get()
    password = password_entry.get()
# Membuat jendela utama
root = tk.Tk()
root.title("Daftar")

# Membuat label
username_label = tk.Label(root, text="Username:")
password_label = tk.Label(root, text="Password:")

# Membuat input field
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")  # Menyembunyikan karakter password

# Membuat tombol login
daftar_button = tk.Button(root, text="Daftar", command=daftar)

# Mengatur tata letak elemen-elemen GUI
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
daftar_button.pack()

# Memulai loop GUI
root.mainloop()
