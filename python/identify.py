import sys

# f = open("yesterday2","r",encoding="utf-8")
# f_new = open("yesterday2.bak","w",encoding="utf-8")
# find_str = sys.argv[1]
# repliac_str = sys.argv[2]
with open("yesterday2","R",encoding="utf-8") as f ,\
    open("yesterday2.bak","w",encoding="utf-8") as f2:

    for line in f:
        if "我的皮肤因为你的碰触而剧烈燃烧" in line:
            line = line.replace("我的皮肤因为你的碰触而剧烈燃烧","pshade的皮肤因为你的碰触而剧烈燃烧")
        f2.write(line)

# f.close()
# f_new.close()