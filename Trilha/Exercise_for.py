names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
names.extend(names1)

# Adicionando convidados a lista
while True:
    add = input("Do you want to invite more friends? Yes or No: ").upper()
    if add == 'YES':
        names.append(input("Who? "))
    elif add == 'NO':
        break

# Repeticao para convites
for guest in names:
    print(f'{guest.title()}! You are invited to the party Saturday!')