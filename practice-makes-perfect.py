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
  
#6/15
  def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

  print is_prime(13)
  print is_prime(10)

"""
  I had difficulty with this one. My problem was complex control-flow. 
  With a better macro understanding with what does and what doesn't qualify as a prime, I would have produced a more elegant solution.
"""

#7/15
  def reverse(text):
    text = str(text)
    rev_list = []
    for letter in range(len(text)-1, -1, -1):
      rev_list.append(text[letter])
    rev_string = "".join(rev_list)
    return rev_string

  reverse('palindrome')

#8/15
  
