import string
import random

#create lists for randomization, also asking for user input after
s1 = list(string.ascii_uppercase)
s2 = list(string.ascii_lowercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

user_input = input("How many charecters do you want inside your password?: ")

#check if input is more than 8
while True:
    try:
        characters = int(user_input)
        if characters < 8:
            print("your password should be longer than 8 characters so that it is more secure")
            user_input = input("please enter a new number greater than 8")
        else:
            break
    except:
        print("please enter whole numbers only")
        user_input = input("how many characters do you want in your password? ")

#Shuffle the lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

#getting 30 and 20 percent of the character length so that you can create a range to generate from
part1 = round(characters * (30/100))
part2 = round(characters * (20/100))
part3 = characters - part1 - part2 #gets remaining to add to end of len(result)


part1 = min(part1, len(s1), len(s2))
part2 = min(part2, len(s3), len(s4))
part3 = min(part3, len(s1), len(s2), len(s3), len(s4))

#generation of password 60/40
result = []
#randomizing the result by appending it with elements from each of the ranges and lists
for x in range(part1):
    result.append(s1[x % len(s1)])
    result.append(s2[x % len(s2)])
for x in range(part2):
    result.append(s3[x % len(s3)])
    result.append(s4[x % len(s4)])

if len(result) < characters:
    remaining = characters - len(result)
    all_chars = s1 + s2 + s3 + s4
    result.extend(random.sample(all_chars, remaining))

#shuffle the result
random.shuffle(result)

#join result
password = "".join(result)
print("Your Strong password is: ", password)
#ask for personalization
final_q = input("Does this email meet your requirements (y/n): ")
if final_q.lower() == 'n':
    fix = input("What are some hidden words we can place in your password to make it more secure to you: ")

        def pass_fix(password, fix):
        position = random.randint(0, len(password))
        new_pass = password[:position] + fix + password[position:]
        return new_pass

    # Assuming 'password' is defined somewhere before this
    password = "ExampleRandom123"  # Placeholder
    print("Your Strong password is:", pass_fix(password, fix))
else:
    pass