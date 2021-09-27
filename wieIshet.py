Question = input('is de kaas geel?: ')

if  Question == "yes":  
    Question1 = input('zitten er gaten in?: ')   
    if  Question1 == "yes":
        Question2 = input('is de kaas belachelijk duur?: ')
        if Question2 == 'yes':
            print('Emmenthaler is het duurste')
        if Question2 == 'noo':
            print('Leerdammer goedkoopste')    
    else:    
        Question3 = input('Is de kaas hard als steen?: ' )
        if  Question3 == "yes":
            print('De pamingo reggino')  
        if Question3 == "noo":
            print('Het is de goudste kaas')     

else:
    Question4 = input('heeft de kaas blauwe schimmels?: ') 
    if  Question4 == "yes":
        Question5 = input('Heeft de kaas een korst?: ')
        if  Question5 == "yes":    
            print('Blue de Rochbaron')
        else: 
            print('Fourme d Abert')     
    
    else:
        Question6 = input('Heeft de kaas een korst?: ')
        if  Question6 == "yes":
            print('Camembert')
        else:    
            print('Mozarella')