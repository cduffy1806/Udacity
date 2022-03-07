## Scripting Exercise 1
# names =  input('Enter names separated by commas: ').title().split(',')
# assignments =  input('Enter assignment counts separated by commas: ').split(',')
# grades =  input('Enter grades separated by commas: ').split(',')
#
# # message string to be used for each student
# # HINT: use .format() with this string in your for loop
# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"
#
# # write a for loop that iterates through each set of names, assignments, and grades to print each student's message
# for name, assignment, grade in zip(names,assignments,grades):
#     print(message.format(name,assignment, grade, int(grade) + int(assignment)*2))
#
# #--------------------------------------------------------------------------------#
## Scripting Exercise 2
# def party_planner(cookies, people):
#     leftovers = None
#     num_each = None
#     # TODO: Add a try-except block here to
#     #       make sure no ZeroDivisionError occurs.
#     try:
#         num_each = cookies // people
#         leftovers = cookies % people
#     except ZeroDivisionError:
#         print('Oops, you entered 0 people will be attending!')
#         print('Please enter a good number of people for a party')
#
#     return(num_each, leftovers)
#
# # The main code block is below; do not edit this
# lets_party = 'y'
# while lets_party == 'y':
#
#     cookies = int(input("How many cookies are you baking? "))
#     people = int(input("How many people are attending? "))
#
#     cookies_each, leftovers = party_planner(cookies, people)
#
#     if cookies_each:  # if cookies_each is not None
#         message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
#         print(message.format(people, cookies_each, leftovers))
#
#     lets_party = input("\nWould you like to party more? (y or n) ")
# #--------------------------------------------------------------------------------#
## Scripting Exercise 3
# def create_cast_list(filename):
#     cast_list = []
#     #use with to open the file filename
#     #use the for loop syntax to process each line
#     #and add the actor name to cast_list
#     with open(filename) as f:
#         for line in f:
#             cast_list.append(line.strip().split(',')[0])
#     return cast_list
#
# cast_list = create_cast_list('flying_circus_cast.txt')
# for actor in cast_list:
#     print(actor
# #--------------------------------------------------------------------------------#
## Scripting Exercise 4

# #initiate empty list to hold user input and sum value of zero
# user_list = []
# list_sum = 0
#
# # seek user input for ten numbers
# for i in range(10):
#     userInput = int(input("Enter any 2-digit number: "))
#
# # check to see if number is even and if yes, add to list_sum
# # print incorrect value warning  when ValueError exception occurs
#     try:
#         number = userInput
#         user_list.append(number)
#         if number % 2 == 0:
#             list_sum += number
#     except ValueError:
#         print("Incorrect value. That's not an int!")
#
# print("user_list: {}".format(user_list))
# print("The sum of the even numbers in user_list is: {}.".format(list_sum))
# #--------------------------------------------------------------------------------#
## Scripting Exercise 5
# # TODO: First import the `random` module
# import random
#
# # We begin with an empty `word_list`
# word_file = "words.txt"
# word_list = []
#
# # We fill up the word_list from the `words.txt` file
# with open(word_file,'r') as words:
# 	for line in words:
# 		# remove white space and make everything lowercase
# 		word = line.strip().lower()
# 		# don't include words that are too long or too short
# 		if 3 < len(word) < 8:
# 			word_list.append(word)
#
# # print(word_list)
#
# # TODO: Add your function generate_password below
# # It should return a string consisting of three random words
# # concatenated together without spaces
# def generate_password():
#     password=''
#     for i in range(3):
#         password += random.choice(word_list)
#     return password
#
# # Now we test the function
# print(generate_password())

# #--------------------------------------------------------------------------------#
## Scripting Exercise 6
# Write your code here

# HINT: create a dictionary from flowers.txt
flowers = {}
with open('flowers.txt') as f:
    for line in f:
        key,value = line.strip().split(': ')
        flowers[key] = value
# print(flowers)

# HINT: create a function to ask for user's first and last name
def flower_name():
    first_name,last_name=input('Enter your First name [space] Last name only:').split(' ')
    flower = flowers[first_name[0].upper()]
    return print('Unique flower name with the first letter:{}'.format(flower))

# print the desired output
flower_name()
