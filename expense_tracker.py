# My-First-Python-Projects
Expenses =[]
print("*****Welcome To ​📊 Expense Tracker Project*****")
name_expenses=[]
while True:
    name=input("Type The Name Of The Expenses? Or Type (q) To Quit 🔚 \n").lower()
    if name=="q":  
        if len(Expenses)==0:
            print("There Is No Data To Account! ")
            break
        else:
            average=sum(Expenses)/len(Expenses)
            high=max(Expenses)                                       
        
        print(f"Total: ${sum(Expenses)} | Details: {dict(zip(name_expenses, Expenses ))}")
        print(f"The High Expenses is {high}  and the average is {average: .2f}")

        break
    else:    
     price=int(input("Type the price 💰?\n"))
     if price>500:
         print("The Price Is To High !🔝")
     Expenses.append(price)
     name_expenses.append(name)
