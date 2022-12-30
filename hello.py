# message = "Hello my name is Aditya. I am Aditya"

#capitalize
# converts the first character to upper case
# print(message.capitalize())

#casefold
# converts string into lower case
# print(message.casefold())

#center
# returns a centered string
# print(message.center(100))

#count
# returns the number of times a specified value occurs in a string
# print(message.count("Aditya"))

#encode
# returns an encoded version of the string
# print(message.encode())

#endswith
# returns true if the string ends with the specified value
# print(message.endswith("Adi"))


#expandtabs
# sets the tab size of the string
# print(message.expandtabs(10))


# find
# searches the string for a specified value and returns the position of where it was found

# print(message.find("Aditya"))

#format
# formats specified values in a string 
# print(message.format(name="Aditya"))


#format_map
# formats specified values in a string
# print(message.format_map({"name": "Aditya"}))

#index
# searches the string for a specified value and returns the position of where it was found 
# print(message.index("Aditya"))

message2 = "aditya"

# isalnum
# returns True if all characters in the string are alphanumeric
# print(message.isalnum())

# isalpha
# returns True if all characters in the string are in the alphabet
# print(message2.isalpha())


# isdecimal
# returns True if all characters in the string are decimals
number = "12300"
# print(number.isdecimal())

#isdigit
# returns True if all characters in the string are digits
# print(number.isdigit())


#isidentifier
# returns True if the string is an identifier
# print(number.isidentifier())


#islower
# returns True if all characters in the string are lower case
# print(message2.islower())


#isnumeric
# returns True if all characters in the string are numeric
# print(number.isnumeric())


#isprintable
# returns True if all characters in the string are printable
# print(message.isprintable())

message = "Hello my name is aditya. I am aditya"
# title = "Heading"
upper = "HELLO"
#isspace
# returns True if all characters in the string are whitespaces
# print(message.isspace())

#istitle
# returns True if the string follows the rules of a title
# print(title.istitle())

#isupper
# returns True if all characters in the string are upper case
# print(upper.isupper())

# listOfWords = ["Hi", "I", "Am", "Aditya"]
# #join
# # joins the elements of an iterable to the end of the string
# print("-".join(listOfWords))

#ljust
# returns a left justified version of the string
# print(message.ljust(100, "A"))

#lower
# returns a string in lower case
name = "ADITYA"
# print(name)

# #lstrip
# # returns a left trim version of the string
# print(name.rstrip() + "Adi")


#maketrans
# returns a translation table to be used in translations
# table = name.maketrans("A", "M")
# print(table)

# print(name.translate(table))

#partition
# returns a tuple where the string is parted into three parts
# print(message.partition("my"))

#replace
# returns a string where a specified value is replaced with a specified value
# replacedString = message.replace("aditya", "Adi")
# print(replacedString)


#rfind
# returns the last index of the specified value
# print(message.rfind("aditya"))

#rindex
# returns the last index of the specified value
# print(message.rindex("aditya"))

#rjust
# returns a right justified version of the string
# print(message.rjust(50,"A"))


#rpartition
# returns a tuple where the string is parted into three parts
# print(message.rpartition("my"))


#rsplit
# splits the string at the specified separator, and returns a list
# print(message.rsplit(" "))

#rstrip
# returns a right trim version of the string

#split
# returns a list where the string has been split at the specified separator
# print(message.split("my"))


message3 = "I am Aditya."
#splitlines
# returns a list where the string has been split at line breaks
# print(message3.splitlines())

#startswith
# returns true if the string starts with the specified value
# print(message3.startswith("I am adi."))

#strip
# returns a trimmed version of the string
# message4 = "   I am adi    "
# print(message4.strip())

#swapcase
# returns a string where all the upper case letters are lower case and vice versa
# print(message3.swapcase())

#title
# returns a string where the first character in every word is upper case

# print(message3.title())

#translate
# returns a translated string

#upper
# returns a string where all the lower case letters are upper case
message4 = "I am aditya"
print(message4.upper())

#zfill
# returns a filled string with zeros on the left
print(message4.zfill(50))