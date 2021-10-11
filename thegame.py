print('Hallo, we gaan een spel spelen waardoor je gratis een Iphone 13, een PS5, een Lenovo laptop, een fiets of een FIFA 22 kan winnen :)')
print('Als je minder dan 60% van alle vragen fout hebt dan win je niks. ')
score = 0

vraag = int(input('1- In welke jaar kwam de eerste Iphone uit?: '))
if vraag == 2009:
    score += 10
vraag = int(input('2- Wat is de pixeldichtheid van de Iphone 13 per inch?: '))
if vraag == 460:
    score += 10
vraag = int(input('3- In welke jaar werd de Playstation voor het eerst in Europa verkocht?: '))
if vraag == 1995:
    score += 10
vraag = int(input('4- In welke jaar werd de Playstation 3 uitgebracht?: '))
if vraag == 2006:
    score += 10
vraag = int(input('5- In welke jaar werd de lenovo geïntroduceerd?: '))
if vraag == 2004:
    score += 10
vraag = str(input('6- In welke land fietsen ze het meest?: '))
if vraag == 'Nederland':
    score += 10
vraag = str(input('7- Wie is de uitvinder van Apple?: '))
if vraag == 'Los Altos':
    score += 10
vraag = int(input('8- Hoe lang bestaat de serie FIFA?: '))
if vraag == 28:
    score += 10
vraag = int(input('9- In welke jaar is FIFA opgericht?: '))
if vraag == 1904:
    score += 10
vraag = int(input('10- Hoeveel Europese landen hebben FIFA opgericht?: '))    
if vraag == 7:
    score += 10

if score == 100:   
    print('Gefeliciteerd, U hebt de Iphone 13 GEWONNEN ')
elif score == 90:
    print('Gefeliciteerd, U hebt de PS5 GEWONNEN ')    
elif score == 80:
    print('Gefeliciteerd, U hebt een Lenovo laptop GEWONNEN ')
elif score == 70:
    print('Gefeliciteerd, U hebt een fiets GEWONNEN ')          
elif score == 60:
    print('Gefeliciteerd, U hebt de FIFA 22 GEWONNEN ')  
else:
    print('Helaas waren er geen genoeg antwoorden goed. ')    
    