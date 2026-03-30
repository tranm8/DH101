import string
def removeDigits(text):
'''
Parameter: text, a string that might contain digits
Returns: a string that contains the same characters as text with all digits
removed
'''
result = ""
for character in text:
if not character in "1234567890":
result = result + character
return result
    
