import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import gensim
from gensim.summarization import summarize
#import unicodedata as ud
#from unidecode import unidecode


#def remove_non_ascii(text):
#    return unidecode(unicode(text, encoding = "utf-8"))

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


lines = [line.rstrip('\n') for line in open('content.txt')]

print lines

text = "Last year the average American spent more than 290 hours behind the wheel of a car – that’s roughly equivalent to seven 40-hour weeks – according to a report published by the AAA Foundation. When you expand that globally, the amount of time we spend driving is staggering. That’s why automakers like Renault-Nissan, Volvo, BMW and Toyota are embracing the Internet of Things (IoT) to provide new ways to help drivers stay safe, connected and productive during their time on the road.By 2020, 90 percent of new cars will have connectivity capabilities1 and Microsoft is helping the automotive industry drive this transformation. Today at the Consumer Electronics show in Las Vegas, we announced the Microsoft Connected Vehicle Platform, an offering built on the powerful Microsoft Azure cloud. It brings Microsoft’s intelligent services in virtual assistants, business applications, office services, visual analytics and productivity tools to the car, to reduce driver distractions and help drivers be even more mobile.In her post on the Official Microsoft Blog, Peggy Johnson, executive vice president of business development, shared more about how Microsoft is helping auto makers, tier-one suppliers and the entire automotive ecosystem revolutionize their businesses while supporting better driving experiences for customers.No other manufacturing industry has done more to embrace the value of partnerships in delivering great products and customer experiences than the automotive industry. Likewise, in the software industry, Microsoft has the heritage and longstanding approach to partnerships and ecosystems that make us a trusted technology partner with many organizations world-wide."

   
#print 'Input text:'
#print text

#text = remove_non_ascii(text)

#text = replace_trash(text)

#text = strip_non_ascii(text )

print 'Summary:'
print summarize(lines)