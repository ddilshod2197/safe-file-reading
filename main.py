def xavfsiz_fayl_oqing(fayl_nomi):
    try:
        with open(fayl_nomi, 'r') as fayl:
            matn = fayl.read()
            print(matn)
    except FileNotFoundError:
        print(f"Fayl {fayl_nomi} topilmadi.")
    except PermissionError:
        print(f"Fayl {fayl_nomi} uchun ruxsat yo'q.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
    finally:
        print("Fayl o'qish tugallandi.")

xavfsiz_fayl_oqing("fayl.txt")
