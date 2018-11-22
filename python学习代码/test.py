path = "E:/AI/Base_of_Python_code/f.txt"
tf = open(path,"w+")
ls = ["中国","美国","法国"]
tf.writelines(ls)
for line in tf:
    print (line)
tf.close()