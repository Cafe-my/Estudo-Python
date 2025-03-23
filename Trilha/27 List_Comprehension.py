# aquilo que fazemos com comprehension podemos fazer com for loop


numbers = [1,2,3,4,5,6,7,8,9]

# FOR LOOP
new_list = []
for num in numbers:
    new_list.append(num*num)
    # fica: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# LIST COMPREHENSION
new_list = [num*num for num in numbers]     # (num*num) = faca isso / (for num in numbers) = para esse iteravel 
    # fica: [1, 4, 9, 16, 25, 36, 49, 64, 81]


# sintaxe basica/exemplo
new_list = [num for num in numbers if num % 2 == 0]
# [(Do this) (for this collection/iterable) (with this condition)]
# (num)         (for num in numbers)            (if num % 2 == 0)
    # fica: [2, 4, 6, 8]

# Outra forma de obter o mesmo resultado
new_list = filter(lambda num: num % 2 ==0,numbers)
    # fica: [2, 4, 6, 8]


# FOR LOOP
new_list = []
for letter in 'spam':
   for num in range(4):
       new_list.append((letter,num))
    # fica: [('s', 0), ('s', 1), ('s', 2), ('s', 3), ('p', 0), ('p', 1), ('p', 2), ('p', 3), ('a', 0), ('a', 1), ('a', 2), ('a', 3), ('m', 0), ('m', 1), ('m', 2), ('m', 3)]
   
# LIST COMPREHENSION
new_list = [(letter,num) for letter in'spam' for num in range(4)]
    # fica: [('s', 0), ('s', 1), ('s', 2), ('s', 3), ('p', 0), ('p', 1), ('p', 2), ('p', 3), ('a', 0), ('a', 1), ('a', 2), ('a', 3), ('m', 0), ('m', 1), ('m', 2), ('m', 3)]
