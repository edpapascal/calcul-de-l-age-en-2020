# fonction lambda
import boucle
user_year = lambda birth_day: 2020-birth_day

birth_year = int(input("entrez votre date de naissance"))

print(user_year(birth_year))

boucle.condition(user_year(birth_year))
