import time, os 
pizza=[]

try:
  f=open("pizza.hut","r")
  pizzas=eval(f.read())
  f.close()
except:
  print("\033[31mError occurred...No such file exists🤔 \033[0m")
    

def add():
  time.sleep(2)
  os.system("clear")
  type=input("What type shall you take? ")
  num=input("How many pizzas mon ami? ")
  if num.isnumeric()==False:
    num=input("Error...enter digit figures only~~ ")
  size=input("What size shall you take, s/m/l? ").lower()
  cost=0
  if size=="s":
    cost=4.89
  elif size=="m":
    cost=9.99
  else:
    cost=12.99
  
  total=int(num)*int(cost)
  name=input("What's your name?😌 ")
  print("\033[32mInfo updated...\033[0m")
  row=[name,type,size,num,total]
  pizza.append(row)

def view():
  it="Name"
  it1="PizzaType"
  it2="Size"
  it3="Qty"
  it4="Cost"
  print(f"{it:^7}{it1:10}{it2:^7}{it3:^6}{it4:^12}")
  for row in pizza:
   print(f"{row[0]},{row[1]},{row[2]} {row[3]}, {row[4]}")
   print(f"\033[34mHello {row[0]}. Total cost is Ksh.{row[4]} \033[0m")

while True:
  time.sleep(2)
  os.system("clear")
  print("\033[33m⭐🍕Kip's Pizzas⭐🍕\033[0m")
  menu=input("1. Add order\n2. View order\n>>")
  if menu=="1" or menu=="Add":
    add()
  else:
    view()
  f=open("pizza.hut","w")
  f.write(str(pizza))
  f.close()
  
  
  
  

    


