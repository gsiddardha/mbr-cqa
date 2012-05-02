C: 100
C++: 80
CSHARP: 30

    
fd    # answer counts - overall and local. - do it in a loop
kvk   # weights to different tags - manually construct the weights and give score based on these weights
fd    # score for the answers - get all scores and then sum them up for a user
kvk   # user reputation and acceptance rate - get from the site.
    
kvk   # then give different weights to each of the above factors and build a profile
kvk   # change the score depending on the number of questions suggested to that user (cooling rate?)
kvk   # diversity in recommendation ?? 
fd    # complexity of question. ranking the question and recommending tough ones to expert and easy ones to novice
