
score = 0
vraag10snor = 0
vraag10krulhaar = 0
vraag1 = input('Wat is uw naam?: ')
vraag2 = input('In welke stad woont u?: ')
vraag3 = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?: '))
vraag4 = int(input('Hoeveel jaar ervaring heeft u met jongleren?: '))
vraag5 = int(input('Hoeveel jaar praktijkervaring heeft u met acrobatiek?: '))
vraag6 = input('Bent u sportief? (y/n): ')
vraag7 = (input('Bent u in bezit van een Diploma MBO-4 ondernemen? (y/n): '))
if vraag7 == 'y':
    score += 1
vraag8 = input('Bent u in bezit van een geldig Vrachtwagen rijbewijs? (y/n): ')
if vraag8 == 'y':
    score += 1
vraag9 = input('Bent u in bezit van een hoge hoed? (y/n): ')
if vraag9 == 'y':
    score += 1
vraag10 = input('Bent u een man/vrouw?: ')
if vraag10 == "man":
    vraag10snor = int(input('wat is uw snorlengte: '))
    score += 1
if vraag10 == "vrouw":
    vraag10krulhaar = int(input('wat is uw krulhaarlengte: '))
    score += 1
vraag11 = int(input('Hoeveel cm bent u?: '))
vraag12 = int(input('Hoe zwaar bent u?: '))
vraag13 = input('Hoe vaak eet u per dag?: ')
vraag14 = str(input('Heeft u een Certificaat van "Overleven met gevaarlijk personeel"? (y/n): '))
vraag15 = input('Hoeveel Certificaten heeft u in totaal?: ')

if score >= 4 and (vraag3 > 4 or vraag4 > 5 or vraag5 > 3) and (vraag10snor > 10 or vraag10krulhaar > 20) and vraag11 > 150 and vraag12 > 90 and vraag14 == 'y':
    print('U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV.')
else:
    print('U voldoet niet aan onze strenge eisen voor deze functie, het spijt ons.')
