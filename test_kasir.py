import unittest
from kasir import GenericList, ItemBelanja

class TestKasir(unittest.TestCase):
    def test_tambah_item(self):
        kasir = GenericList[ItemBelanja]()
        item = ItemBelanja("Indomie", 3000, 2)
        kasir.add_item(item)
        self.assertEqual(kasir.count(), 1)

    def test_subtotal(self):
        item = ItemBelanja("Aqua", 5000, 3)
        self.assertEqual(item.subtotal(), 15000)

    def test_total_harga_dan_diskon(self):
        kasir = GenericList[ItemBelanja]()
        kasir.add_item(ItemBelanja("Teh Botol", 7000, 2))  # 14.000
        kasir.add_item(ItemBelanja("Roti Tawar", 12000, 1))  # 12.000
        self.assertEqual(kasir.total_harga(), 26000)
        self.assertAlmostEqual(kasir.total_setelah_diskon(0.1), 23400)  # diskon 10%

if __name__ == '__main__':
    unittest.main()
