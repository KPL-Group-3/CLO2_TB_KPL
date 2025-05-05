import time
from kasir import GenericList, ItemBelanja

kasir = GenericList[ItemBelanja]()
start = time.time()

for i in range(10000):
    kasir.add_item(ItemBelanja(f"Item-{i}", 1000, 1))

end = time.time()
print(f"⏱ Waktu untuk tambah 10.000 item: {end - start:.4f} detik")
