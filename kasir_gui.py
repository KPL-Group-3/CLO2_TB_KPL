import tkinter as tk
from tkinter import ttk, messagebox

class ItemBelanja:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

def login(username, password):
    return username == "admin" and password == "1234"

class KasirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kasir Feminin")
        self.root.geometry("900x600")
        self.root.configure(bg='#F8EAFB')

        self.kasir = []
        self.riwayat_transaksi = []
        self.menu_items = [
            ItemBelanja("Indomie", 3000, 1),
            ItemBelanja("Aqua", 5000, 1),
            ItemBelanja("Teh Botol", 7000, 1),
            ItemBelanja("Roti Tawar", 12000, 1),
            ItemBelanja("Susu UHT", 8000, 1),
        ]

        self.username = None
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",
            background="#ffffff",
            foreground="black",
            rowheight=25,
            fieldbackground="#F8EAFB",
            font=("Segoe UI", 11))
        self.style.map("Treeview", background=[('selected', '#D1C4E9')])

        self.build_login_page()

    def build_login_page(self):
        self.clear_root()
        frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief=tk.RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=400, height=300)

        tk.Label(frame, text="Login Kasir", font=("Segoe UI", 18, "bold"), bg="#ffffff", fg="#967bb6").pack(pady=10)
        tk.Label(frame, text="Username", bg="#ffffff", anchor="w").pack(fill="x", padx=30, pady=(10,0))
        self.username_entry = tk.Entry(frame, font=("Segoe UI", 12))
        self.username_entry.pack(padx=30, fill="x")

        tk.Label(frame, text="Password", bg="#ffffff", anchor="w").pack(fill="x", padx=30, pady=(10,0))
        self.password_entry = tk.Entry(frame, show='*', font=("Segoe UI", 12))
        self.password_entry.pack(padx=30, fill="x")

        tk.Button(frame, text="Login", command=self.handle_login, font=("Segoe UI", 12), bg="#967bb6", fg="white", height=2).pack(pady=20, padx=30, fill="x")

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if login(username, password):
            self.username = username
            self.build_dashboard()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah!")

    def build_dashboard(self):
        self.clear_root()
        frame = tk.Frame(self.root, bg="#F8EAFB")
        frame.pack(expand=True)

        tk.Label(frame, text=f"Halo, {self.username}!", font=("Segoe UI", 22, "bold"), bg="#F8EAFB", fg="#6A1B9A").pack(pady=30)

        button_style = {"font": ("Segoe UI", 14), "bg": "#BA68C8", "fg": "white", "padx": 20, "pady": 10}

        tk.Button(frame, text="💼  Mulai Transaksi", command=self.build_main_ui, **button_style).pack(pady=10, ipadx=20, fill="x")
        tk.Button(frame, text="📄  Lihat Mutasi", command=self.show_mutasi, **button_style).pack(pady=10, ipadx=20, fill="x")
        tk.Button(frame, text="🚪  Logout", command=self.build_login_page, font=("Segoe UI", 12), bg="#E1BEE7", fg="white").pack(pady=40, ipadx=10, fill="x")

    def show_mutasi(self):
        self.clear_root()
        frame = tk.Frame(self.root, bg="#F8EAFB")
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        tk.Label(frame, text="📄 Riwayat Transaksi", font=("Segoe UI", 18, "bold"), bg="#F8EAFB", fg="#8E24AA").pack(pady=10)

        text_area = tk.Text(frame, font=("Segoe UI", 12))
        text_area.pack(fill="both", expand=True, pady=10)

        if not self.riwayat_transaksi:
            text_area.insert(tk.END, "Belum ada transaksi.")
        else:
            for i, struk in enumerate(self.riwayat_transaksi, 1):
                text_area.insert(tk.END, f"Transaksi {i}\n{struk}\n{'-'*40}\n")

        tk.Button(frame, text="🔙 Kembali ke Dashboard", command=self.build_dashboard, font=("Segoe UI", 12), bg="#CE93D8", fg="white").pack(pady=5)

    def build_main_ui(self):
        self.clear_root()
        tk.Label(self.root, text=f"Transaksi oleh {self.username}", font=("Segoe UI", 14), bg="#F8EAFB", fg="#6A1B9A").pack(pady=10)

        frame = tk.Frame(self.root, bg="#F8EAFB")
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        left_frame = tk.Frame(frame, bg="#ffffff", bd=2, relief=tk.RIDGE)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        right_frame = tk.Frame(frame, bg="#ffffff", bd=2, relief=tk.RIDGE)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(left_frame, text="Daftar Belanja", font=("Segoe UI", 14, "bold"), bg="#ffffff", fg="#6A1B9A").pack(pady=10)
        self.tree = ttk.Treeview(left_frame, columns=("#1", "#2", "#3"), show="headings", height=18)
        self.tree.heading("#1", text="Produk")
        self.tree.heading("#2", text="Jumlah")
        self.tree.heading("#3", text="Subtotal")
        self.tree.column("#1", anchor="w", width=150)
        self.tree.column("#2", anchor="center", width=80)
        self.tree.column("#3", anchor="e", width=120)
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        self.total_label = tk.Label(left_frame, text="Subtotal: Rp 0", font=("Segoe UI", 16, "bold"), fg="#8E24AA", bg="#ffffff")
        self.total_label.pack(pady=10)

        tk.Label(right_frame, text="Tambah Produk", font=("Segoe UI", 14, "bold"), bg="#ffffff", fg="#6A1B9A").pack(pady=10)
        tk.Label(right_frame, text="Produk", bg="#ffffff").pack()
        self.selected_item = tk.StringVar()
        self.combobox = ttk.Combobox(right_frame, textvariable=self.selected_item, values=["Pilih Barang"] + [item.nama for item in self.menu_items], font=("Segoe UI", 12), state="readonly")
        self.combobox.set("Pilih Barang")
        self.combobox.pack(padx=10, fill="x")

        tk.Label(right_frame, text="Jumlah", bg="#ffffff").pack(pady=(10,0))
        self.quantity_entry = tk.Entry(right_frame, font=("Segoe UI", 12))
        self.quantity_entry.pack(padx=10, fill="x")

        tk.Button(right_frame, text="Tambah", command=self.tambah_item, font=("Segoe UI", 12), bg="#967bb6", fg="white").pack(pady=10, padx=10, fill="x")
        tk.Button(right_frame, text="Hapus Item", command=self.hapus_item, font=("Segoe UI", 12), bg="#967bb6", fg="white").pack(pady=5, padx=10, fill="x")

        tk.Label(right_frame, text="Metode Pembayaran", font=("Segoe UI", 14, "bold"), bg="#ffffff", fg="#6A1B9A").pack(pady=(20, 5))
        self.payment_method = tk.StringVar()
        metode_opsi = ["Tunai", "Debit", "QRIS", "Transfer"]
        self.payment_combobox = ttk.Combobox(right_frame, textvariable=self.payment_method, values=metode_opsi, font=("Segoe UI", 12), state="readonly")
        self.payment_combobox.set(metode_opsi[0])
        self.payment_combobox.pack(padx=10, fill="x")
        self.payment_combobox.bind("<<ComboboxSelected>>", self.on_payment_method_change)

        self.uang_tunai_label = tk.Label(right_frame, text="Uang Tunai", font=("Segoe UI", 12), bg="#ffffff")
        self.uang_tunai_entry = tk.Entry(right_frame, font=("Segoe UI", 12))
        self.uang_tunai_label.pack(padx=10, pady=(10,0), fill="x")
        self.uang_tunai_entry.pack(padx=10, pady=(0,10), fill="x")

        tk.Button(right_frame, text="Bayar", command=self.bayar, font=("Segoe UI", 12), bg="#967bb6", fg="white").pack(pady=15, padx=10, fill="x")
        tk.Button(right_frame, text="Keluar", command=self.keluar_ke_dashboard, font=("Segoe UI", 12), bg="#967bb6", fg="white").pack(pady=5, padx=10, fill="x")

        self.toggle_uang_tunai(True)

    def toggle_uang_tunai(self, show):
        if show:
            self.uang_tunai_label.pack(padx=10, pady=(10,0), fill="x")
            self.uang_tunai_entry.pack(padx=10, pady=(0,10), fill="x")
        else:
            self.uang_tunai_label.pack_forget()
            self.uang_tunai_entry.pack_forget()
            self.uang_tunai_entry.delete(0, tk.END)

    def on_payment_method_change(self, event):
        metode = self.payment_method.get()
        self.toggle_uang_tunai(metode == "Tunai")

    def tambah_item(self):
        nama = self.selected_item.get()
        try:
            jumlah = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showwarning("Input Salah", "Masukkan jumlah yang valid.")
            return

        if nama == "Pilih Barang" or jumlah <= 0:
            messagebox.showwarning("Input Tidak Lengkap", "Silakan pilih barang dan jumlah yang valid.")
            return

        for item in self.kasir:
            if item.nama == nama:
                item.jumlah += jumlah
                self.refresh_cart()
                self.reset_input()
                return

        for item in self.menu_items:
            if item.nama == nama:
                self.kasir.append(ItemBelanja(item.nama, item.harga, jumlah))
                break

        self.refresh_cart()
        self.reset_input()

    def hapus_item(self):
        nama = self.selected_item.get()
        try:
            jumlah = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showwarning("Input Salah", "Masukkan jumlah yang valid.")
            return

        for item in self.kasir:
            if item.nama == nama:
                if jumlah > item.jumlah:
                    messagebox.showwarning("Jumlah Salah", f"Jumlah yang ingin dihapus lebih besar dari jumlah yang ada ({item.jumlah}).")
                    return
                elif jumlah == item.jumlah:
                    self.kasir.remove(item)
                else:
                    item.jumlah -= jumlah
                self.refresh_cart()
                self.reset_input()
                return

        messagebox.showwarning("Tidak Ditemukan", f"Barang '{nama}' tidak ada dalam daftar belanja.")

    def refresh_cart(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        total = 0
        for item in self.kasir:
            subtotal = item.harga * item.jumlah
            self.tree.insert('', 'end', values=(item.nama, item.jumlah, f"Rp {subtotal:,}".replace(",", ".")))
            total += subtotal

        self.tree.insert('', 'end', values=("", "", ""))
        self.tree.insert('', 'end', values=("TOTAL", "", f"Rp {total:,}".replace(",", ".")))
        self.total_label.config(text=f"Subtotal: Rp {total:,}".replace(",", "."))

    def bayar(self):
        total = sum(item.harga * item.jumlah for item in self.kasir)
        if total >= 50000:
            diskon = int(0.1 * total)
            total -= diskon
        else:
            diskon = 0

        if total == 0:
            messagebox.showinfo("Info", "Belum ada item yang dibeli.")
            return

        metode = self.payment_method.get()
        if metode == "Tunai":
            try:
                uang_bayar = int(self.uang_tunai_entry.get())
                if uang_bayar < total:
                    messagebox.showwarning("Uang Kurang", f"Uang tunai yang dibayarkan kurang dari total. Total: Rp {total}")
                    return
                kembalian = uang_bayar - total
            except ValueError:
                messagebox.showwarning("Input Salah", "Masukkan jumlah uang tunai yang valid.")
                return
        else:
            uang_bayar = 0
            kembalian = 0

        struk = f"\n{'='*40}\n          STRUK PEMBAYARAN KASIR\n{'='*40}\n"
        for item in self.kasir:
            subtotal = item.harga * item.jumlah
            struk += f"{item.nama:<20} x{item.jumlah:<3} Rp{subtotal}\n"
        if diskon:
            struk += f"\nDiskon 10%          -Rp{diskon}"
        struk += f"\n\nTotal: Rp{total}\nMetode: {metode}\n"
        if metode == "Tunai":
            struk += f"Uang Bayar: Rp{uang_bayar}\nKembalian: Rp{kembalian}\n"
        struk += f"{'='*40}\n     Terima kasih telah berbelanja!\n{'='*40}"

        self.riwayat_transaksi.append(struk)
        self.show_struk(struk)
        self.kasir.clear()
        self.refresh_cart()
        self.reset_input()
        self.toggle_uang_tunai(metode == "Tunai")

    def show_struk(self, struk):
        self.clear_root()
        tk.Label(self.root, text="Struk Pembayaran", font=("Segoe UI", 16, "bold"), bg="#f4f4f4").pack(pady=10)
        text_area = tk.Text(self.root, font=("Segoe UI", 12), height=20)
        text_area.pack(padx=20, pady=10, fill="both", expand=True)
        text_area.insert(tk.END, struk)
        text_area.config(state="disabled")
        tk.Button(self.root, text="Kembali ke Dashboard", command=self.build_dashboard, font=("Segoe UI", 12), bg="#4CAF50", fg="white").pack(pady=10)

    def keluar_ke_dashboard(self):
        self.kasir.clear()
        self.refresh_cart()
        self.reset_input()
        self.toggle_uang_tunai(False)
        self.build_dashboard()

    def reset_input(self):
        self.combobox.set("Pilih Barang")
        self.quantity_entry.delete(0, tk.END)

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = KasirApp(root)
    root.mainloop()
