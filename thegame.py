print('Hallo, we gaan een spel spelen waardoor je gratis een Iphone 13, een PS5, een Lenovo laptop, een fiets of een FIFA 22 kan winnen :)')
print('Als je minder dan 50% van alle vragen fout hebt dan win je niks. ')
vraag = str(input('Ben je er klaarvoor om te beginnen?: '))
if vraag == 'ja':
    vraag1 = int(input('1- In welke jaar kwam de eerste Iphone uit?: '))
    vraag2 = int(input('2- Wat is de pixeldichtheid van de Iphone 13 per inch?: '))
    vraag3 = int(input('3- In welke jaar werd de Playstation voor het eerst in Europa verkocht?: '))
    vraag4 = int(input('4- In welke jaar werd de Playstation 3 uitgebracht?: '))
    vraag5 = int(input('5- In welke jaar werd de lenovo geïntroduceerd?: '))
    vraag6 = str(input('6- In welke land fietsen ze het meest?: '))
    vraag7 = str(input('7- Wie is de uitvinder van Apple?: '))
    vraag8 = int(input('8- Hoe lang bestaat de serie FIFA?: '))
    vraag9 = int(input('9- In welke jaar is FIFA opgericht?: '))
    vraag10 = int(input('10- Hoeveel Europese landen hebben FIFA opgericht?: '))

else:
    print('U kunt altijd terug komen als u er klaar voor bent. ')      

if vraag1 == 2009 and vraag2 == 460 and vraag3 == 1995 and vraag4 == 2006 and vraag5 == 2004 and vraag6 == 'Nederland' and vraag7 == 'Los Altos' and vraag8 == 28 and vraag9 == 1904 and vraag10 == 7:
    if 90% True:    
        print('Gefeliciteerd, U hebt de Iphone 13 GEWONNEN ')
    if 80% True:
        print('Gefeliciteerd, U hebt de PS5 GEWONNEN ')    
    if 70% True:
        print('Gefeliciteerd, U hebt een Lenovo laptop GEWONNEN ')
    if 60% True:
        print('Gefeliciteerd, U hebt een fiets GEWONNEN ')          
    if  50% True:
        print('Gefeliciteerd, U hebt de FIFA 22 GEWONNEN ')     
    
else:
    print('Helaas waren er geen genoeg antwoorden goed. ')   
    