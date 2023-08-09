#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def tag():
    tag = ["#ち？ゆ？り", "#チ？ユ？リ", "#知？由？理"]
    return random.choice(tag)
title = tag()

meishi = "@長山？知由理"

print(title, meishi)

def tag1():
    tag1 = ["chiyuri.tiyuri", "tiyuri.chiyuri"]
    return random.choice(tag1)
title1 = tag1()

def tag2():
    tag2 = ["chiyuri.chiyuri", "tiyuri.tiyuri"]
    return random.choice(tag2)
title2 = tag2()

def tag3():
    tag3 = ["chiyuri.nagayama", "nagayama.chiyuri"]
    return random.choice(tag3)
title3 = tag3()

def tag4():
    tag4 = ["tiyuri.nagayama", "nagayama.tiyuri"]
    return random.choice(tag4)
title4 = tag4()

def tag5():
    tag5 = ["長山知由理", "長山ちゆり", "ながやまちゆり"]
    return random.choice(tag5)
title5 = tag5()

def tag6():
    tag6= ["ちゆり", "ちゆりちゃん"]
    return random.choice(tag6)
title6= tag6()

print(title1, title2, title3, title4, title5, title6)

def comment():
    comment = ["I'm doing well today.", "It's going well today.", "I am having a good time today."]
    return random.choice(comment)
subtitle = comment()

def name():
    name = ["Nagayama Chiyuri", "Chiyuri Nagayama"]
    return random.choice(name)
meishi = name()

print(subtitle, "by", meishi)

# In[ ]:




