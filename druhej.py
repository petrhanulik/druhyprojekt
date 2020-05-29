import random
import time

def hlavni():
    cisla = uvod()
    pocet_hadani = 0
    hadane_cislo = hadej_cislo()
    s = time.time()
    bulls, cows = over_cislo(hadane_cislo, cisla)


    while bulls != 4:
        pocet_hadani += 1
        hadane_cislo = hadej_cislo()
        bulls, cows = over_cislo(hadane_cislo, cisla)
        print(ohodnoceni_hry(bulls, cows, pocet_hadani))

    print(ohodnoceni(pocet_hadani))
    e = time.time()
    v = round(e - s, 2)
    print(f"cislo jsi uhadl za  {v} sekund")

def uvod():
    print("""             ahoj!
             vygeneroval jsem 4 nahodna cisla...
             pojd hrat hru BULLS and COWS!"""
          )
    list1 = [1,2,3]
    list2 = [0,4,5]
    list3 = [6,7]
    list4 = [8,9]
    return str(random.choice(list1)) + str(random.choice(list2)) + str(random.choice(list3)) + str(random.choice(list4))


def hadej_cislo():
    cislo = input(f"hadej ctyrciselne cislo: ")
    if len(cislo) == 4:
        return cislo
    else:
        print("ZADAL JSI SPATNE CISLO, NASTALA CHYBA")


def over_cislo(hadane_c, v_cislech):
    cows = 0
    bulls = 0
    for index, cis in enumerate(v_cislech):
        if v_cislech[index] == hadane_c[index]:
            bulls += 1
        elif cis in hadane_c:
            cows += 1
    return bulls, cows


def ohodnoceni_hry(bulls, cows, suma_hadani):
    if bulls == 1 and cows == 1:
        return f"BULL: {bulls}, COW: {cows}"
    elif bulls == 1:
        return f"BULL: {bulls}, COWS: {cows}"
    elif cows == 1:
        return f"BULLS: {bulls}, COW: {cows}"
    elif bulls == 4:
        return f"SKVELE! cislo jsi uhadnul na {suma_hadani}. pokus."

    else:
        return f"BULLS: {bulls}, COWS: {cows}"


def ohodnoceni(hadani):
    if hadani < 10:
        print("BRAVO!")
    if 10 < hadani < 20:
        print("JDE TO!")
    if 20 < hadani < 10000:
        print("NIC MOC!")



hlavni()



