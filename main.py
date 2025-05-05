from kasir import GenericList, ItemBelanja
from auth import login
from config import config

# Daftar item tetap yang bisa dipilih
menu_items = [
    ItemBelanja("Indomie", 3000, 1),
    ItemBelanja("Aqua", 5000, 1),
    ItemBelanja("Teh Botol", 7000, 1),
    ItemBelanja("Roti Tawar", 12000, 1),
    ItemBelanja("Susu UHT", 8000, 1)
]

def main():
    print("=== 🛒 Aplikasi Kasir CLI ===")
    username = input("Username: ")
    password = input("Password: ")

    if not login(username, password):
        print("❌ Login gagal. Program keluar.")
        return

    print(f"✅ Selamat datang, {username}!")
    kasir = GenericList[ItemBelanja]()

    while True:
        print("\nMenu:")
        print("1. Tambah Item")
        print("2. Lihat Keranjang")
        print("3. Lihat Struk & Total")
        print("4. Hapus Item dari Keranjang")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            if kasir.count() >= config["max_items"]:
                print("⚠️ Jumlah item telah mencapai batas maksimum.")
                continue

            print("\n📋 Daftar Menu:")
            for idx, item in enumerate(menu_items, start=1):
                print(f"{idx}. {item.nama} - Rp {item.harga:,.0f}")

            # Pilih beberapa item
            try:
                item_indices = input("Pilih nomor item: ")
                selected_items = [int(i.strip()) for i in item_indices.split(",")]

                for idx in selected_items:
                    if 1 <= idx <= len(menu_items):
                        jumlah = int(input(f"Jumlah untuk {menu_items[idx - 1].nama}: "))
                        item_asli = menu_items[idx - 1]
                        item_baru = ItemBelanja(item_asli.nama, item_asli.harga, jumlah)
                        kasir.add_item(item_baru)
                        print(f"✅ Item '{item_baru.nama}' (Rp {item_baru.harga:,.0f}) x{jumlah} ditambahkan.")
                    else:
                        print(f"❌ Item nomor {idx} tidak valid.")

            except ValueError:
                print("❌ Input tidak valid.")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif pilihan == "2":
            if kasir.count() == 0:
                print("🧺 Keranjang masih kosong.")
                continue

            print("\n🧺 Isi Keranjang:")
            for i, item in enumerate(kasir.get_items(), start=1):
                print(f"{i}. {item.nama} x {item.jumlah} = Rp {item.subtotal():,.0f}")

        elif pilihan == "3":
            if kasir.count() == 0:
                print("📝 Belum ada item yang dibeli.")
                continue

            print("\n=== 🧾 Struk Belanja ===")
            for i, item in enumerate(kasir.get_items(), start=1):
                print(f"{i}. {item.nama} x {item.jumlah} @ Rp {item.harga:,.0f} = Rp {item.subtotal():,.0f}")

            total = kasir.total_harga()
            total_diskon = kasir.total_setelah_diskon(config["discount_rate"])
            print(f"\nTotal: Rp {total:,.0f}")
            print(f"Diskon ({config['discount_rate']*100}%): Rp {total - total_diskon:,.0f}")
            print(f"Total Bayar: Rp {total_diskon:,.0f}")

        elif pilihan == "4":
            if kasir.count() == 0:
                print("🧺 Keranjang masih kosong.")
                continue

            print("\n🗑 Hapus Item dari Keranjang:")
            for i, item in enumerate(kasir.get_items(), start=1):
                print(f"{i}. {item.nama} x {item.jumlah} = Rp {item.subtotal():,.0f}")

            try:
                hapus = int(input("Masukkan nomor item yang ingin dihapus: "))
                if 1 <= hapus <= kasir.count():
                    item_to_delete = kasir.get_items()[hapus - 1]
                    print(f"🛒 Anda memilih untuk hapus: {item_to_delete.nama} x {item_to_delete.jumlah}")
                    
                    # Tanya user berapa jumlah yang ingin dihapus
                    jumlah_hapus = int(input(f"Berapa banyak {item_to_delete.nama} yang ingin dihapus? (max {item_to_delete.jumlah}): "))
                    if 1 <= jumlah_hapus <= item_to_delete.jumlah:
                        item_to_delete.jumlah -= jumlah_hapus
                        if item_to_delete.jumlah == 0:
                            kasir.get_items().remove(item_to_delete)
                        print(f"✅ {jumlah_hapus} pcs {item_to_delete.nama} telah dihapus.")
                    else:
                        print(f"❌ Jumlah yang ingin dihapus tidak valid.")
                else:
                    print("❌ Nomor item tidak valid.")
            except ValueError:
                print("❌ Input tidak valid.")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif pilihan == "5":
            print("👋 Terima kasih telah menggunakan kasir CLI!")
            break

        else:
            print("❌ Pilihan tidak valid.")

if __name__ == "__main__":
    main()
