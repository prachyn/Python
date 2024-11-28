from datetime import datetime, timedelta

print(datetime.now())
dnesni_poledne = datetime(2024, 11, 7, 12)
print(dnesni_poledne)

blanka_narozky = datetime(1982, 5, 23)
print(f"Blanka se narodila {blanka_narozky.isoweekday()}. den v tydnu")

aktualni = datetime.now()
print(aktualni.strftime("%d. %b %Y, %H:%M"))

apollo_start = datetime(1969, 7, 16, 14, 32)
apollo_pristani = datetime.fromisoformat("1969-07-21T18:54:00")
apollo_pristani = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M")
delka_mise = apollo_pristani - apollo_start
print(delka_mise)

planovany_prijezd = datetime(2024, 3, 13, 19, 59)
zpozdeni = timedelta(minutes=10, seconds=25)
skutecny_prijezd = planovany_prijezd + zpozdeni
print(f"Vlak prijede az v {skutecny_prijezd}")

# Ukoly
# 1
print(f"Americky cas startu Apolla {apollo_start.strftime("%m/%d/%Y")}")
solarorbiter_start = datetime(2020, 2, 10, 5, 3)
print(f"Den v tydnu startu Solar Orbiter: {solarorbiter_start.isoweekday()}")
od_startu = aktualni - solarorbiter_start
print(f"Od startu Solar Orbiter uplynulo {od_startu}")


objednavka = datetime(2020, 11, 13, 19, 47)
prevzeti = timedelta(minutes=8, seconds=35)
priprava = timedelta(minutes=30)
doprava = timedelta(minutes=25, seconds=30)
kdy_dostanu = objednavka + prevzeti + priprava + doprava
print(f"Objednavku z {objednavka} dostanu {kdy_dostanu}")
