shopping_list = []

def show_help():
  print("What should we pick up at the store?")
  print("""
Enter 'DONE' to stop adding items
Enter 'HELP' for this help
Enter 'SHOW' to show list of items
""")

  
def add_to_list(item):
  shopping_list.append(item)
  print("You have {} items in your basket".format(len(shopping_list)))


def show_list():
  list_number = 1
  for item in shopping_list:
    print("Item {} => ".format(list_number) + item)
    list_number += 1
 

show_help()  
while True:
  new_item = input("> ")
  if new_item.upper() == "DONE":
    break
  elif new_item.upper() == "HELP":
    show_help()
    continue
  elif new_item.upper() == "SHOW":
    show_list()
    continue
  
  add_to_list(new_item)

print("Final List Items:")
show_list()

