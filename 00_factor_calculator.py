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
            if response >= low:
                return response
            #checks if number is lower than high
            elif response <= high:
                return response
            else: 
                print(error)
                print()

        except ValueError:
            print(error)
            print()

#calculates the factors of a number
def factor_calc(int):
    int



# main routine goes here
statement_generator("factors idk", "-")
num_check("Enter a number ", 1, 200)
