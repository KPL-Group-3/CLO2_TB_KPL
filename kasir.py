from typing import Generic, TypeVar, List
from config import get_config

config = get_config()

T = TypeVar('T')

class GenericList(Generic[T]):
    """
    Struktur data generik untuk menampung item belanja.
    """
    def __init__(self):
        self.items: List[T] = []

    def add_item(self, item: T):
        assert item is not None, "Item tidak boleh kosong"  # secure coding
        if len(self.items) >= config["max_items"]:
            raise Exception("📦 Jumlah item melebihi batas maksimum")  # secure coding
        self.items.append(item)

    def get_items(self) -> List[T]:
        return self.items.copy()

    def count(self) -> int:
        return len(self.items)

    def total_harga(self) -> float:
        return sum(item.subtotal() for item in self.items)

    def total_setelah_diskon(self, diskon_rate: float) -> float:
        return self.total_harga() * (1 - diskon_rate)

class ItemBelanja:
    def __init__(self, nama: str, harga: float, jumlah: int):
        assert nama, "Nama item tidak boleh kosong"  
        assert harga >= 0, "Harga harus >= 0"  
        assert jumlah > 0, "Jumlah harus > 0"  
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

        if len(self.items) >= config["max_otems"]:
            raise Exception("Jumlah item melebihi batas maksimum")

    def subtotal(self) -> float:
        return self.harga * self.jumlah