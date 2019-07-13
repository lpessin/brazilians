from steem import Steem
from steem.account import Account
import csv
import openpyxl as op
atlas = ['BRASIL', 'BRAZIL']
ac = Account('lpessin')
s = Steem()
all = []
with open('all', mode='r') as inall:
    leitor = csv.reader(inall)
    for linha in leitor:
        l = linha[0]
        all.append(l)
p = ac.profile.get('location').upper()
print(p)


wb = op.load_workbook('br.xlsx')
ws = wb['Sheet1']
ws2 = wb['Sheet2']
c = 0
for br in all:
    ac = Account(br)
    c += 1
    if c <= 500000:
        ws.append([ac.name, ac.profile.get('location')])
    else:
        print('metade!!')
        ws2.append([ac.name, ac.profile.get('location')])
 
wb.save('br.xlsx')
wb.close()
