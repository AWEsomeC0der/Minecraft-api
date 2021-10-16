import json


hi = input('Name: ')

hi = hi.title() #title is a function that returns a string.

#https://www.w3schools.com/python/ref_string_title.asp

with open('items.json','r') as fp:
  items_dict =  json.load(fp)


#Open: ooking at the json file, we observe a list that has a dictionary of each item in Minecraft.

#items = each dictionary entry
for item in items_dict: #For items in a list (from json)
  if hi == item["displayName"]: #Determine if input matches dictionary display name.
    #print(item)
    for x in item:#print the attributes 

      #Declutter condition to not display duplicate information.
      if x != "displayName" and x != "name": 

        if x == "variations":
          for y in item["variations"]:
            print(y["metadata"], y["displayName"])
        else:
          print(x, item[x])


#Summary: Designed and created the search functions within a json object. We were able to display the attributes of an item. Also, we tidied up print statements, so the code would not print out duplicate information.



#Ideas and functions:

#- Reverse Search of given a partial description of an item, display all items that are close to that description

#i.e. input = sword returns wooden sword, stone sword, iron sword .......

#******************HOMEWORK******************************************
# - Given an enchantment, determine which applicable tool it can go on. 
# different algorithms and conditions needed:
# if "enchant categories" == userinput print possible tools that "enchantment" can go on.
# userinput("give an enchant categorie")
#******************HOMEWORK******************************************


#For next week:

#Using the search function created from today, see if you can do one of the following functions from the ideas. 

#Reverse search is similar to what we created today in class, but instead of ==, we should use ........
#Check conditionals and comparisons from w3 
