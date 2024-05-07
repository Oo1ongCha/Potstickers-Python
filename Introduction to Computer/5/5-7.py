q=("對酒當歌，人生幾何。譬如朝露，去日苦多。"
"慨當以慷，憂思難忘。何以解憂，唯有杜康。"
"青青子衿，悠悠我心。但為君故，沈吟至今。"
"呦呦鹿鳴，食野之苹。我有嘉賓，鼓瑟吹笙。"
"明明如月，何時可輟。憂從中來，不可斷絕。"
"越陌度阡，枉用相存。契闊談讌，心念舊恩。"
"月明星稀，烏鵲南飛。繞樹三匝，何枝可依。"
"山不厭高，海不厭深。周公吐哺，天下歸心。")

p=""
for i in range(len(q)):
    if q[i] not in ["，","。"]:p+=q[i]

N=len(p)
while True:
    r=int(input("==> "))
    R=4*r
    C=N//R+(1 if N%R else 0)

    for i in range (R):
          for j in range (C-1,-1,-1):
              k =R*j+i
              print(p[k] if k<N else "  " ,end =" ")
          if (i+1)%4 == 0: print()
          print()
