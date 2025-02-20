#1 Matches 'a' followed by zero or more 'b'
import re

print(bool(re.fullmatch(r"ab*", "a")))      
print(bool(re.fullmatch(r"ab*", "abb")))   
print(bool(re.fullmatch(r"ab*", "ac"))) 

#2 Matches 'a' followed by exactly 2 or 3 'b'
import re

print(bool(re.fullmatch(r"ab{2,3}", "abb")))   
print(bool(re.fullmatch(r"ab{2,3}", "abbb")))  
print(bool(re.fullmatch(r"ab{2,3}", "ab")))  

#3 Matches sequences of lowercase letters connected by '_'
import re

print(bool(re.fullmatch(r"[a-z]+_[a-z]+", "hello_world"))) 
print(bool(re.fullmatch(r"[a-z]+_[a-z]+", "helloWorld")))  

#4 Matches one uppercase letter followed by lowercase letters
import re

print(bool(re.fullmatch(r"[A-Z][a-z]+", "Hello"))) 
print(bool(re.fullmatch(r"[A-Z][a-z]+", "HELLO"))) 

#5 Matches 'a' followed by any characters and ending with 'b'
import re

print(bool(re.fullmatch(r"a.*b", "a123b")))  
print(bool(re.fullmatch(r"a.*b", "aXbY")))  

#6 
import re

text = "Hello, world. How are you?"
print(re.sub(r"[ ,.]", ":", text))  

#7
def to_camel(text):
    return "".join(word.capitalize() for word in text.split("_"))

print(to_camel("hello_world")) 

#8
import re

print(re.split(r"[A-Z]", "HelloWorld"))  

#9  Adds spaces before uppercase letters
import re

print(re.sub(r"([A-Z])", r" \1", "HelloWorld").strip())  

#10  Replaces uppercase letters with '_lowercase'
import re

def to_snake(text):
    return re.sub(r'([A-Z])', r'_\1', text).lower().strip('_')

print(to_snake("HelloWorld")) 


