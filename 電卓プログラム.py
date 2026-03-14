#!/usr/bin/env python
# coding: utf-8

# In[1]:


#CLI電卓プログラム_niko
while True:
    print('\n1:足し算')
    print('2:引き算')
    print('3:掛け算')
    print('4:割り算')
    print('5:終了')
    x=int(input('選択してください：'))
    
    if x==1:
        a=int(input('1つ目の数字：'))
        b=int(input('2つ目の数字：'))
        print(f'答え：{a+b}')

    elif x==2:
        a=int(input('1つ目の数字：'))
        b=int(input('2つ目の数字：'))
        print(f'答え：{a-b}')

    elif x==3:
        a=int(input('1つ目の数字：'))
        b=int(input('2つ目の数字：'))
        print(f'答え：{a*b}')

    elif x==4:
        a=int(input('1つ目の数字：'))
        b=int(input('2つ目の数字：'))
        if b==0:
            print('0では割れません')
        else:
            print(f'答え：{a/b}')

    elif x==5:
        print('終了します')
        break

    else:
        print('1~5の数字を入力してください!')

