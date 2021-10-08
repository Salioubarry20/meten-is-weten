print('Hallo, we gaan een spel spelen waardoor je gratis een Iphone 13 kan winnen :)')
print('Eerst moet je 90% van de vragen goed hebben anders helaas. ')
vraag = input('Ben je er klaarvoor om te beginnen?: ')
if vraag == 'ja':
    vraag1 = int(input('In welke jaar kwam de eerste Iphone uit?: '))
else:
    print('U kunt altijd terug komen als u er klaar voor bent. ')      

if vraag1 == 2009: 
    print('Gefeliciteerd, U hebt de Iphone 13 GEWONNEN ')
else:
    print('Helaas waren er geen genoeg antwoorden goed. ')    