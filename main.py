import random
#print("Hello World!") #it prints the strings
#print ("print('what to print')")
#print ("Hello" + " " + "World!")
# a = input("What is your name?")
# print (a)
# print ("I am" + " " + input("HOW OLD ARE YOU"))

#print("Plese enter your name?\n")
#name = input()
#number = len(name)
#print(f"Your name consist of {number} of letters")

# a = input ()
# b = input()

# c = a
# a = b
# b = c

# print (a)
# print (b)

# city_name = input( "What is your city name?\n")
# user_name = input( "What is ypur name?\n")
# Combination = city_name + " " + user_name
# print (Combination)
# print (Combination.upper())
# print (Combination.lower())
# print (Combination.title())
# print (Combination.capitalize())
# print (Combination.swapcase())
# print (Combination.istitle())
# print (Combination.isupper())
# print (Combination.islower())
# print (Combination.isalnum())

# print("Hello"[4])
# print("Hello"[-1])

# number = 1_345_100
# print(number)
# print(type(number))

# num = input ("Write a two digit number?")
# if (int(num)<100 and int(num)>0):
#  sum = int(num[0])+int(num[1])
#  print(sum)

# weight = input("Insert your weight: ")
# height = input ("Insert your height: ")

# BMI = float(weight)/((float(height))**2)
# print (round(BMI,2))

# num = int(input ("Insert a number: "))

# if num % 2 == 0:
#   print ("The number is even")
# else:
#   print ("The number is odd")

# name1 = input ("Write his/her name, please?")
# name2 = input ("Write your name, please?")
# counterT = 0
# counterL = 0
# true = "True"
# love = "Love"

# for i in range (len(true)):
#  for j in range (len(name1)):
#   if name1[j] == true[i]:
#     counterT+=1
#   if name1[j] == love[i]:
#       counterL+=1
  
#  for k in range (len(name2)):
#    if name2[k] == love[i]:
#     counterL+=1
#    if name2[k] == true[i]:
#      counterT+=1

# percentage = int(str(counterT)  + str(counterL))

# if percentage < 10 or percentage > 90:
#   print (f"Your love score is {percentage}%")
# else:
#   print (f"Your love score is {percentage}%. You go together like coke and mentos")

# name2 = input ("Write your name, please?")
# name1 = name2.lower()
# l = name1.count("l")
# print(l)

# states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas"]
# states_of_america.append("Yeraland")
# print (states_of_america)

# names_string = input()
# names = names_string.split(", ")
# print(names) 
# print(len(names))
# ran_val = random.randint(0, len(names)-1)
# print (ran_val)
# print(names[ran_val])

# fruits = ["aa" , "bb" ]
# vegetables = ["cc" , "dd" ]
# mix = [fruits, vegetables]
# print (mix[0])
# print (mix[1])
# print (mix[0] [1])
# print (mix[1] [1])

# students_scores = input ().split()
# for n in range (0, len(students_scores)):
#   students_scores[n] = int(students_scores[n])
# maxi = 0
# for i in students_scores:
#   if maxi < i:
#      maxi =i
# print(maxi)

# number  = int(input())
# num = 0
# for i in range(2,number+1,2):
#   num += i
#   print(num)


# # Hardcoded list of all letters (both lowercase and uppercase)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# nr_letters = int(input("How many letters do you want?"))
# nr_symbols = int(input("How many symbols do you want?"))
# nr_numbers = int(input("How many numbers do you want?"))

# mix_list = [alphabet,symbols,numbers]
# #mix_list1 = [nr_letters,nr_symbols,nr_numbers]
# password = []
# counterL = 0
# counterS = 0
# counterN = 0
# # maxi = 0
# # for i in mix_list1:
# #   if maxi < i:
# #      maxi =i
# # print(maxi)

# for i in range (nr_letters+nr_symbols+nr_numbers):
  
#   if counterS==nr_symbols and counterN==nr_numbers:
#     a=0
#   elif  counterN==nr_numbers:
#     a = random.randint(0,1)
#   elif counterS==nr_symbols:
#     new_list = [0,2]
#     a = random.choice(new_list)
#   elif counterL==nr_letters:
#     a = random.randint(1,2)
#   elif counterS<nr_symbols or counterN<nr_numbers or counterL<nr_letters: 
#     a = random.randint(0,2) 
    
#   if a == 0 and counterL<=nr_letters:
#     b = random.randint(0,len(alphabet)-1)
#     password.append(mix_list[a][b])
#     counterL+=1
#   elif a == 1 and counterS<=nr_symbols:
#     c = random.randint(0,len(symbols)-1)
#     password.append(mix_list[a][c])
#     counterS+=1
#   elif a == 2 and counterN<=nr_numbers:
#     d = random.randint(0,len(numbers)-1)
#     password.append(mix_list[a][d])
#     counterN+=1

# password1 = "".join(password)
# print(password1)
  


# Generate the password

# for i in range(nr_letters):
#     password.append(random.choice(alphabet))
# for i in range(nr_symbols):
#     password.append(random.choice(symbols))
# for i in range(nr_numbers):
#     password.append(random.choice(numbers))


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(start_text, shift_amount):
#   encrypted_text = ""
#   for char in start_text:
#     if char in alphabet:
#       position = alphabet.index(char)
#       shifted_position = (position + shift_amount)
#       if position + shift_amount > len(alphabet)-1:
#          shifted_position = (position + shift_amount) - (len(alphabet))
#       elif position + shift_amount <= len(alphabet)-1:
#         shifted_position = (position + shift_amount)
#       encrypted_text += alphabet[shifted_position]
#     else:
#         encrypted_text += char
#   print(f"Here's your message: {encrypted_text}")
      
