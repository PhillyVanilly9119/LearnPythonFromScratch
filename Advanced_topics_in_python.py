# return functions for dictionaries are:
# .items(), .keys() and .values() -> They dont return it in any order though
# IMPORTANT !!! check all the variables an print orders before running!!!
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

even_squares = [x ** 2 for x in range(1,12) if (x ** 2) % 2 == 0]
print even_squares

cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
print cubes_by_four

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message

# Quick Interejction! Syntax for list slicing [start:end:stride]
# Default Python examples print to_five[3:]
# prints ['D', 'E']
# print to_five[:2]
# prints ['A', 'B']
# print to_five[::2]
# print ['A', 'C', 'E']

my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)

# Introduction to the lambda- function (= temporary function or dynamic function)
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

squares = [x ** 2 for x in range(1,11)]
print filter(lambda x: x > 30 and x < 70, squares)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != 'X', garbled)
print message




# Review of interating over a dictionary ('dict')
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}
print movies.items()
