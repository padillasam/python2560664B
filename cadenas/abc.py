def alfabeto(cad):    
    cadena=''
    for i in cad:
        if i not in cadena:
            cadena+=i            
    return len(cadena)

print(alfabeto('soacha'))
        
