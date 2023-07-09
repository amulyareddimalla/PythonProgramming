'''def is_one_step_number(num):
    num = str(num)
    for i in range(len(num)-1):
        if abs(int(num[i]) - int(num[i+1])) != 1:
            return False
    return True

def main():
    s, e = map(int, input("Enter the range (lower limit, upper limit): ").split(','))
    one_step_numbers = [num for num in range(s, e+1) if is_one_step_number(num)]
    if one_step_numbers:
        print(', '.join(map(str, one_step_numbers)))
    else:
        print(-1)

if __name__ == '__main__':
    main()'''

#2nd code
def one_step_number(num):
    str_num = str(num)
    for i in range(len(str_num)-1):
        if abs(int(str_num[i]) - int(str_num[i+1])) != 1:
            return False
    return True

def get_one_step_numbers(s, e):
    one_step_nums = []
    for num in range(s, e+1):
        if one_step_number(num):
            one_step_nums.append(num)
    return one_step_nums

input_str = input("Enter the range (S,E): ")
s, e = map(int, input_str.split(","))
if len(str(s)) < 2 or len(str(e)) < 2:
    print("Both numbers should be at least 2 digits.")
else:
    one_step_nums = get_one_step_numbers(s, e)
    if one_step_nums:
        print(", ".join(map(str, one_step_nums)))
    else:
        print(-1)


