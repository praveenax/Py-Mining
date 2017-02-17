


for i in xrange(input()):
	n,m=map(int,raw_input().split())
    print n
    print m
	s=sorted(map(int,raw_input().split()))
    print s
	seq=list(x for x in xrange(1,n+1) if x not in s)
    print seq
	k=[str(seq[x]) for x in xrange(len(seq)) if x%2==0]
	l=[str(seq[x]) for x in xrange(len(seq)) if x%2==1]
	print " ".join(k)
	print " ".join(l) 