from db.db import DB
import os

class payment:
    def detailproduk(self, id):
        detail = DB('product')._get()[0]
        print(f"produk: {detail[1]}")
        print(f"harga: {detail[3]}")
        print(f"unit: 3")
        print(f"total belanja: 234")

    def __totalprice(self):
        return self.__price*self.__totalproduct

    def pilihanpembayaran(self):
        print("\nSilahkan pilih metode pembayaran anda")
        method = DB('payment')._get()
        for method in method:
            print(f"{method[0]}) {method[1]}")

        user = input("\nPilih metode anda :   ")
        os.system("clear")

        pilihan = DB('payment')._where('id', user)._get()

        if pilihan:
            self.detailproduk(1)
            print(f"Berikut Nomor Pembayaran VA {pilihan[0][1]} {pilihan[0][2]}")
            print("\n-------------Silahkan kirim ke nomor yang tertera-------------\n")
        else:
            print('Pilihan anda salah')

paymentz=payment()


paymentz.detailproduk(1)
paymentz.pilihanpembayaran()

