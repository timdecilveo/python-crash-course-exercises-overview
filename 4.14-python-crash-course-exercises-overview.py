print(f"1. What is 7 to the power of 4?")
print(f"7 to the power of 4 is: {7 **4}")
print(f"----------------------------------------")

print("2. Split this string: s = 'Hi there Sam!' into a list.")
s = 'Hi there Sam!'
print(list(s.split()))
print(f"----------------------------------------")

print("3. Given the variables:")
print("planet = 'Earth'")
print("diameter = 12742")
print("Use .format() to print the following string: The diameter of Earth is 12742 kilometers.")

planet = 'Earth'
diameter = 12742
print(f"The diameter of {planet} is {diameter} kilometers.")
print(f"----------------------------------------")

print(f"4. Given this nested list, use indexing to grab the word 'hello'")
print(f"lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]")
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(f"{lst[3][1][2][0]}")
print(f"----------------------------------------")


print(f"5. Given this nested dictionary grab the word 'hello'. Be prepared, this will be annoying/tricky")
print("d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}")
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(f"{d['k1'][3]['tricky'][3]['target'][3]}")
print(f"----------------------------------------")


print(f"6. What is the main difference between a tuple and a list?")
print("a Tuple is immutable, but a list is not.")
print(f"----------------------------------------")


print(f"7. Create a function that grabs the email website domain from a string in the form: user@domain.com")
print(f"So for example, passing 'user@domain.com' would return: domain.com")

list_domain = ['user@domain.com']
def func_one(email):
    return email.split('@')[-1]
print(func_one('user@domain.com'))
print(f"----------------------------------------")


print(f"8. Create a basic function that returns True if the word 'dog' is contained in the input string.")
print(f"Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.")

def findDog(dog):
    return 'dog' in dog.lower().split()
print(findDog('Is there a dog here?'))
print(f"----------------------------------------")

print(f"9. Create a function that counts the number of times the word 'dog' occurs in a string. Again ignore edge cases.")
def countDog(dog):
    return dog.count('dog')
print(countDog('This dog runs faster than the other dog dude!'))
print(f"----------------------------------------")


print(f"10. Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:")
print(f"seq = ['soup','dog','salad','cat','great']")
print(f"should be filtered down to: ['soup','salad']")

seq = ['soup','dog','salad','cat','great']
filtered_list = list(filter(lambda word: word[0]=='s', seq))
print(filtered_list)

print(f"----------------------------------------")
"""
You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results:
"No ticket", "Small ticket", or "Big Ticket".
    If your speed is 60 or less, the result is "No Ticket".
If speed is between 61 and 80 inclusive, the result is "Small Ticket".
If speed is 81 or more, the result is "Big Ticket".
Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.
"""
def caught_speeding(speed, is_birthday):
    low_speed = 60
    med_speed = 61
    high_speed = 80
    if speed <= low_speed and is_birthday == False:
        return 'No Ticket'
    elif speed >= med_speed and speed <= high_speed and is_birthday == False:
        return 'Small Ticket'
    elif speed <= (low_speed + 5) and is_birthday == True:
        return 'No Ticket'
    elif speed >= (med_speed + 5) and speed <= (high_speed + 5) and is_birthday == True:
        return 'Small Ticket'
    else:
        return 'Big Ticket'
    pass
print(caught_speeding(81,True))
print(caught_speeding(81,False))