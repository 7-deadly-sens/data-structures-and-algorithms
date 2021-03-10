"""
A string may encode an integer (e.g. "123" encodes 123).

Implement an integer to string conversion function and string to integer conversion function (should be able to handle negative values). 
Do not use library functions like int in python.

"""

# Similar source: https://leetcode.com/problems/string-to-integer-atoi/ 

def integer_to_string(num):
    """
    Convert number to string: 
    Cases to consider:
    1. Zero
    2. Negative Number
    3. Decimals

    Algorithm:
    Keep dividing integer by 10, keep modulus/remainder as the value 

    Time Complexity: O(N) where N is the length (number of digits) of num. 2N (1 for while loop and then reverse)
    Space Complexity: O(N) since temp_ans is size of N and so is the final return string value, N
    """

    temp_ans = []

    if (num == 0):
        return("0")
    elif(num < 0):
        temp_ans.append('-')
        num = -num
    
    while(num > 0):
        curr_dig = num % 10 
        temp_ans.append(curr_dig)
        num = num // 10
    
    return(''.join(temp_ans[::-1]))


def string_to_integer(s):
    """
    Convert a string to an integer

    Approach go backward from right to left. Consider cases: "0", "-123" and "123"
    Or we can go in normal order from left to right.
    """
    if (len(s) == 1 and s[0] == "0"): return(0)

    ans = 0
    total_len = len(s) - 1
    place = 0
    if (s[0] == "-"):       # Negative value
        for ind in range(total_len, 0, -1):
            digit = ord(s[ind]) - ord('0')
            ans += digit * (10 ** place)
            place += 1
        return(-1 * ans)
    else:                   # Positive value
        for ind in range(total_len, -1, -1):
            digit = ord(s[ind]) - ord('0')
            ans += digit * (10 ** place)
            place += 1
        return(ans)

def string_to_integer_left_to_right(s):
    if (len(s) == 1 and s[0] == "0"): return(0)

    ans, place, neg_flag = 0, len(s) - 1, False
    for ind, digit_string in enumerate(s):
        if (ind == 0 and s[ind] == "-"):
            neg_flag = True
        else:
            num_val = ord(digit_string) - ord('0')
            ans += num_val * (10 ** place)
        place -= 1
    return(ans)

