'''
The provided code stub reads and integer, n, from STDIN. 
For all non-negative integers i < n, print i(2).
'''

def get_negative_square(num):
    if num % 2 is not 0:
        for i in range(0, num):
            print(i**2)

if __name__ == '__main__':
    n = int(raw_input())
    
    get_negative_square(n)