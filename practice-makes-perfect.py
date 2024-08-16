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
  for letter in word:
    # problem: the sequence of the letters in 'word' is key
    # solution: preserve the order
    # implementation: use a switch in a while loop so that if the next letter after the word is also equal to the letter in text, the switch remains true and will perform some action. it is not equal, the switch will be false and will not perform the action.

    while True:
      if letter in word:


  # return text replaced by word to asterisks

text = "this hack is wack hack"
word = "wack"

censor(text, word)