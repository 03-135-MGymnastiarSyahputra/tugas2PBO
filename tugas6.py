import tkinter as tk
from tkinter import ttk, messagebox
import os

# --- Helper Functions ---
def load_users():
    """Memuat data pengguna dari file 'users.txt' ke dalam dictionary"""
    users = {}
    if os.path.exists("users.txt"):  # Cek jika file ada
        with open("users.txt", "r") as f:
            for line in f:
                username, password = line.strip().split(",")
                users[username] = password  # Tambahkan ke dictionary
    return users

def save_user(username, password):
    """Menyimpan data pengguna baru ke file 'users.txt'"""
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")

# --- Kelas Aplikasi Utama ---
class App:
    def __init__(self, root):
        """Inisialisasi aplikasi"""
        self.root = root
        self.root.title("Login & Register")        # Judul window
        self.root.geometry("400x400")              # Ukuran window
        self.root.config(bg="#f0f4f7")              # Warna latar belakang
        self.show_login()                          # Tampilkan tampilan login pertama

    def clear_frame(self):
        """Menghapus semua widget dari jendela"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login(self):
        """Menampilkan tampilan login"""
        self.clear_frame()
        tk.Label(self.root, text="Login", font=("Arial", 20, "bold"), bg="#f0f4f7", fg="#333").pack(pady=20)

        # Input username
        tk.Label(self.root, text="Username", bg="#f0f4f7").pack()
        self.username_entry = tk.Entry(self.root, bg="#e1f5fe")
        self.username_entry.pack(pady=5)

        # Input password
        tk.Label(self.root, text="Password", bg="#f0f4f7").pack()
        self.password_entry = tk.Entry(self.root, show="*", bg="#e1f5fe")
        self.password_entry.pack(pady=5)

        # Tombol login
        tk.Button(self.root, text="Login", command=self.login, bg="#4caf50", fg="white").pack(pady=10)
        
        # Tombol ke halaman register
        tk.Button(self.root, text="Register", command=self.show_register, bg="#2196f3", fg="white").pack()

    def show_register(self):
        """Menampilkan tampilan registrasi"""
        self.clear_frame()
        tk.Label(self.root, text="Register", font=("Arial", 20, "bold"), bg="#f0f4f7", fg="#333").pack(pady=20)

        # Input username
        tk.Label(self.root, text="Username", bg="#f0f4f7").pack()
        self.reg_username = tk.Entry(self.root, bg="#fff9c4")
        self.reg_username.pack(pady=5)

        # Input password
        tk.Label(self.root, text="Password", bg="#f0f4f7").pack()
        self.reg_password = tk.Entry(self.root, show="*", bg="#fff9c4")
        self.reg_password.pack(pady=5)

        # Konfirmasi password
        tk.Label(self.root, text="Confirm Password", bg="#f0f4f7").pack()
        self.reg_confirm = tk.Entry(self.root, show="*", bg="#fff9c4")
        self.reg_confirm.pack(pady=5)

        # Tombol submit register
        tk.Button(self.root, text="Submit", command=self.register, bg="#ff9800", fg="white").pack(pady=10)
        # Tombol kembali ke login
        tk.Button(self.root, text="Back to Login", command=self.show_login, bg="#9e9e9e", fg="white").pack()

    def login(self):
        """Proses login pengguna"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        users = load_users()

        # Validasi login
        if username in users and users[username] == password:
            self.show_dashboard(username)  # Login berhasil
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def register(self):
        """Proses registrasi pengguna baru"""
        username = self.reg_username.get()
        password = self.reg_password.get()
        confirm = self.reg_confirm.get()

        users = load_users()

        # Validasi data
        if username in users:
            messagebox.showerror("Error", "Username already exists!")
        elif password != confirm:
            messagebox.showerror("Error", "Passwords do not match!")
        elif username == "" or password == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            save_user(username, password)
            messagebox.showinfo("Success", "Registered successfully!")
            self.show_login()  # Kembali ke halaman login

    def show_dashboard(self, username):
        """Menampilkan halaman setelah login berhasil"""
        self.clear_frame()
        tk.Label(self.root, text=f"Welcome, {username}!", font=("Arial", 20, "bold"), bg="#f0f4f7", fg="#333").pack(pady=30)
        tk.Label(self.root, text="🎉 You have successfully logged in 🎉", bg="#f0f4f7", fg="#2e7d32", font=("Arial", 12)).pack()
        
        # Tombol logout
        tk.Button(self.root, text="Logout", command=self.show_login, bg="#f44336", fg="white").pack(pady=20)

# --- Menjalankan Aplikasi ---
if __name__ == "__main__":
    root = tk.Tk()      # Membuat jendela utama
    app = App(root)     # Menjalankan aplikasi dengan root
    root.mainloop()     # Memulai loop GUI
