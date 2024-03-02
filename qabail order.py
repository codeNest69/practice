print("-----------QUETTA QABAIL MEANU-----------")

menu    = {"chai": 60,
          "sada paratha":50,
          "aalo paratha":120,
          "half fry":50,
          "homlate":70,
          "sabaz chai":50,
          "speacial paratha":100,
          "full fry":70,
          }
cart=[]
total = 0

menu.update({"cofee":150})

for key , value in menu.items():
    print(f"{key:10} : Rs.{value:.2f}")
print("-----------------------------------------")

while True:
    order = input("kya chaiye kilwalaa:(q to quit)") .lower()
    if order == "q":
        break
    elif menu.get (order) is not None:
        cart.append(order)

print("---------------TUMARA ORDER-----------------")        
for order in cart:
    total += menu.get(order)
    print(order, end=" ")

print()
print(f"total : Rs.{total:.2f}")

print("-------------MEHRABANI QURBAN ---------------")


