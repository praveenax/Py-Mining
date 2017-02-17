import prx

def find_max (L):
    max = 0
    for x in L:
        if x > max:
            max = x
    return max

arr = [12,32,34,2]

prx.calc_time(find_max,arr)

    

