# ns funties bereken ding
# Esper

def standaardprijs(afstandKM):
    if afstandKM <0:
        afstandKM = 0
        
    if afstandKM <=50:
        pre_euro_prijs = afstandKM * 0.8
    else:
        pre_euro_prijs = 15 + afstandKM * 0.6
    return pre_euro_prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    pre_euro_prijs = standaardprijs(afstandKM)
    if leeftijd <12 or leeftijd >=65:
        if weekendrit == True:
            prijs = pre_euro_prijs * 0.65
        else:
            prijs = pre_euro_prijs * 0.70
    else:
        if weekendrit == True:
            prijs = pre_euro_prijs * 0.60
        else:
            prijs = pre_euro_prijs
    return prijs

while True:
    afstandKM = input("Wat is de afstand in kilometers? \n > ")
    try:
        afstandKM = float(afstandKM)
        break
    except:
        print(f"{afstandKM} is geen geldige waarde!")
        continue

while True:
    leeftijd = input("Wat is je leeftijd in jaren? \n > ")
    try:
        leeftijd = int(leeftijd)
        break
    except:
        print(f"{leeftijd} is geen geldige waarde!")
        continue

while True:
    antwoord = input("Reis je in het weekend? 1 voor ja, 2 voor nee \n > ")
    if antwoord == "1":
        weekendrit = True
        break
    elif antwoord == "2":
        weekendrit = False
        break
    else:
        print(f"{antwoord} is geen geldig antwoord!")
        continue

print(ritprijs(leeftijd,weekendrit,afstandKM))