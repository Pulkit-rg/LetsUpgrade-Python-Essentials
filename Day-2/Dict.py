#Dictionary and its default functions

avenger={"name": "Thor", "Age":1500, "weapon": "Stormbreaker"}
print(avenger)

#1. get function- used for getting the value of the key mentioned
avenger={"name": "Thor", "Age":1500, "weapon": "Stormbreaker"}
print(avenger.get("weapon"))

# 2. keys function - used to get all the keys

avenger={"name": "Thor", "Age":1500, "weapon": "Stormbreaker"}
print(avenger.keys())

# 3. Items function- used to get all the key-value pairs in the list

avenger={"name": "Thor", "Age":1500, "weapon": "Stormbreaker"}
print(avenger.items())

# 4. pop function - used for removing a key-value pair
avenger={"name": "Thor", "Age":1500, "weapon": "Stormbreaker"}
print(avenger.pop("weapon"))
print(avenger)

# 5. update function- for adding a key-value pair in the dictionary
avenger={"name": "Thor", "Age":1500, "weapon": "Stormbreaker"}
avenger.update({"Address": "Asgard"})
print(avenger)
