# My-First-Python-Projects
Expenses =[]
name_expenses=[]
while True:
    name=input("Type the name of the expenses? or type (q) to print the expenses\n").lower()
    if name=="q":
        print(f"Total: {sum(Expenses)} | Details: {dict(zip(name_expenses, Expenses))}")

        break
    else:    
     price=int(input("Type the price?\n"))
     Expenses.append(price)
     name_expenses.append(name)
