"""The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True"""

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


"""We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False"""

def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or (not a_smile and not b_smile):
    return True
  else:
    return False

"""Given two int values, return their sum. Unless the two values are the same, then return double their sum.
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8"""

def sum_double(a, b):
  if a == b:
    return 2*(a+b)
  else:
    return a+b

"""Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
diff21(19) → 2
diff21(10) → 11
diff21(21) → 0"""

def diff21(n):
  if n > 21:
    return 2 * abs(n-21)
  else:
    return abs(21-n)

"""We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble."""
def parrot_trouble(talking, hour):
  if (hour < 7 or hour > 20) and talking:
    return True
  else:
    return False

"""Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10."""
def makes10(a, b):
  if (a == 10 or b == 10) or (a+b == 10):
    return True
  else:
    return False

"""Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number."""
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

"""
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative."""
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

"""Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged."""
def not_string(str):
  if str.startswith("not"):
    return str
  else:
    return "not "+str

"""Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive)."""
def missing_char(str, n):
    if n in range(0, len(str) - 1):
        return str[:n] + str[n + 1:]

"""Given a string, return a new string where the first and last chars have been exchanged."""
def front_back(str):
  if len(str)<=1:
    return str
  else:
    return str[-1]+str[1:len(str)-1]+str[0]

"""Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front."""
def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front

"""Given a string and a non-negative int n, return a larger string that is n copies of the original string."""
def string_times(str, n):
  return n*str

"""Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;"""
def front_times(str, n):
    if len(str) > 3:
        front = str[0:3]
    else:
        front = str
    return front * n

"""Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo"."""
def string_bits(str):
    res = ''
    for i in range(len(str)):
        if i % 2 == 0:
            res += str[i]
        else:
            continue
    return res

"""Given a non-empty string like "Code" return a string like "CCoCodCode"."""
def string_splosion(str):
  res = ''
  for i in range(len(str)+1):
    res += str[0:i]
  return res

"""Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring)."""
def last2(str):
    if len(str) < 2:
        return 0
    # last2 = str[len(str)-2:]
    last2 = str[-2:]
    count = 0
    for i in range(len(str) - 2):
        sub = str[i:i + 2]
        if sub == last2:
            count = count + 1
    return count

"""Given an array of ints, return the number of 9's in the array."""
def array_count9(nums):
  if len(nums) == 0:
    return 0
  else:
    count = 0
    for i in nums:
      if i==9:
        count += 1
  return count

"""Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4."""
def array_front9(nums):
    if len(nums) < 4:
        if 9 in nums:
            return True
        else:
            return False
    else:
        if 9 in nums[0:4]:
            return True
        else:
            return False

"""Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere."""

def array123(nums):
  if len(nums) < 3:
    return False
  else:
    flag = False
    for i in range(len(nums)):
      #print(nums[i:i+3])
      if nums[i:i+3] == [1,2,3]:
        flag=True
      else:
        continue
    return flag

#### STRINGS
"""Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!"."""
def hello_name(name):
  return ("Hello "+ name + "!")

"""Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi"."""
def make_abba(a, b):
  return a+b+b+a

"""The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>"."""
def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"

"""Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>"."""
def make_out_word(out, word):
  return out[0:len(out)/2]+word+out[len(out)/2:]

"""Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2."""
def extra_end(str):
  return 3*str[-2:]

"""Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string ""."""
def first_two(str):
  if len(str) < 2:
    return str
  else:
    return str[0:2]

"""Given a string of even length, return the first half. So the string "WooHoo" yields "Woo"""
def first_half(str):
  return str[0:len(str)/2]

"""Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2."""
def without_end(str):
    if len(str) < 2:
        return str
    else:
        return str[1:len(str) - 1]

"""Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0)."""
def combo_string(a, b):
  if len(a) < len(b):
    return a+b+a
  else:
    return b+a+b

"""Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1."""
def non_start(a, b):
  if len(a) <1 or len(b) < 1:
    return
  else:
    return a[1:]+b[1:]

"""Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2."""
def left2(str):
  if len(str) < 2:
    return
  else:
    return str[2:]+str[0:2]

"""Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more."""
def first_last6(nums):
  if len(nums) < 1:
    return False
  else:
    if (nums[0] ==6 or nums[-1]==6):
      return True
    else:
      return False

"""Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal."""
def same_first_last(nums):
    if len(nums) >= 1:
        if nums[0] == nums[-1]:
            return True
        else:
            return False
    else:
        return False

