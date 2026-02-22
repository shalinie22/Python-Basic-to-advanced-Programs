lower = int(input("Enter the starting number:"))
Upper = int(input("Enter the ending number:"))

for num in range(lower, Upper+1):
    temp_num = num
    total_sum=0
    num_digits = len(str(num))

    while temp_num>0:
        digits = temp_num%10
        total_sum += digits**num_digits
        temp_num //=10

    if total_sum == num:
        print(total_sum)

