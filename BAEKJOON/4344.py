count = int(input())
total = 0
stu_score = 0


for i in range(count):
    case = list(map(int, input().split()))
    stu_score = sum(case[1:])/case[0] # 평균점수
    stu_count =0
    for j in range(len(case[1:])):
        if case[j+1] > stu_score:
            stu_count +=1
        i = (stu_count / case[0]) * 100
    x = format(round(i,3),".3f")
    y = "%"
    print("%s%s" % (x,y))

# print(avg)