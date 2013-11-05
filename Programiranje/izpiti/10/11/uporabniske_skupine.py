import os, collections

#users = collections.defaultdict(list)
users = {}
if os.path.exists(os.getcwd()):
    for line in open("groups.txt","rt"):
        grp_name, password, group_id, grp_list = line.strip().split(":")
        for user in grp_list.split(","):
            if user not in users:
                users[user] = [grp_name]
            else:
                users[user].append(grp_name)
#print(uporabiske_skupine)
print(users["dani"])
