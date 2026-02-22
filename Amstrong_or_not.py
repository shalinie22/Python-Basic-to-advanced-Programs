num = int(input("Enter the number:"))

num_digits = len(str(num))

temp_num = num
sum_digits =0

while temp_num>0:

    digits = temp_num%10
    sum_digits += digits**num_digits
    temp_num //= 10

if sum_digits == num:
    print(f"{num} is a Armstrong number")
else:
    print(f"{num} is not a  Armstrong number")