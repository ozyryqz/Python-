score = float ( input ("Please input a score:") )
print ( score)
if  (score > 100 and score < 0) :
    print ("The score is invalid")
elif  score < 0:
    print ("The score is invalid")
elif score > 90:
    print ("A")
elif score > 80:
    print ("B")
elif score > 70:
    print ("C")
elif score >60:
    print ("D")
elif score < 60:
    print ("Disqualified")
