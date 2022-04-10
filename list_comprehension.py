'''
You are given three integers, x, y and z representing 
the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i,j,k)
on a 3D grid where the sum of i + j + k is not equal to n.

'''

def create_list_comp(x, y, z, n):
    new_list = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k == n:
                    continue
                else:
                    new_list.append([i, j, k])
    return new_list
    

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    comp_list = create_list_comp(x, y, z, n)
    
    print(comp_list)
