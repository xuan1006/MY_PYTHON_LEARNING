def adjust_scores(scores):
    index = 0
    for score in scores:
        scores[index]= (score+20 if score<80 else 100)
        index +=1

scores = [10,40,96,77]
adjust_scores(scores)
print(scores)