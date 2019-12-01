name_for_userid={
    382:"Ailce",
    590:"Bob",
    951:"Dilbert",
    }
'''
用字典get()方法设置字典默认值 （）
'''
def greeting(userid):
    return "Hi %s" % name_for_userid.get(userid,"there") 

print(greeting(382)) 
#字典内 输出 Hi Ailce
print(greeting(33333)) 
#字典外 输出 Hi there
