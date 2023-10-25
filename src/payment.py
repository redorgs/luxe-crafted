from db.db import DB
import os

class payment:
    def __totalprice(self):
        return self.__price*self.__totalproduct

    def detailproduk(self, id):
        detail = DB('product')._get()[0]
        print(f"produk: {detail[1]}")
        print(f"harga: {detail[3]}")
        print(f"unit: 3")
        print(f"total belanja: 234")

    def pilihanpembayaran(self):
        print("\nSilahkan pilih metode pembayaran anda")
        print("1) Virtual account BCA")
        print("2) Virtual account BRI")
        print("3) Account GOJEK")
        print("4) Account DANA")

        user = input("\nPilih metode anda :   ")
        os.system("clear")

        iscorrect = False
        if user == "1":
            text="Berikut Nomor Pembayaran VA BCA 222232344434234"
        elif user == "2":
            text="Berikut Nomor Pembayaran VA BRI 222232344434234"
        elif user == "3":
            text="Berikut Nomor Pembayaran via GOJEK 222232344434234"
        elif user== "4":
            text="Berikut Nomor Pembayaran via DANA 222232344434234"

        else:
            iscorrect = True


        if iscorrect:
            print("Inputan anda salah")

        #Menampilkan hasil akhir
        else:
            paymentz.detailproduk(1)
            print(text)

            print("\n-------------Silahkan kirim ke nomor yang tertera-------------\n")

paymentz=payment()


paymentz.detailproduk(1)
paymentz.pilihanpembayaran()

