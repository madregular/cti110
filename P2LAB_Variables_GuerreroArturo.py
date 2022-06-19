user_int = int(input('Enter integer (32 - 126):\n'))

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
user_float = float(input('Enter float:\n'))
user_character = input('Enter character:\n')
user_string = str(input('Enter string:\n'))

print(user_int, user_float, user_character, user_string)

# FIXME (2): Output the four values in reverse
print(user_string, user_character, user_float, user_int)  

# FIXME (3): Convert the integer to a characer, and output that character
conv_to_char = chr(user_int)
print(f"{user_int} converted to a character is {conv_to_char}")