num = int(input())

count =0
new_list = []
for i in range(num):
    word_list = input()
    for j in range(len(word_list)-1):
        if word_list[j] != word_list[j+1]:
            new_word = word_list[j+1:]
            if word_list[j] in new_word:
                count -=1
                break
    count +=1



print(count)


