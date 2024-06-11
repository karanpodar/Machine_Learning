car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)
print(car['model'])

y = car.get("price")

print(y)     # if a key is not present in dict it will return the output as None 
print(car['price'])   # this will throw a Key value error yo avoid we use get() methods