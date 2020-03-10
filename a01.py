
def question_first_solution(input_seq,test):
    out_str = ''
    for i in range(len(test)):
        key = test[i]
        count = 0
        if test[i] == test[i-1]:
            continue
        for j in range(len(test)):
            if j>=i and (j-i) < 4 and test[j] == test[i]:
                count += 1
    #     print(key)
    #     print(count-1)
    #     print(num_dict[int(key)][count-1])
        out_str = out_str + input_seq[int(key)][count-1]
    print(out_str)  
    
test = '9999335533'

input_seq = {2 : ['a', 'b', 'c'], 
            3 : ['d', 'e', 'f'],
            4 : ['g', 'h', 'i'],
            5 : ['j', 'k', 'l'],
            6 : ['m', 'n', 'o'],
            7 : ['p', 'q', 'r', 's'],
            8 : ['t', 'u', 'v'],
            9 : ['w', 'x', 'y', 'z']}  

question_first_solution(input_seq,test)

def question_second_solution(tickets):
    seq = {}
    sources = set(tickets.keys())
    destinations = set(tickets.values())
    
    source = list(sources.difference(destinations))[0]
    
    for i in range(len(tickets)):
        seq[source] = tickets[source]
        source = tickets[source]
    return seq

tickets = {"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"}
print("Travel Sequence :",question_second_solution(tickets))


def question_third_solution(states):
    cities = {}
    
    for state,cities1 in states.items():
        for city in cities1:
            if city not in cities:
                cities[city] = [state]
            else:
                cities[city].append(state)
    return cities

states = {'New Hampshire': ['Concord', 'Hanover'],'Massachusetts': ['Boston', 'Concord', 'Springfield'],'Illinois': ['Chicago', 'Springfield', 'Peoria'] }
print("Output :",question_third_solution(states))

def question_fourth_solution(brackets):
    bracket_seq = {"(": ")", "[": "]",  "{": "}"}
    brackets1 = ['(','[','{']
    a = []
    for i in brackets:
        if i in brackets1:
            a.append(i)
        elif a and i == bracket_seq[a[-1]]:
                a.pop()
        else:
            return False
    return a == []

brackets = '()}[]{'
print(question_fourth_solution(brackets))

def question_fifth_solution(number):
    roman = {1: 'I', 4: 'IV', 5:'V', 9: 'IX',
    10: 'X', 40: 'XL', 50: 'L', 90:'XC',
    100: 'C', 400:'CD', 500: 'D', 900:'CM',
    1000:'M'
    }
    
    highest_decimal = sorted(roman.keys(),reverse= True)
    print(highest_decimal)
    if number>=4000:
        return False
    r='' 
    
    index = 0
    while number:
        div = number // highest_decimal[index]
        number %= highest_decimal[index]
        while div: 
            r+=roman[highest_decimal[index]]
            div -= 1
        index += 1
    return r

number=100
print(question_fifth_solution(number))

import re
def question_sixth_solution(code):
    lines = code.split("\n")
    not_comment = re.compile("^[^#]")
    line_count = 0
    for line in lines:
        if line != '' and re.search(not_comment,line.strip()):
            line_count += 1
    return line_count

print("No. of lines of Python Code :",question_sixth_solution(code))

def question_seventh_solution(string):
    reasons = []

    if len(string) < 8:
        reasons.append("The length of the password must be at least 8 characters in length")

    if not re.search("[A-Z]",string):
        reasons.append("The password must contain at least 1 capital letter")
    
    if not re.search("[0-9]",string):
        reasons.append("The password must contain at least 1 digit")

    if re.search("\W",string):
        if re.search("[^!@#$&\w]",string):

            reasons.append("The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)")
    else:
        reasons.append("The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)")

    if reasons:
        return ("Weak", reasons)
    else:
        return ("Strong", []) 


print(question_seventh_solution("aBcD**#&"))

def question_eighth_solution(string):
    reasons = []

    if not string[0].isupper():
        reasons.append("Sentence must start with an Uppercase character.")

    if ' ' not in string:
        reasons.append("Spaces must be present between words in a sentence.")

    if '.' != string[-1] or re.search("\..+",string):
        reasons.append("Sentence must end with a full-stop.")

    if '  ' in string:
        reasons.append("Continuous spaces are not allowed.")
        
    if re.search("[A-Z][A-Z]",string):
        reasons.append("Continuous uppercase characters are not allowed.")    

    if reasons:
        return (False, reasons)
    else:
        return (True, ["Your sentence is syntactically correct!"])


print(question_eighth_solution("An important part of my life has been the people who stood by me.."))

def question_ninth_solution(arr, k):
    all_sub_array = []
    
    for i in range(0, len(arr)-k+1):
        all_sub_array.append(arr[i:i+k])
        
    max_sub_array = sorted(all_sub_array)[-1]    
    return max_sub_array

arr = [1,4,5,5,3,1,5]
k = 4
print(question_ninth_solution(arr, k))

def question_tenth_solution(nums):
    even_nums = []
    odd_nums = []
    for value in nums:
        if value % 2 ==0:
            even_nums.append(value)
        else:
            odd_nums.append(value)
    if len(even_nums) <= len(odd_nums):
        return(len(even_nums),odd_nums)
    else:
        return(len(odd_nums),even_nums)

nums = [1,2,2,4,3]
print(question_tenth_solution(nums))