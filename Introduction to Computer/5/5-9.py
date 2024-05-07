q = ( "山裡有山路轉彎，高山流水響潺潺。"
"深山百鳥聲聲叫，路上行人步步難。"
"勸君莫作雲遊客，孤身日日在山間。"
"人人說道華山好，我道華山第八山。")

p = "" 
for i in range(len(q)) :
    if q[i] not in ["，", "。"] : p += q[i] 

w = (1,1,2,2,3,3,4,4,4,4)
kL = len(p)-1
kR = 0
for i in range(len(w)) :
    print("  "*(4-w[i]), end="")
    if i%2 :
        print(p[kL+w[i]-1:kL-1:-1], 
              p[kR+w[i]-1:kR-1:-1], sep="") 
    else :
        print(p[kL:kL+w[i]], 
              p[kR:kR+w[i]], sep = "")
    kL -= (w[i+1] if i < len(w)-1 else 9999)        
    kR += w[i] 
