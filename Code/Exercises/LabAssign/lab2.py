# Retrieve category & quantity for a requested fitness item.

catalog_file = open("catalog.txt","r")
fit_items = ['treadmill','lifting bars', 'exercise bikes', 'weights', 'rigs', 'dumbbells', 'gym mats', 'steppers', 'exercise balls', 'rowing machine', 'home gym']
d1 = dict() # to store item:category in this dictionary
d2 = dict() # to store item:quantity in this dictionary

# iterating over the fit_items
for item in fit_items:
  line_content = catalog_file.readline() # read contents from the line
  while line_content:
    if line_content.strip() == item:
      category = catalog_file.readline().strip() # get the corresponding category to the item
      item_quantity = catalog_file.readline().strip() # get the corresponding quantity to the item
      d1[item] = category
      d2[item] = item_quantity
      break # no need to search once we get the item in any line
    line_content = catalog_file.readline()

search_again = True # initial stage: keeping search on
while search_again:
  fitness_item = input("Enter a fitness item : ")
  try:  
    fitness_item_category = d1[fitness_item]
    fitness_item_quantity = d2[fitness_item]
  except KeyError: # handling key error
    print("Requested fitness item does not exist. Error raised: ", KeyError)
    continue # Continue the search as the requested item not there.

  # if item is present then  
  print(f"Fitness Item: {fitness_item}, Category: {fitness_item_category}, Quantity: {fitness_item_quantity}")
  wanna_search = input("Would you like to do another search (yes/no) --> ")
  if wanna_search.lower() == "yes":
    continue # continue the search until user want to search
  break # else stop the search
