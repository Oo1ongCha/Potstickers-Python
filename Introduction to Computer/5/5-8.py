q=("桃花塢裡桃花庵，桃花庵下桃花仙。"
"桃花仙人種桃樹，又摘桃花換酒錢。"
"酒醒只在花前坐，酒醉還來花下眠。"
"半醉半醒日復日，花落花開年復年。"
"但願老死花酒間，不願鞠躬車馬前。"
"車塵馬足顯者事，酒盞花枝隱士緣。"
"若將顯者比隱士，一在平地一在天。"
"若將花酒比車馬，彼何碌碌我何閒。"
"別人笑我太瘋癲，我笑他人看不穿。"
"不見五陵豪傑墓，無花無酒鋤作田。")

p1 = "" 
for i in range(len(q)) :
    if q[i] not in ["，", "。"] : p1 += q[i] 


p = ""
for i in range(len(p1)) :
    p += p1[i]
    if i%7 == 3 : p += "／"


N = len(p)
while True :
    r = int(input("==> "))
    R = 8 * r 
    C = N//R + (1 if N%R else 0)

    for i in range(R) :
        for j in range(C-1,-1,-1) :
            k = j*R+i 
            print(p[k] if k < N else "  ", end=" ") 
        if (i+1)%8 == 0 : print() 
        print() 
