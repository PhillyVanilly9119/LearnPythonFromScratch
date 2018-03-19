# The follwing scripts are used to practice simple statistics tasks
# Note that this code is from Codeacademy(c) and can contain copyrighted
# solutions from codeacademy.com
# Also note that functions call each other and maybe need the print- functions
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
    # This function returns a list if grades (numbers)
    for grade in grades_input:
        print grade

# print print_grades(grades)

def grades_sum(scores):
    # This script returns the sum of a list of numbers -> easier: 'sum()'- function
    sum_grades = 0
    for grade in scores:
        sum_grades += grade
    return sum_grades

# print grades_sum(grades)

def grades_average(grades_input):
    # Calculates the average number of a list of numbers
    # Note that this function calls the beforehand initialized  function 'grades_sum'
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average

# print grades_average(grades)

def grades_variance(scores):
    # This function returns the variance of a list of numbers
    # Note that this functions calls the function 'grades_average',
    # which calls the function 'grades_sum'
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)

# print grades_variance(grades)

def grades_std_deviation(variance):
    # This function prints the standard deviation of a list of numbers*
    # Note that this function calls the function 'grades_variance',
    # which calls the function 'grades_average',
    # which calls the function 'grades_sum'
  return variance ** 0.5

variance = grades_variance(grades)

# print grades_std_deviation(variance)
# Think of what function need which input in order to print a reasonable or
# functioning result
