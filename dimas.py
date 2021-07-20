from pyrogram import Client as c

API_ID = input("\nMasukin API_ID kamu sayang:\n > ")

API_HASH = input("\nMasukin API_HASH kamu by:\n > ")

print("\n\n Masukin Nomer Telepon Kamu Jangan Lupa Pake Kode Negara Seperti +62.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)

with i:
    ss = i.export_session_string()

    print("\nSTRING SESSION KAMU BERHASIL DI BUAT, SALIN AJA TUH DIATAS!!\n")

    print(f"\n{ss}\n")