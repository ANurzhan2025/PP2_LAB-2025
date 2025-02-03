# 1
# The function for changing grams to ounces 
def to_ounces(grams): 
    ounces = grams / 28.3496231 
    return ounces 
 
grams = int(input("Enter the weight in grams: ")) 
 
print(to_ounces(grams), "ounces")
# 2  
fahrenheit = float(input("Enter temperature in Fahrenheit: "))  
  
celsius = (5 / 9) * (fahrenheit - 32)  
  
print("Temperature in Celsius:", celsius)


# 3
def solve(heads, legs): 
    # total = 35 
 
    # 2x + 4y = 94 
    # x + y = 35 
 
    # 2x + 4y = 94 
    # 2x + 2y = 70 
 
    # 2y = 24 
    # y = 12 
    # x = 23 
     
    # Calculate the number of rabbits 
    numrabbits = int((legs - (2 * heads)) / 2) 
     
    # Calculate the number of chickens by subtracting the number of rabbits from total heads 
    numchickens = int(heads - numrabbits) 
 
    print("Rabbits:", numrabbits) 
    print("Chickens:", numchickens) 
     
 
heads = int(input("Enter the amount of heads: ")) 
legs = int(input("Enter the amount of legs: ")) 
solve(heads, legs) 


# 4  
# function that checks if the number prime or not  
def is_prime(n):  
    if n < 2:  
        return False  
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  
  
def filter_prime(numbers):  
    return [num for num in numbers if is_prime(num)]  
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))  
print("Prime numbers:", filter_prime(numbers))  
 

# 5  
# function for permutating of a word 
def permute(s, answer=""):  
    if len(s) == 0:  
        print(answer)  
        return  
  
    for i in range(len(s)):  
        char = s[i]  
        remaining = s[:i] + s[i+1:]  
        permute(remaining, answer + char)  
  
k = input("Enter a string: ")  
print("All permutations:")  
permute(k)



# 6  
# function that revers the sentence 
def reverse_sentence(sentence):  
    words = sentence.split()  
    reversed_words = words[::-1]  
    return " ".join(reversed_words)  
  
  
k = input("Enter a sentence: ")  
print(reverse_sentence(k)) 


# 7
def has_33(nums): 
    for i in range(len(nums) - 1): 
        if nums[i] == 3 and nums[i + 1] == 3: 
            return True 
    return False 
 
print(has_33([1, 3, 3]))      
print(has_33([1, 3, 1, 3]))   
print(has_33([3, 1, 3]))



# 8
def spy_game(nums): 
    for i in range(len(nums) - 2): 
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7: 
            return True 
    return False 
spy_game([1,2,4,0,0,7,5]) # True 
spy_game([1,0,2,4,0,5,7]) # True 
spy_game([1,7,2,0,4,5,0]) # False


# 9
import math 
def volume(radius): 
    return (4/3) * math.pi * pow(radius, 3) 
 
r = int(input('Enter the radius: ')) 
print(volume(r))
# 10
def unique_list(list1): 
    list2 = [] 
    for i in list1: 
        if i not in list2: 
            list2.append(i) 
    return list2 
 
numbers = list(map(int, input("Enter numbers separated by space: ").split())) 
print("Unique elements:", unique_list(numbers)) 


# 11
# A function for palindrome 
def palindrome(text): 
    if text == text[::-1]: 
        return True 
    else: 
        return False 
     
text = input('Enter string: ') 
print(palindrome(text))


# 12 
def histogram(lst): 
    for num in lst: 
        print('*' * num) 
numbers = list(map(int, input("Enter numbers separated by space: ").split())) 
histogram(numbers)


# 13
from random import randint 
 
def guess(): 
    name = input('Hello! What is your name? ') 
    print("Well, " + name + ', I am thinking of a number between 1 and 20.') 
 
    num = randint(1, 20) 
    cnt = 0 
     
    while(True): 
        print("Take a guess.") 
        guessed_num = int(input()) 
        cnt += 1 
         
        if guessed_num < num: 
            print("Your guess is too low.") 
        elif guessed_num > num: 
            print("Your guess is too high.") 
        else: 
            print("Good job, " + name + "! You guessed my number in " + str(cnt) + " guesses") 
            break 
 
guess()