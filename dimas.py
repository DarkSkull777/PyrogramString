from pyrogram import Client as c

API_ID = input("\nMasukin API_ID syg:\n > ")
API_HASH = input("\nAhhhh Crooottt Sekarang API_HASH eghmm:\n > ")

print("\n\n Ahhhh Keluarnya Banyak Bgtt, Lagi Dong Masukin Nomer Telepon Pakai Kode Negara:\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)

with i:
    ss = i.export_session_string()
    print("\nAHHHH Udah nanti aku bisa hamilll, Di atas string kamu salin aja crot!!\n")
    print(f"\n{ss}\n")