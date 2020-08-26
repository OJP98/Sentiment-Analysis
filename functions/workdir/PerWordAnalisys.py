import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

#print(test_subset.split())
def perWordAnalisys(text):
    words = text.split()
    sid = SentimentIntensityAnalyzer()
    pos, neg = 0, 0
    for word in words:
        if (sid.polarity_scores(word)['compound']) >= 0.5:
            pos+= 1
        elif (sid.polarity_scores(word)['compound']) <= -0.5:
            neg+= 1        
    return pos - neg  


#test_subset="Lots of fun in the bath but have to use a lot to make it bubble! Nice addition when the kids don't"
test_subset="Good flavor. This review was collected as part of a promotion."
print(perWordAnalisys(test_subset))