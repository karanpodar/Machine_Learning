a = [1, 2, 3, 4]

iter_a = iter(a)

while True:
    try:
        print(next(iter_a))
    except:
        print('In Ex')
        break
