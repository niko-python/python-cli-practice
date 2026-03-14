#!/usr/bin/env python
# coding: utf-8

# In[3]:


# ToDo CLIアプリ_niko
tasks=[]
while True:
    print('\n1:タスク追加')
    print('2:タスク一覧')
    print('3:タスク削除')
    print('4:終了')
    x=int(input('選択してください：'))

    if x==1:
        task=input('追加するタスクを入力してください：')
        tasks.append(task)
        print(f'[{task}]をタスクとして入力しました')

    elif x==2:
        print(f'タスク一覧：{tasks}')

    elif x==3:
        del_task=input('削除するタスクを入力してください：')
        if del_task in tasks:
            tasks.remove(del_task)
        else:
            print(f'{del_task}はタスクとして入力されていません')

    elif x==4:
        print('終了します')
        break

    else:
        print('1~4の数字を入力してください')

