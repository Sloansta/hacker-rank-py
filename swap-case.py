'''
You are given a string and your task is to swap cases. In other words, 
convert all lowercase letters to uppercase letters and vice versa.

'''

def swap_case(s):
    str_arr = list(s)
    
    for i, c in enumerate(s):
        if c.isupper():
            str_arr[i] = c.lower()
        elif c.islower():
            str_arr[i] = c.upper()
            
    new_str = "".join(str_arr)
    return new_str

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print(result)