import csv 
header=['Fruit','Price']
rows=[['Apple',1200],
      ['Berry',2000],
      ['Lemon',1000],
      ['Melon',3000],
      ['Grapes',4000],
      ['Pear',2000]]

with open ('archivos/example.csv','w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)