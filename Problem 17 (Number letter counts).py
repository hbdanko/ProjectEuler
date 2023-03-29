# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# 
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

number_dict = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 
               6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten", 
               11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 
               16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen", 20 : "twenty", 
               30 : "thirty", 40 : "forty", 50 : "fifty", 60 : "sixty", 70 : "seventy",
               80 : "eighty", 90 : "ninety", 100 : "onehundred", 200 : "twohundred", 
               300 : "threehundred", 400 : "fourhundred", 500 : "fivehundred", 600 : "sixhundred", 
               700 : "sevenhundred", 800 : "eighthundred", 900 : "ninehundred", 1000 : "onethousand"}

def number_letter_converter(number):
    if number in number_dict:
        return number_dict[number]
    
    str_version = str(number)
    list_version = [int(x) for x in str(number)]
    letter_version = ""
    
    if len(list_version) == 3:
        letter_version += number_dict[list_version[0] * 100]
        if int(str_version[1:3]) in number_dict:
            letter_version += "and" + number_dict[int(str_version[1:3])]
        elif str_version[1:3] == "00":
            return letter_version
        elif str_version[2] == "0":
            letter_version += "and" + number_dict[list_version[2]]
        else:
            letter_version += "and" + number_dict[list_version[1] * 10]
            letter_version += number_dict[list_version[2]]
    else:
        letter_version += number_dict[list_version[0] * 10]
        letter_version += number_dict[list_version[1]]
    
    return letter_version


def number_letter_counts(limit):
    
    count = 0
    
    for i in range(1, limit + 1):
        count += len(number_letter_converter(i))

    return count

number_letter_counts(1000)




