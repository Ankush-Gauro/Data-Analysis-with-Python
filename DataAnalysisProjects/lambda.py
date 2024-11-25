score = [56,44,36,78,92]
def score_check(score_list):
    if score_list>50:
        return True
    else:
        return False
    
passed_students = filter(score_check,score)

for i in passed_students:
    print(i)
