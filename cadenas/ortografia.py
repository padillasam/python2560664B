def ortografica(c):
    if c[-1]=='á'or c[-1]=='é'or c[-1]=='ó'or c[-1]=='í'or c[-1]=='ú':
        print('Aguda')
    else:
        print('No necesariamente es aguda')

ortografica('árbol')

