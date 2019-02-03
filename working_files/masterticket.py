TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100  

def total_order(ticket_quantity):
  total_ticket_cost = (ticket_quantity * TICKET_PRICE) + SERVICE_CHARGE
  return total_ticket_cost

while tickets_remaining > 0:
  print("Welcome, there are {} tickets remaining".format(tickets_remaining))
  user_name = input("Please enter your name: ")
  try:
    ticket_order_quantity = int(input("{}, How many tickets would you like? ".format(user_name)))
    if ticket_order_quantity > tickets_remaining:
      raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
  except ValueError as err:
    print("Sorry we ran into an error. {}. Please try again".format(err))
  else:
    order_total = total_order(ticket_order_quantity)
    print("{}, your total order would be ${}.".format(user_name, order_total))
    confirm_status = input("{}, Do you wish to proceed with your order of {} tickets at a total price of ${}? Y/N: ".format(user_name, ticket_order_quantity, order_total))
    if confirm_status.upper() == "Y":
      print("Sold!, {} your purchase is confirmed.".format(user_name))
      tickets_remaining -= ticket_order_quantity
    else:
      print("Thankyou {} for your interest in our tickets".format(user_name))
print("All Tickets are now sold")

