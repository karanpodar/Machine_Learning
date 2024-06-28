class Animal:
	name = 'lucky'
	
p = Animal()
print('Before modification:', p.name)
setattr(p, 'name', 'Woozoo')

print(getattr(p, 'name'))

print('After modification:', p.name)

print('After modification:', getattr(p, 'name'))