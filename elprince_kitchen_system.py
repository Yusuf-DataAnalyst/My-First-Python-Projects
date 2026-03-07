print("***** Welcome To El Prince Kitchen *****👨🏻‍🍳")
Customers =int(input("Type The Number Of Customers 🧾"))
hour=int(input("Type The Hour ⏳"))
mintues=int(input("Type The Mintues ⏱️"))
current_hour=(hour*60)+mintues
iftar_time=(6*60)+10
result=iftar_time-current_hour
if result > 0:
    print(f"Fast! You have {result} minutes left!")
else:
    print("Iftar has started! Enjoy your meal 🌙")

capacity=50
time="5:10 PM"
breakfast="6:10 PM"
pots=(Customers+capacity-1)//capacity
print("----------------------------------------")
print(f"Remaining time to Iftar: {result} Minutes ⏳")
print(f"For {Customers} customers ")
print(f"You Need To Cook {pots} pots Of Rice 🍚 ")
print(f" You Should Start In {time} Because The Breakfast Is In {breakfast}  ")
