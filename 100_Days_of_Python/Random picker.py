# Random picker
import random
#create list of names of the subect
subject = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8', 'name9', 'name10']
# pick random samples from subect list, designating how many
pick_1 = random.sample(subject, 2)
print(f'The two picked are {pick_1}')