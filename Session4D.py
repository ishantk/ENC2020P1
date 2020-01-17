# Shift Operators >> <<

# num1 = 8
num1 = -13
num2 = 2
num3 = num1 >> num2

print(">> num1 is:", num1, bin(num1))
print(">> num2 is:", num2, bin(num2))
print(">> num3 is:", num3, bin(num3))

"""
    num1 := 1 0 0 0 >> 2
            _ _ 1 0
            0 0 1 0 -> 2

    num1 := 1 0 1 1 >> 2
            _ _ 1 0
            0 0 1 0 -> 2
            
    num1 := 1 0 1 1
            0 1 0 0
                  1
            0 1 0 1 >> 2
            
            _ _ 0 1
            
            1 1 0 1
            0 0 1 0
                  1
            0 0 1 1 -> -3 
            
    num1 := 1 1 0 1
            0 0 1 0
                  1
            0 0 1 1
            >> 2
            _ _ 0 0
            1 1 0 0
            
            0 0 1 1
                  1
            0 1 0 0  -> -4                                
    
"""

num4 = 8
num5 = 3
num6 = num4 << num5

num7 = num6 >> num5

"""
    num4 := 0 0 0 0  1 0 0 0
            0 0 1 0  0 0 0 0 -> 32
"""

print(">> num6 is:", num6)
print(">> num7 is:", num7)

# PS: Right Shift -> / by 2 pow shift
#     Left Shift ->  * by 2 pow shift

# HW: Please Explore left shift operator on negative numbers
# HW: Please Explore will above formula work same for -ves
# HW: Do explore where else other than security we can use Shift Operators

