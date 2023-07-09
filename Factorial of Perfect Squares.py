import math

def is_perfect_square(num):
  """Return True if num is a perfect square, False otherwise"""
  sqrt = int(math.sqrt(num))
  return sqrt * sqrt == num

def get_factorial_trailing_digits(num):
  """Return the last 3 digits of the factorial of num"""
  factorial = 1
  for i in range(2, num+1):
    factorial *= i
    if factorial % 1000 == 0:
      return str(factorial // 1000)[-3:]
  return str(factorial)[-3:]

def generate_output_string(input_str):
  """Generate output string from input string of integers"""
  input_nums = list(map(int, input_str.split(",")))
  positive_nums = [num for num in input_nums if num > 0]
  perfect_squares = [num for num in positive_nums if is_perfect_square(num)]
  if not perfect_squares:
    return "-1"
  output_list = [get_factorial_trailing_digits(num) for num in perfect_squares]
  return ",".join(output_list)

input_str = input("Enter the input string of integers: ")
output_str = generate_output_string(input_str)
print("Output string:", output_str)
