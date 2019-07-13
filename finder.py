from steem import Steem
from steem.account import Account
import csv

atlas = ['BRASIL', 'BRAZIL']
ac = Account('lpessin')
s = Steem()
all = []
with open('all', mode='r') as inall:
    leitor = csv.reader(inall)
    for linha in leitor:
        l = linha[0]
        all.append(l)


for br in all:
    ac = Account(br)
    #print(ac.name, ac.profile.get('location'))
    local = str(ac.profile).upper()
    for a in atlas:
        if a in local:
            print(ac.name, ac.profile.get('location'))
