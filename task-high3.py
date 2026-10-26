def add(a):
    def inner(b):
        return a + b
    return inner


add_five = add(1)

print("1 + 1 = ", add_five(1))
print("1 + 5 = ", add_five(5))
print("1 + 9 = ", add_five(9))
print("1 + 14 = ", add(1)(14))