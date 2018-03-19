
# The following functions were coded from the "practice!"- exercise on Codeacademy(c)
# Note that some (the majority) are the solutions from Codeacademy(c)
def is_even(x):
    # This function return whether or not a number a even
    if x % 2 == 0:
        return True
    else:
        return False

# print is_even(33)

def is_int(number):
    # This function returns whether or not a input (number) is an interger
    absolute_count = abs(number)
    type_count = type(number)
    round_count = round(absolute_count)
    if type_count and absolute_count - round_count == 0:
        return True
    else:
        return False

# print is_int(45.5)

def digit_sum(x):
    # This function returns the cross sum of a number (sum of all digits)
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        print x
    return total

# print digit_sum(12345)

def factorial(number):
    # This function returns the factorial of any number it is fed
    total = 1
    while number > 1:
        total *= number
        number -= 1
    return total

# print factorial(5.0)

def is_prime(number):
    # This function returns whether or not a number is prime
    if number < 2:
        return False
    else:
        for n in range(2, number - 1):
            if number % n == 0:
                return False
        return True

# print is_prime(237846)

def reverse(reversable_text):
    # This function reverses the order of letters in a string
    word = ""
    l = len(reversable_text) - 1
    while l >= 0:
        word = word + reversable_text[l]
        l -= 1
    return word

# print reverse("Take Caps Aswell As Spaces ?")

def anti_vowel(text):
    # This function only returns only the consonants of a string
    t = ""
    for c in text:
        for i in "aeiouAEIOU":
            if c == i:
                c = ""
            else:
                c = c
        t = t + c

    return t

# print anti_vowel("Was soll das denn sein?!")

def scrabble_score(word):
    # This function adds the values of a letter within a string, kinda like a simplified scrabble-game would work
  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
  word = word.lower()
  total  = 0
  for letter in word:
    for leter in score:
      if letter == leter:
        total = total + score[leter]
  return total

# print scrabble_score('Matthias')

def censor(text, word):
    # This function censors a word/ letter/ sentence within a given word/ letter/ sentence
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result

# print censor("This is shit", "shit")

def count(sequence, item):
    # This function counts a certain item in a list and returns the sum of the item within the list
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count

# print count([1, 2, 312, 2, 3, 32, 2312, 1, 312, 3, 2, 1, 1], 1)

def purify(list):
    # This function only prints even numbers within a given list of numbers
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)

    return new_list

# print purify([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def product(int_list):
    # This function returns the product of all the intergers within a given list
    total = 1
    for num in int_list:
        total = total * num
    return total

# print product([1, 2, 3, 4, 5])

def remove_duplicates(doupl_list):
    # This function removes all the duplicates from a given list of numbers
    if doupl_list == []:
        return []

    doupl_list = sorted(doupl_list)
    output_list = [doupl_list[0]]

    for i in doupl_list:
        if i > output_list[-1]:
            output_list.append(i)

    return output_list

# print remove_duplicates([1, 1, 2, 2, 3, 3, 3])

def median(lst):
    # This function returns the median (middle- most element) of a list after sorting it
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        index = len(sorted_list)//2
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2]) / 2.0
        return mean

# print median([1, 5, 6, 4])