"""Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more."""
def common_end(a, b):
  if len(a) < 1 or len(b) < 1:
    return False
  else:
    if a[0]==b[0] or a[-1]==b[-1]:
      return True
    else:
      return False

"""Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}."""
def rotate_left3(nums):
  if len(nums) != 3:
    return 0
  else:
    lst1 = nums[1:]
    lst1.append(nums[0])
    return lst1

"""Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}."""
def reverse3(nums):
  if len(nums) != 3:
    return 0
  else:
    return nums[::-1]

"""Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array."""
def max_end3(nums):
  if len(nums) != 3:
    return 0
  else:
    if nums[0] > nums[-1]:
      return [nums[0],nums[0],nums[0]]
    else:
      return [nums[-1],nums[-1],nums[-1]]

"""Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0."""
def sum2(nums):
  if not nums:
    return 0
  elif len(nums) == 1:
    return nums[0]
  else:
    sum = 0
    for i in range(2):
      sum += nums[i]
  return sum

"""Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements."""
def middle_way(a, b):
  if len(a) !=3 or len(b) != 3:
    return 0
  else:
    return [a[1],b[1]]

"""Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more."""
def make_ends(nums):
  if len(nums) < 1:
    return
  else:
    return [nums[0],nums[-1]]

"""Given an int array length 2, return True if it contains a 2 or a 3.'"""
def has23(nums):
  if not nums:
    return
  else:
    if 2 in nums or 3 in nums:
      return True
    else:
      return False

"""When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise."""
def cigar_party(cigars, is_weekend):
  if is_weekend:
    if cigars >= 40:
      return True
    else:
      return False
  else:
    if cigars >= 40 and cigars <= 60:
      return True
    else:
      return False

"""You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe)."""
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  else:
    return 1

"""The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise"""
def squirrel_play(temp, is_summer):
    if is_summer:
        if temp >= 60 and temp <= 100:
            return True
        else:
            return False
    else:
        if temp >= 60 and temp <= 90:
            return True
        else:
            return False

"""
You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
"""
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <=65:
      return 0
    elif speed >= 66 and speed <= 85:
      return 1
    elif speed >= 87:
      return 2
  else:
    if speed <=60:
      return 0
    elif speed >= 61 and speed <= 80:
      return 1
    elif speed >= 81:
      return 2

"""Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20."""
def sorta_sum(a, b):
  sum = a+b
  if sum in range(10,20):
    return 20
  else:
    return sum

"""Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off"."""
def alarm_clock(day, vacation):
  if vacation:
    if day in range(1,6):
      return '10:00'
    else:
      return "off"
  else:
    if day in range(1,6):
      return '7:00'
    else:
      return '10:00'

"""The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number."""
def love6(a, b):
  if a ==6 or b ==6:
    return True
  elif a+b == 6 or abs(a-b)==6:
    return True
  else:
    return False

"""Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10."""
def in1to10(n, outside_mode):
  if outside_mode:
    if n <=1 or n >= 10:
      return True
    else:
      return False
  else:
    if n in range(1,11):
      return True
    else:
      return False

"""Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod
"""
def near_ten(num):
  if num % 10 <= 2 or num%10 >= 8:
    return True
  else:
    return False

"""Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
"""
def count_evens(nums):
  count = 0
  for i in nums:
    if i%2 == 0:
      count += 1
    else:
      continue
  return count

"""Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values."""
def big_diff(nums):
  min_val = min(nums)
  max_val = max(nums)
  return max_val-min_val

def has22(nums):
  flag = False
  for i in range(0,len(nums)-1):
    if nums[i] == 2:
        print(i,nums[i])
        if nums[i+1] == 2:
            flag = True
        else:
            flag = False
            continue
    else:
        flag = False
        continue
    return flag




if __name__=="__main__":
    print(sleep_in(True,False))
    print(monkey_trouble(True,False))
    print(sum_double(2,2))
    print(diff21(21))
    print(parrot_trouble(False, 6))
    print(pos_neg(-4, -5, True))
    print(not_string('not bad'))
    print(front_back('ab'))
    print(front3('abc'))
    print(string_times('Hi', 1))
    print(front_times('Chocolate', 3))
    print(string_bits('Hello'))
    print(string_splosion('Code'))
    print(last2('axxxaaxx'))
    print(array_front9([1, 2, 9, 3, 4]) )
    print(array123([1, 1, 2, 3, 1]))
    print(has22([1, 2, 2]))
