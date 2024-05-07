p="茶香葉嫩芽慕詩客愛僧家碾雕白玉羅織紅紗銚煎黃蕊色碗轉曲塵花夜後邀陪明月晨前命對朝霞洗盡古今人不倦將至醉後豈堪誇"
k=0
for i in range (1,8):
    print ("  "*(8-i),end="")
    if i ==1 :
        print (" ",p[1])
        k=k+i
    else :
        print (p[k:k+i],p[k+i:k+2*i])
        k=k+2*i
               
