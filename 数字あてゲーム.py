#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1〜10のランダムな数字を当てるゲーム_niko
import random
x=random.randint(1,10)
while True:
    y=int(input('1~10の数字を当ててください：'))
    if y>x:
        print('もっと小さいです')

    elif y<x:
        print('もっと大きいです')

    elif y==x:
        print('正解！')
        break

