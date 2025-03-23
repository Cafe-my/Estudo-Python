sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

sunday = sales_w2.append(int(input('How many lemonades did we sell today? ')))
sales.extend(sales_w1)              # outra forma de somar listas seria: sales = sales_w1 + sales_w2
sales.extend(sales_w2)              

profit_bd = max(sales) * 1.5
profit_wd = min(sales) * 1.5
profit_total = sum(sales) * 1.5

print(f'On the best day, I earned: {profit_bd} dollars')
print(f'On the worst day, I earned: {profit_wd} dollars')
print(f'In total, I earned: {profit_total} dollars')


