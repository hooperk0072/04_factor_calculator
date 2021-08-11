# puts a series of symbols at start and end of text for emphasis
def statement_generator(text, decoration):

    # make string with five characters
    ends = decoration * 5

    # add decoration to start and end of a statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return""

#checks input is a number more than a given value
def num_check(question, low, high):

    valid = False
    while not valid: 

        error = 'Please enter a number that is more than or equal to {}, and lesser than {}.'.format(low, high)

        try:

            # asks user to enter a number
            response = int(input(question))

            # checks if numer is more than low
            if low >= response <= high:
                return response

            else: 
                print(error)
                print()

        except ValueError:
            print(error)
            print()

import random

my_list = []

# generate 4 random numbers between 1 & 10...
for item in range(0, 4):

    # generate random number between 1 and 10
    random_num = random.randint(1, 10)

    # add number to list
    my_list.append(random_num)

# print the unsorted list
print(my_list)

# sort the list
my_list.sort()

my_list_len = len(my_list)

# print the sorted list
print()
print(my_list)
print("The list has {} items".format(my_list_len))
print()



# main routine goes here
statement_generator("factors idk", "-")
num_check("Enter a number ", 1, 200)
