name_for_userid={
    382:"Ailce",
    590:"Bob",
    951:"Dilbert",
    }
def greeting(userid):
    return "Hi %s" % name_for_userid.get(userid,"there")

print(greeting(382))
print(greeting(33333))