import json  #导入json模块

#字典标准打印不好读
my_mapping={'f':200,'a':23,'b':42,'c':0xc0ffee,'d':100}
print(my_mapping)
#{'a': 23, 'b': 42, 'c': 12648430}

print(json.dumps(my_mapping,indent=4,sort_keys=True))
# {
#     "a": 23,
#     "b": 42,
#     "c": 12648430
# }
#这只适合于字典

json.dumps({all:'yup'})
#TypeError: keys must be str, int, float, bool or None, not 

#dumps 转储
#indent 缩进4个空格
#sort_keys=True 排序


