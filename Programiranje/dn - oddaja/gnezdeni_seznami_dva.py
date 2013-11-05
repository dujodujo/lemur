a = 3
b = 5
for i in range(1,101):
    if not i % a:
        if not i % b:
            print("fizzbuzz")
        print("fizz")
    elif not i % b == 0:
        print("buuz")
    else:
        print(i)

