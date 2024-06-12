import Levenshtein

dist = Levenshtein.distance('Table', 'T@ble')

print(dist)