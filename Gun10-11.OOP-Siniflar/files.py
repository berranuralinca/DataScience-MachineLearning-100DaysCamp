my_file = open("Gun10-11.OOP-Siniflar\\test.txt")
type(my_file)
text = my_file.read()
print(text)
my_file.close()


with open("Gun10-11.OOP-Siniflar\\deneme.txt", "w", encoding="utf-8") as f:
    f.write("Merhaba Dunya!\n")


with open("Gun10-11.OOP-Siniflar\\deneme.txt", "a", encoding="utf-8") as f:
    f.write("Bu satir en sona eklendi.\n")

my_new = open("Gun10-11.OOP-Siniflar\\deneme.txt")
text = my_new.read()
print(text)
my_new.close()