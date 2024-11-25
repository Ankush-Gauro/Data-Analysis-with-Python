score = [56,44,36,78,92]

def percent(score_list):
    p = (score_list*100)/200
    return p

mapped_list = map(percent, score)
print(list(mapped_list))