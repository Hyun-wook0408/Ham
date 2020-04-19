import random

colors = ['Red', 'Blue', 'Black']
clothes = ['Dress', 'Skirt', 'Pants']
results = random.choices(colors, k=1)
Another = random.choices(clothes, k=1)
print(results, Another)