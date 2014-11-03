__author__ = 'Claudio'


"""Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""
def read_sdin(data):
    age = 1
    if age > 0:
        try:
            age = int(input( "Enter other person's age:" ))
            data.append(age)
            if age <= 0:
                print( "Your age must be positive" )
            read_sdin()
        except ValueError:
            print( "That is an invalid age specification" )
            read_sdin()
        except EOFError:
            print(data)
            print( "There was an unexpected error reading input." )
            raise
    else:
        read_sdin()