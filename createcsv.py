import csv

def adresswriter(name,email):
    with open('data.csv', 'a+') as csvfile:
        
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([name, email])

x=0
while 1==1:
    em=input('enter email address: ')
    nm=input('enter name/name: ')
    adresswriter(nm,em)
    x=x+1
    print('No of entries={number}'.format(number=x))
    
