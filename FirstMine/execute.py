import gzip
import pickle
import matplotlib.cm as cm
import matplotlib.pyplot as plt


with gzip.open('mnist.pkl.gz', 'rb') as f:
    train_set, valid_set, test_set = pickle.load(f)
    
    
    train_x, train_y = train_set
    
    print len(train_x[0])
    
#    for l in range(len(train_x)):
    
    for l in range(0,len(train_x)):
#        print l
        plt.imshow(train_x[l].reshape((28, 28)), cmap=cm.Greys_r)
#        plt.show()
        s = "imgs/foo_"+str(l)+".png"
#        s=s.join(str(l))
#        s=s.join(".png")
        print s
        plt.savefig(s)
    
#    plt.imshow(train_x[0].reshape((28, 28)), cmap=cm.Greys_r)
#    plt.show()
#    save the pic
#    plt.savefig('foo.png')
