try:
    x = int(input("Sayi giriniz: "))
except ValueError:
    print("Sayi olmali")
finally:
    print("Program bitti.")
