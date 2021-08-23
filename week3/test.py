"""
my_string = "giraffe"
print(my_string[-1])
print(my_string[2:4])

print(my_string[-1])
print(my_string[-7:-1:-1])
print(my_string[-1:-7])
"""

my_string = "012345"
#[start, stop, stride]

print(my_string[-1])        # 5
print(my_string[-1::])      # 5         you get the last character
print(my_string[:-1])       # 01234     you get everything but the last character

print(my_string[-1::-1])      # 543210      start at the right and step left reverse order , no end (default)
print(my_string[-1:-6:-1])    # 543210      start at the right and step left to char -6
print(my_string[:-1:1])       # 01234       start at the beginning and step right to one shy of the end  

print(my_string[-6::1])     # 012345
print(my_string[-6:-1:1])   # 01234
print(my_string[-6:0:1])    #  no print  & no error  
print(my_string[-6:-5:-1])    #  no print  & no error  ** start, stop, stride doesn't make logical sense.. 

print(my_string[-2:-4:-1])   # 43       reverse order -- you get -2(4) and -3(3)
print(my_string[-4:-2:1])   # 23         you get -4(2) and -3(3)


