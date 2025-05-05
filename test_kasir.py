import unittest
from kasir import GenericList, ItemBelanja

class TestKasir(unittest.TestCase):
    def test_tambah_item(self):
        kasir = GenericList[ItemBelanja]()
        item = ItemBelanja("Batik", 100000, 2)
        kasir.add_item(item)
        self.assertEqual(kasir.count(), 1)

    def test_subtotal(self):
        item = ItemBelanja("Kemeja", 75000, 3)
        self.assertEqual(item.subtotal(), 225000)

    def test_total_harga_dan_diskon(self):
        kasir = GenericList[ItemBelanja]()
        kasir.add_item(ItemBelanja("Sepatu", 200000, 1))
        kasir.add_item(ItemBelanja("Kaos", 100000, 2))
        self.assertEqual(kasir.total_harga(), 400000)
        self.assertAlmostEqual(kasir.total_setelah_diskon(0.1), 360000)

if __name__ == '__main__':
    unittest.main()
