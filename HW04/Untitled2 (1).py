#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_lines(file_name):
    '''<foo> and remove all comments'''

    lines = []
    try:
        fp = open(file_name, "r")
    except FileNotFoundError:
        print(f"Can't open {file_name}")
    else:
        with fp:
            fhand = fp.readlines()
            # print(fhand)
            for i in fhand:
                if i.endswith("\\\n"):
                    i = i.rstrip("\\\n")
                lines.append(i)
    finally:
        print(1)
        for i in lines:
            index = len(i)
            if "#" in i:
                index = i.find("#")
            if i[:index].strip() is not "":
                yield i[:index].strip()


# In[8]:


for i in get_lines("hw05_test2.txt"):
    print(i)

# In[ ]:
