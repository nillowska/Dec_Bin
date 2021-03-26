print("Witaj w programie zamieniającym wartości liczbowe.")
choice = int(input("Wybierz sposób zamiany liczby. Jeśli chcesz zamienić na kod binarny wybierz 1, jeśli na dziesiętny wybierz 2: "))

if choice == 1:
    isDec = int(input("Wybrałeś zamianę dec->bin. Podaj wartość, która jest mniejsza od 15: "))
    if isDec <= 15:
        valueBin = bin(isDec)[2:8]
        print("Wartość została zamieniona i wynosi: " +valueBin)
    else:
        print("Wartość musi być mniejsza niż 15!")
elif choice == 2:
    isBin = str(input("Wybrałeś zamianę bin->dec. Podaj wartość, która jest mniejsza od 15: "))
    valueDec = int(isBin, 2)
    print("Wartość została zamieniona i wynosi: ",valueDec)
else:
    print("Wybrałeś niepoprawne działanie.")
    
input()
