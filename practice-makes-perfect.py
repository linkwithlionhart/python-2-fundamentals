#2/15
  def is_even(x):
    if x % 2 == 0:
      return True
    else:
      return False

#3/15
  def is_int(x):
    if x % 1 == 0:
      return True
    else:
      return False

#4/15
  n = 1234
  def digit_sum(n):
    #turn into stirng
    str_array = str(n)
    num_array = []
    total = 0
    for letter in str_array:
      num_array.append(int(letter))
    for number in num_array:
      total += number
    return total

    # call and test
    print digit_sum(n)
    print type(digit_sum(n))
  
  #5/15
    def factorial(x):
      refined_num = int(x)
      num_list = []
      total = 1
      while refined_num > 0:
        num_list.append(refined_num)
        refined_num -= 1
      # print num_list
      for num in num_list:
        total *= num
      return total

    print factorial(9) 