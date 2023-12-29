def is_palindrome(number):
    return str(number) == str(number)[ : : -1]

def is_lychrel(number):
    attemp = 0
    curr_num = number

    while attemp < 50:
        reversed_num = int(str(curr_num)[ : : -1])
        curr_attemp = curr_num + reversed_num

        if is_palindrome(curr_attemp) == True:
            return False
        else:
            curr_num = curr_attemp
            attemp += 1
    
    return True

def lychrel_numbers(ceil):
    count = 0

    for number in range(ceil):
        if is_lychrel(number) == True:
            count += 1
    
    return count

lychrel_numbers(10000)