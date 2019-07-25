__Author__ = "noduez"

import itchat
import random

itchat.auto_login()

friends_list = itchat.get_friends(update=True)
print(len(friends_list))
luohao = friends_list[0]
props = ['NickName', 'Signature', 'Sex']
for prop in props:
    print(luohao[prop])

lucky_friends = random.sample(friends_list[1:], 5)
props = ['NickName', 'Signature', 'City']
for friend in lucky_friends:
    for prop in props:
        print(friend[prop] or '没有此项信息')
    print('-' * 80)