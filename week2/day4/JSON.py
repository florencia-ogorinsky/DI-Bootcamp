#JavaScriptObjectNotation
#Loos like a dictionary but is a string 
# import json (for python)


# my_family = {
#     "parents":['Beth', 'Jerry'],
#     "children":['Summer', 'Morty']
# }

#json.dump{object to save, destination file}  
#.json



import json

my_family = {
    "parents" :['Beth', 'Jerry'],
    "children" :['Summer', 'Morty']
}

json_file = "family.json"

with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj)


