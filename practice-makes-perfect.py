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
  # make vowel reference
  lower_vowels = 'aeiou'
  upper_vowels = lower_vowels.upper()
  all_vowels = lower_vowels + upper_vowels
  print all_vowels

  def anti_vowel(text):
    # initialize result to return
    result = ''
    # only concatenate matches in vowel reference
    for letter in text:
      if letter not in all_vowels:
        result += letter
    return result

  print anti_vowel("Hey You!")

#9/15
  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
          "x": 8, "z": 10}

  word = "Helix"

  def scrabble_score(word):
    total_score = 0
    lower_word = word.lower()
    for letter in lower_word:
      total_score += score[letter]
    return total_score

  print scrabble_score(word)

  """
  Make sure you double check variable naming. My conflict with score took longer to solve than expected. The approach was correct.
  """
#10/15
  def censor(text, word):
    text_list = text.split()
    # print text_list
    result = ''
    stars = '*' * len(word)
    count = 0

    for target in text_list:
      if target == word:
        # print target
        text_list[count] = stars
      count += 1
    result = ' '.join(text_list)

    return result

  # test case
  text = "this hack is wack hack"
  word = "hack"

  print censor(text, word)

#11/15
  def count(sequence, item):
    count = 0
    
    for target in sequence:
      if target == item:
        count += 1

    # return an integer
    return count

  print count([1, 2, 1, 1], 1)

#12/15
  def purify(number_list):
    even_list = []

    for num in number_list:
      if num % 2 == 0:
        even_list.append(num)
    
    return even_list

  # test case
  purify([1,2,3])

#13/15
  def product(int_list):
    product = 0
    if len(int_list) > 0:
      product = 1 

    for num in int_list:
      product *= num
    
    return product

  print product([4, 5, 5])

#14/15
  def remove_duplicates(ls):
    ls = sorted(ls)
    result = []

    for target in ls:
      if target not in result:
        result.append(target)
        print target

    return result

  print remove_duplicates([1, 1, 2, 2])

#15/15
  def median(ls):
  ls = sorted(ls)
  result = 0

  # case has one item
  if len(ls) == 1:
    return ls[0]
  # case is odd, return middle value
  elif len(ls) % 2 != 0:
    result = ls[len(ls) / 2]
  # case is even, return average of middle 2 values
  else:
    low_median = int(float(len(ls)) / 2) - 1 
    high_median = low_median + 1 
    result = (ls[low_median] + ls[high_median]) / float(2)

  return result

# test cases
  # even
  print median([4, 5, 5, 4])
  # odd 
  print median([6, 8, 12, 2, 23])