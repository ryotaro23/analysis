#代入
i=1
j=1
while i<10:#つぎにiを１～９まで変化
    while j<10:#まずｊを１～９まで変化
        print (i*j)
        j=j+1
    i=i+1
    j=1#j=9からj=１にリセットする
print('終了')
