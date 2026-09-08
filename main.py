import random


def search():
  name = input("What is the name of your monster: ")
  found = False
  with open("Monsters.txt","r", encoding="utf-8") as file:
      for line in file:
          content = line.strip().split(",")
          if name == content[1]:
              found = True
              name = content[1]
              Origin = content[2]
              Description = content[3]
              Attack = content[4]
              Magical_Force = content[5]
              Magical_Defense = content[6]
              Defense = content[7]
              Intelligence = content[8]
              Health = content[9]
              Experience = content[10]
              break




  if found:
      print(f"Name: {name} | Origin: {Origin} | Description: {Description} | Attack: {Attack} | Magical Force: {Magical_Force} | Magical Defense: {Magical_Defense} | Defense: {Defense} | Intelligence: {Intelligence} | Health: {Health} | Experience: {Experience} ")
  else:
      print("The monster named does not exist")




  main()




def main():
  choice = input("What would you like to do today \n"
                 "[1] Random Monster Encounter\n"
                 "[2] Search for a monster\n"
                 "[3] Output list of favourite monsters\n"
                 "[4] Add a monster to list of favourites\n"
                 "[5] Remove monster from list of favourites\n"
                 "[6] Stop\n"
                 ": "
              )
  match choice:
      case "1":
          random_encounter()
      case "2":
          search()
      case "3":
          output()
      case "4":
          addlist()
      case "5":
          remove()
      case "6":
          return 0
      case _:
          print("Please input a valid choice (1 to 6)")
          main()




def random_encounter():
  with open("Monsters.txt", "r", encoding="utf-8") as monster_file:
      monsters = monster_file.readlines()
      tempbuffer = random.choice(monsters)
      content = tempbuffer.strip().split(",")
      name = content[1]
      Origin = content[2]
      Description = content[3]
      Attack = content[4]
      Magical_Force = content[5]
      Magical_Defense = content[6]
      Defense = content[7]
      Intelligence = content[8]
      Health = content[9]
      Experience = content[10]
      print(f"Name: {name} | Origin: {Origin} | Description: {Description} | Attack: {Attack} | Magical Force: {Magical_Force} | Magical Defense: {Magical_Defense} | Defense: {Defense} | Intelligence: {Intelligence} | Health: {Health} | Experience: {Experience} ")




  main()
def addlist():
  name = input("What is the name of your monster: ")
  found = False
  with open("Monsters.txt", "r", encoding="utf-8") as file:
      for line in file:
          content = line.strip().split(",")
          if name == content[1]:
              found = True
              name = content[1]
              break
  if found:
      with open("Favourites.txt", "r", encoding="utf-8") as file:
          InFavourite = False
          for line in file:
              if line == name:
                  print("Monster is already in your favourite list!")
                  InFavourite = True
                  break
          if not InFavourite:
              with open("Favourites.txt", "a", encoding="utf-8") as file:
                  file.write(f"{name}\n")








  else:
      print("The monster named does not exist")




  main()












def output():
  print("List of favourite monsters: ")
  with open("Favourites.txt","r", encoding="utf-8") as file:
      for line in file:
          line.strip()
          print(line)








  main()




def remove():
   name = input("What is the name of the monster that you want to remove from your list of favourites?: ")
   with open("Favourites.txt","r",encoding="utf-8") as file:
       lines = file.readlines()
      


   with open("Favourites.txt", "w", encoding="utf-8") as file:
       for line in lines:


           if line.strip("\n") != name.strip():
               file.write(line)


   main()










main()



