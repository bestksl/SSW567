# @Author: HaoxuanLi
# @Date 2/19/2019
# CWID: 10434197
import requests
import json


def get_repo(id):
    r = requests.get("https://api.github.com/users/" + id + "/repos")
    j = r.json()
    list1 = []
    for ele in j:
        temp = requests.get("https://api.github.com/repos/bestksl/" + ele["name"] + "/commits")
        list1.append([ele["name"], len(temp.json())])
    return list1


l = get_repo("bestksl")
print(l)
