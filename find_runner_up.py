
'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given n scores. 
Store them in a list and find the score of the runner-up.
'''

def find_runner_up(arr):
    arr.sort()
    max_num = max(arr)
    for i in range(0, len(arr)): 
        if(arr[i+1] == max_num):
            return arr[i]
    
        

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    x = find_runner_up(arr)
    print(x)