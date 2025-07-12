def elso_feladat():
    import random

    fogalmak = [
        'majorság', 'hűbéres', 'jobbágy', 'nemes', 'tized', 'kilenced', 'robot',
        'szügyhám', 'vetésforgó', 'ugar', 'lovag'
    ]

    meghatarozasok = [
        'Egy-egy nagybirtok vagy valamely részének igazgatási központja.',
        'Aki örökletes használatra megkapja a földet.',
        'Telkes paraszt, aki a földesúrtól kapott földön gazdálkodik.',
        'Kiváltságos réteg.',
        'Egyházi adó.',
        'Földesúrnak beszolgáltatott adó.',
        'Ötvenkét igás, vagy 104 kézimunka nap kötelezettség.',
        'Igavonási találmány, melynek köszönhetően nem az állat nyakában van a húzó eszköz.',
        'A termőföld használata évszakonként más és más.',
        'Művelés alá nem vont terület.',
        'Vagyonos katonai szolgálattevő lóval, páncéllal.'
    ]

    fogalom_dict = {fogalmak[i]: meghatarozasok[i] for i in range(len(fogalmak))}

    kerdesek = list(fogalom_dict.items())
    random.shuffle(kerdesek)

    helyes = 0
    rossz = 0

    print("=== Középkori fogalmak párosító játék ===")
    print("Írd be a fogalom nevét a meghatározás alapján!")
    print("Írj be 'END', 'Q' vagy 'QUIT' ha ki akarsz lépni.\n")

    for fogalom, meghat in kerdesek:
        print(f"\nMeghatározás:\n{meghat}")
        valasz = input("Fogalom: ").strip().lower()

        if valasz in ['end', 'q', 'quit']:
            break

        if valasz == fogalom.lower():
            print("Helyes válasz!")
            helyes += 1
        else:
            print(f"Rossz válasz. Helyesen: {fogalom}")
            rossz += 1

    ossz = helyes + rossz
    if ossz > 0:
        arany = (helyes / ossz) * 100
    else:
        arany = 0.0

    print("\nEredmények")
    print(f"Helyes válaszok: {helyes}")
    print(f"Helytelen válaszok: {rossz}")
    print(f"Pontosság: {arany:.2f}%")

elso_feladat()

def masodik_feladat():
    from collections import Counter

    data_list_string_format = """Név;Életkor;Város Németh Kamilla;19;Debrecen Fekete Géza;18;Pécs Kovács Péter;27;Budapest Kiss Tibor;20;Debrecen Szabó Erzsébet;21;Budapest Szilágyi Ede;18;Pécs Agárdi Pál;26;Budapest Pálosi Richárd;23;Budapest Budai Máté;19;Debrecen Karácsony Antal;20;Budapest Aradi Márta;27;Pécs Piros Adél;29;Debrecen Bíró Zsolt;16;Budapest Szabados Attila;25;Debrecen Román Sarolta;24;Budapest Virág Bertalan;22;Pécs Varga Imre;18;Budapest Tóth Sándor;22;Debrecen Nagy Ibolya;23;Pécs Horváth Ferenc;17;Budapest Balogh Edina;26;Budapest"""

    adatok = data_list_string_format.split(" ")
    adatok = [s for s in adatok if ";" in s]

    szemelyek = [adatok[

masodik_feladat()