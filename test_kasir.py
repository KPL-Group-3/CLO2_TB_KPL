# test_kasir.py
import unittest
from kasir import GenericList, ItemBelanja

class TestKasir(unittest.TestCase):
    def setUp(self):
        self.kasir = GenericList[ItemBelanja]()
        self.item1 = ItemBelanja("Teh Botol", 5000, 2)
        self.item2 = ItemBelanja("Aqua", 3000, 1)

    def test_add_item(self):
        self.kasir.add_item(self.item1)
        self.assertEqual(self.kasir.count(), 1)

    def test_total_harga(self):
        self.kasir.add_item(self.item1)
        self.kasir.add_item(self.item2)
        total = self.kasir.total_harga()
        self.assertEqual(total, 5000 * 2 + 3000)

    def test_total_diskon(self):
        self.kasir.add_item(self.item1)
        total_setelah_diskon = self.kasir.total_setelah_diskon(0.1)
        self.assertEqual(total_setelah_diskon, 10000 * 0.9)

    def test_get_items(self):
        self.kasir.add_item(self.item2)
        items = self.kasir.get_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].nama, "Aqua")

if __name__ == "__main__":
    unittest.main()
