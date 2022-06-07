# 1. Basic
for x in range(0, 151):
    print(x)
# 2. Multiples of 5
for multiples in range(5, 1001, 5):
    print(multiples)
# 3. Counting, the Dojo Way
for dojo_count in range(1, 101):
    if dojo_count % 10 == 0:
        print("Coding Dojo")
    elif dojo_count % 5 == 0:
        print("Coding")
    else:
        print(dojo_count)
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
low_num = 6
high_num = 228
mult = 7
for mult_print in range(low_num, high_num + 1):
    if mult_print % mult == 0:
        print(mult_print)