# def decrypt(start_text, shift_amount):
#   encrypt(start_text, -shift_amount)


# def cipher (start_text, shift_amount, cipher_direction):
#   if direction == "encode":
#     encrypt(start_text, shift_amount)
#   elif direction == "decode":
#     decrypt(start_text, shift_amount)
#   else:
#     print("Wrong input")


  
# # def encrypt(text, shift):
# #   encrypted_text = ""
# #   for char in text:
# #       if char in alphabet:
# #           position = alphabet.index(char)
# #           shifted_position = (position + shift) % len(alphabet)
# #           encrypted_text += alphabet[shifted_position]
# #       else:
# #           encrypted_text += char  # Keep non-alphabetic characters unchanged
# #   return encrypted_text


# counter = True
# while counter:
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))
#   shift = shift%26
#   cipher(start_text=text, shift_amount=shift, cipher_direction=direction)
#   ask_again = input ("Do you want to try again? (y/n)\n").lower()
#   if ask_again == "n" or ask_again == "no":
#     counter = False
#     print("Bye")
#   elif ask_again == "y" or ask_again == "yes":
#     counter = True
#   else:
#     print("Wrong input")
#     counter = False

# def max_bid (bid_dict):
#   maxi = 0
#   max_key = ""
#   for bidder in bid_dict:
#     bid_amount = bid_dict[bidder]
#     if bid_dict[bidder] > maxi:
#       maxi = bid_dict[bidder]
#       max_key = bidder
#   print (f"The winner is {max_key} with a bid of {maxi}")

# dict = {}
# counter = True
# while counter:
#   name = input("Type the name of the bidder:\n")
#   bid = int(input("Type the bid:\n"))
#   dict[name] = bid
#   ask_again = input ("Do you want to add another bidder? (y/n)\n").lower()
#   if ask_again == "n" or ask_again == "no":
#     counter = False
#     max_bid(dict)
#     print("Bye")
#   elif ask_again == "y" or ask_again == "yes":
#     counter = True
#   else:
#     print("Wrong input")
#     counter = False


#from replit import clear
# def max_bid(bid_dict):
#   # Function to find and print the bidder with the highest bid
#   maxi = 0
#   max_key = ""
#   for bidder in bid_dict:
#       bid_amount = bid_dict[bidder]
#       if bid_amount > maxi:
#           maxi = bid_amount
#           max_key = bidder
#   print(f"The winner is {max_key} with a bid of {maxi}")

# bid_dict = {}
# counter = True

# while counter:
#   print("Inside the loop") 
#   name = input("Type the name of the bidder:\n")
#   bid = int(input("Type the bid:\n"))
#   bid_dict[name] = bid

#   ask_again = input("Do you want to add another bidder? (y/n)\n").lower()
#   if ask_again in ["n", "no"]:
#       counter = False
#       max_bid(bid_dict)
#       print("Bye")
  # elif ask_again in ["y", "yes"]:
  #     clear()
  # else:
  #     print("Wrong input")
  #     counter = False

# def format (fname, lname):
#   formated_f = fname.title()
#   formated_l = lname.title()
#   return f"{formated_f} {formated_l}"

# print(format(input()))


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def another_card(ans):
    get_card = input(f"Do you want another card? (y/n)\n").lower()
    if get_card == "y" or get_card == "yes":
        card = random.choice(cards)
        ans.append(card)
        return ans
    else:
        return ans

def calculate_score(user_cards):
    score = 0
    if 11 in user_cards and sum(user_cards) > 21:
        user_cards.remove(11)
        user_cards.append(1)
    score += sum(user_cards)
    return score

start_game = input("Do you want to play a game? (y/n)\n").lower()
if start_game == "y" or start_game == "yes":
    print("Let's play a game")
    your_cards = []
    dealer_cards = []
    for i in range(2):
        card = random.choice(cards)
        your_cards.append(card)
        card = random.choice(cards)
        dealer_cards.append(card)
    print(f"Your cards: {your_cards}")
    rand_deal = random.choice(dealer_cards)
    print(f"Dealer's card: {rand_deal}")

    your_cards = another_card(ans=your_cards)
    print(f"Your cards: {your_cards}")

    while sum(dealer_cards) < 17:
        new_card = random.choice(cards)
        dealer_cards.append(new_card)

    print(f"Dealer's cards: {dealer_cards}")

    your_score = calculate_score(user_cards=your_cards)
    dealer_score = calculate_score(user_cards=dealer_cards)

    print(f"Your score: {your_score}")
    print(f"Dealer's score: {dealer_score}")

    if your_score == 21 and dealer_score == 21:
        print("It's a tie!")
    elif dealer_score == 21:
        print("Dealer has Blackjack! You lose!")
    elif your_score == 21:
        print("You have Blackjack! You win!")
    elif your_score > 21:
        print("You busted! You lose!")
    elif dealer_score > 21:
        print("Dealer busted! You win!")
    elif dealer_score == your_score:
        print("It's a tie!")
    elif dealer_score > your_score:
        print("Dealer wins!")
    else:
        print("You win!")

else:
    print("Bye")
