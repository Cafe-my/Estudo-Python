movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]

year =[1971,1975,1979,1982,1983,2014]

names = ['John','Eric','Michael','Graham','Terry','TerryG']

# DICT COM FOR LOOP
new_dict = dict()
for movie, yr in zip(movies,year):
    new_dict[movie] = yr
print(new_dict)
    # fica: {'And Now for Something Completely Different': 1971, 'Monty Python and the Holy Grail': 1975, "Monty Python's Life of Brian": 1979, 'Monty Python Live at the Hollywood Bowl': 1982, "Monty Python's The Meaning of Life": 1983, 'Monty Python Live (Mostly)': 2014}

# DICT COM COMPREHENSION
new_dict = {movie:yr for movie,yr in zip(movies,year)}
print(new_dict)
    # fica: {'And Now for Something Completely Different': 1971, 'Monty Python and the Holy Grail': 1975, "Monty Python's Life of Brian": 1979, 'Monty Python Live at the Hollywood Bowl': 1982, "Monty Python's The Meaning of Life": 1983, 'Monty Python Live (Mostly)': 2014}

# COM CONDICOES
new_dict = {movie:yr for movie,yr in zip(movies,year) if yr < 1983 and movie.startswith('Monty')}
print(new_dict)
    # fica: {'Monty Python and the Holy Grail': 1975, "Monty Python's Life of Brian": 1979, 'Monty Python Live at the Hollywood Bowl': 1982}

# Formatando 
n1 =[[f"{name}'s favorite movie was {movie} from {str(yr)}"] for name,movie,yr in zip(names,movies,year) if yr < 1981 ]
print(n1)
    # fica: [["John's favorite movie was And Now for Something Completely Different from 1971"], ["Eric's favorite movie was Monty Python and the Holy Grail from 1975"], ["Michael's favorite movie was Monty Python's Life of Brian from 1979"]]