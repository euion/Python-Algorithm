count = int(input())

for i in range(count):
    ox_list = list(input())
    score = 0
    total_score = 0
    for j in ox_list:
        if j =="O":
            score +=1
            total_score +=score
        else:
            score = 0
    print(total_score)
