print("Vítejte v evidenci účastníků pojištění.\nZvolte požadovanou akci:\n\t"
      "1 = přidání pojištěnce\n\t2 = výpis pojištěnců\n\t3 = vyhledání pojištěnce\n\t4 = ukončení aplikace")

from pojistenec import Pojistenec
# vytvoření pole
pojistenci = []

vstup = 0

while vstup != 4:
    try:
        vstup = int(input("Zadejte zvolené číslo akce: "))

        # vytvoření pojištěného
        if vstup == 1:
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            vek = input("Zadejte věk: ")
            telefon = input("Zadejte telefon: ")
            pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
            print(pojistenec)
            pojistenci.append(pojistenec)
            print("Přidali jste úspěšně nového pojištěnce do databáze.")

        # výpis pojištěnců
        elif vstup == 2:
            print("Toto je seznam všech aktuálních pojištěnců:")
            for pojistenec in pojistenci:
                print(pojistenec)

        # vyhledávání pojištěnců
        elif vstup == 3:
            pojistenec_nalezen = "nenalezen"
            hledane_jmeno = input("Zadejte hledané jméno: ")
            hledane_prijmeni = input("Zadejte hledané příjmení: ")
            for pojistenec in pojistenci:
                if hledane_jmeno == pojistenec.jmeno and hledane_prijmeni == pojistenec.prijmeni:
                    pojistenec_nalezen = pojistenec
            print(f"Hledaný pojištěnec je {pojistenec_nalezen}.")

        # ukončení aplikace
        elif vstup == 4:
            print("Děkujeme za použití naší aplikace.")

        # nesprávná hodnota
        else:
            print("Zadejte platnou hodnotu.")

    # ošetření výjimky
    except ValueError:
        print("Zadejte pouze platnou číselnou hodnotu.")