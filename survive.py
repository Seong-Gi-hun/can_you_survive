import platform

def survive():
    id_numbers = [36, 74, 199, 8364, 45, 49, 84, 123, 52, 103, 51, 110, 116, 95, 107, 52, 49, 114, 48, 95, 48, 112, 51, 114, 52, 116, 49, 48, 110, 95, 115, 117, 99, 99, 51, 53, 53, 125]
    return ''.join(chr(x) for x in id_numbers)

print("You are on the way to find the flag")
print("\n".join(["."] * 500)) 
print(survive())
