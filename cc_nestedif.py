priceIsRight = 15

if priceIsRight < 5:
    print("Price is too low!")
elif priceIsRight <= 9:          ## instruction #2 says elif priceIsRight >= 5 and priceIsRight <= 9: --> priceIsRight >= 5 is not necessary
    print("Price is almost there!")
elif priceIsRight == 10:
    print("Price is exactly that!")
else:
    print("Price is too high!")