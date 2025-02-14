import platform

def survive():
    id_numbers = [83, 74, 67, 69, 123, 121, 111, 117, 95, 103, 111, 116, 95, 105, 116, 125]
    return ''.join(chr(x) for x in id_numbers)


print("You are on the way to find the flag")
print("\n".join(["."] *500)) 
print(survive())
