a = 10
b = 2

if a > b:
    print("a jest wieksze od b")
elif a < b:
    print("a jest mniejsze od b")
else:
    print("a jest rowne b")

#warunek jednoliniowy
print("a i b są równe") if a == b else print("a i b są różne")\

#warunek z łącznikem and gdy oba są prawdziwe
if b >= 5 and a <= 10:
    print("b jest wieksze lub rowne 5 i a jest mniejsze lub rowne 10")

#warunek z łącznikem or gdy jeden jest prawdziwy to wyświetli się komunikat
if a != 10 or b > 3:
    print("a nie jest rowne od 10 lub b jest wieksze od 3")



# warunek z argumentem pass uzywamy gdy deklarujemy warunek ale nie chcemy nic z nim robic
if b > a:
    pass

fruits = ["jabłko", "pomarancza", "śliwka"]

if "jabłko" in fruits:
    print("Jabłko jest w liście owoców")

car = {
    "producent": "Toyota",
    "model": "supra",
}

if "model" in car:
    print("Model jest w słowniku samochodów")
    if car ["model"] == "supra":
        print("Model to supra") fc