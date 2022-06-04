# 1. Basic
for x in range(0, 151):
    print(x)
# 2. Multiples of 5
for multiples in range(5, 1001, 5):
    print(multiples)
# 3. Counting, the Dojo Way
for DojoCount in range(1, 101):
    if DojoCount % 10 == 0:
        print("Coding Dojo")
    elif DojoCount % 5 == 0:
        print("Coding")
    else:
        print(DojoCount)
# 4. Woah, That's Huge
num_sum = 0
for odd_num in range(0, 500001):
    if odd_num % 2 != 0:
        num_sum = num_sum + odd_num
print(num_sum)
# 5. Countdown by Fours
for num in range(2018, 0, -4):
    print(num)
# 6. Flexible Counter
lowNum = 6
highNum = 228
mult = 7
for mult_print in range(lowNum, highNum + 1):
    if mult_print % mult == 0:
        print(mult_print)