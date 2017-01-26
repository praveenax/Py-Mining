#with open('content.txt') as f:
#    lines = f.readlines()
#    print lines
    
lines = [line.rstrip('\n') for line in open('content.txt')]

print lines