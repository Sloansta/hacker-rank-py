'''
Example: n = 5
print the string 12345
'''

def get_consec(num):
    arr = []
    new_str = ""
    for i in range(1, num+1):
        arr.append(str(i))
    new_str = new_str.join(arr)
    print(new_str)
    
if __name__ == '__main__':
    n = int(raw_input())
    get_consec(n)