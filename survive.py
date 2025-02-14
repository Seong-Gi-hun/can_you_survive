import platform

def survive():
    
    id_numbers = [83, 74, 67, 69, 123, 121, 111, 117, 95, 103, 111, 116, 95, 105, 116, 125]
  
    return ''.join(chr(x) for x in id_numbers)

def is_online_platform():
   
    return platform.system() == "Linux"  


if is_online_platform():
    print(survive())  
