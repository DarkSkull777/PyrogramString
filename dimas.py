from pyrogram import Client as c

API_ID = input("\nMasukin API_ID syg:\n > ")
API_HASH = input("\nAhhhh Crooottt Sekarang API_HASH eghmm:\n > ")

print("\n\n Dimas Gantengg\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)

with i:
    ss = i.export_session_string()
    print("\nAHHHH CROTT!! String Kamu Ada Di Bawah Salin Aja.\n")
    print(f"\n{ss}\n")