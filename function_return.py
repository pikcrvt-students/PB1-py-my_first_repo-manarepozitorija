def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

skaitlis1 = int(input("ievadi pirmo skaitli "))
skaitlis2 = int(input("ievadi otro skaitli "))
lielakais = maximum(skaitlis1, skaitlis2)
print(lielakais)