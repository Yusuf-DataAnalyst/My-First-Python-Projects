#Sales Analysis Project - Accomplished 📉
product=[]
price=[]
Quantity=[]
totals=[]
print("******Welcome To Sales Analysis Project - Accomplished 🛒📉 ******")
while True:
    name=input("What Is The Name Of Product ? Or Type (q) To Quit  :").lower()
    if name =="q":
        if len(totals)>0:
            total_revenue=sum(totals)
            max_money=max(totals)
            the_index=totals.index(max_money)
            name_of_best=product[the_index]
            
            print("""******TOTAL*****""")
            
            print(f"Totals:{sum(totals) : .2f} Details :{dict(zip(product,totals))}")
            print(f"The King Of The Sales is {name_of_best} {max_money:.2f}  ")
            break
        else:
             print("No Data Entered !")
             break
    else :
             product.append(name)
             price_1=float(input(f"What Is The Price Of {name} $"))
             price.append(price_1)
             quantity=int(input(f"What Is The Quantity Of {name}  "))
             Quantity.append(quantity)
             result=price_1*quantity
             totals.append(result)
