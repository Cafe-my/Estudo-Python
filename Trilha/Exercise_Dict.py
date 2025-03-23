#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up

#create stores
freelancers = {'name':'Freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

# cart = {}
# def compras(loja):
#     item_comprado = input(f'Seja bem vindo a {loja.pop('name')}! Temos: {loja}! O que gostaria de levar? ').lower()
#     cart.update({item_comprado:loja.pop(item_comprado)})
    
# compras(freelancers)
# compras(antiques)
# compras(pet_shop)

# print(f'Voce comprou {cart.keys()}! Hoje todos os itens estao de graca, um bom dia')


#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
# cart = {}
# purse = 1000
# # loop pelas lojas/dicio
# for shop in (freelancers,antiques,pet_shop) :
#     buy_item = input(f'Welcome to {shop.pop('name')}! What do you want to buy: {shop}? Type exit if you do not want to buy. ').lower()
#     # sair da loja caso escrever algo diferente de um item
#     if buy_item not in shop:
#         continue
#     # Atualizando o carrinho de compras
#     cart.update({buy_item:shop.pop(buy_item)})
# # Realizando a conta do total das compras e do que sobrou a partir do 'cart'
# t_price = 0
# for price in cart.values():
#     purse -= price
#     t_price += price
    
# print(f'You Purchased: {', '.join(list(cart.keys()))}. You spent {t_price} golds and left {purse} golds in your purse!')


#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'
#inventario pela manha
department_store = {**freelancers, **antiques, **pet_shop}
print(sorted(department_store.items()))
print(100*'-')
cart = {}
purse = 1000
# loop pelas lojas/dicio
for shop in (freelancers,antiques,pet_shop) :
    buy_item = input(f'Welcome to {shop.pop('name')}! What do you want to buy: {shop}? Type exit if you do not want to buy. ').lower()
    # sair da loja caso escrever algo diferente de um item
    if buy_item not in shop:
        continue
    # Atualizando o carrinho de compras
    cart.update({buy_item:shop.pop(buy_item)})
    # Realizando a conta do total das compras e do que sobrou a partir do 'cart'
    t_price = sum(cart.values())
    
print(f'You Purchased: {', '.join(list(cart.keys()))}. You spent {t_price} golds and have left {purse - t_price} golds in your purse!')

#inventario no fim do dia
print(100*'-')
department_store_after = {**freelancers, **antiques, **pet_shop}
print(sorted(department_store_after.items()))