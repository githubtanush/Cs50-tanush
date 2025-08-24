from calculator import square

def main():
    test_square()

#unit test by making bug in calculator.py
'''An AssertionError is a type of error that occurs in programming
when an assert statement fails. An assert statement is used
to test a condition or assumption within the code. If the condition 
evaluates to False, then an AssertionError is raised, indicating that 
a fundamental assumption about the program's state or logic has been violated.'''

def test_square():
    try:
        assert square(2) == 4
    except AssertionError: 
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    
    try:
        assert square(-2) == 4
    except AssertionError: 
        print("-2 squared was not 4")
    
    try: 
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
    

if __name__ == "__main__":
    main()

#assert is a keyword in python
#AssertionError

#pytest is a third party programming which checking the 
#code manually by itself that is there is any bug or not
#unittest is a testing in individual unit of the programme that 
#it is correct or not