import random
otp = random.randrange(10000)       # -> 0 to 10000 with step of 1
print(">> 1. OTP is:", otp)

otp = random.randrange(2000, 6000)  # -> 2000 to 6000 with step of 1
print(">> 2. OTP is:", otp)

otp = random.randrange(2000, 6000, 10)  # -> 2000 to 6000 with step of 10
print(">> 3. OTP is:", otp)

otp = random.randint(1000, 9000)    # random number in range 1000 to 9000
print(">> 4. OTP is:", otp)

# Try Implementing Algorithm for generating OTP's
# Find Algo where the same number wont be repeated

