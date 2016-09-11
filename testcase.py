#!/usr/bin/env python
#encoding: utf-8

#以下是测试数据

#测试用例1:正确输出结果
tcidata1 = '''e4e87cb2-8e9a-4749-abb6-26c59344dfee
2016/09/02 22:30:46
cat1 10 9

351055db-33e6-4f9b-bfe1-16f1ac446ac1
2016/09/02 22:30:52
cat1 10 9 2 -1
cat2 2 3

dcfa0c7a-5855-4ed2-bc8c-4accae8bd155
2016/09/02 22:31:02
cat1 12 8 3 4
'''
tciid1 = 'dcfa0c7a-5855-4ed2-bc8c-4accae8bd155'
tco1 = '''cat1 15 12
cat2 2 3
'''

#测试用例2:动物位置校验失败
tcidata2 = '''e4e87cb2-8e9a-4749-abb6-26c59344dfee
2016/09/02 22:30:46
cat1 10 9

351055db-33e6-4f9b-bfe1-16f1ac446ac1
2016/09/02 22:30:52
cat1 10 9 2 -1
cat2 2 3

dcfa0c7a-5855-4ed2-bc8c-4accae8bd155
2016/09/02 22:31:02
cat1 11 8 3 4
'''
tciid2 = 'dcfa0c7a-5855-4ed2-bc8c-4accae8bd155'
tco2 = '''Conflict found at dcfa0c7a-5855-4ed2-bc8c-4accae8bd155'''

#测试用例3:ID唯一性
tcidata3 = '''e4e87cb2-8e9a-4749-abb6-26c59344dfee
2016/09/02 22:30:46
cat1 10 9

e4e87cb2-8e9a-4749-abb6-26c59344dfee
2016/09/02 22:30:52
cat1 10 9 2 -1
cat2 2 3

dcfa0c7a-5855-4ed2-bc8c-4accae8bd155
2016/09/02 22:31:02
cat1 12 8 3 4
'''
tciid3 = 'dcfa0c7a-5855-4ed2-bc8c-4accae8bd155'
tco3 = '''Conflict found at e4e87cb2-8e9a-4749-abb6-26c59344dfee'''

#测试用例4:输入时间不完整
tcidata4 = '''e4e87cb2-8e9a-4749-abb6-26c59344dfee
2016/09/02 22:30:46
cat1 10 9

351055db-33e6-4f9b-bfe1-16f1ac446ac1
2016/09/02 22:30:
cat1 10 9 2 -1
cat2 2 3

dcfa0c7a-5855-4ed2-bc8c-4accae8bd155
2016/09/02 22:31:02
cat1 12 8 3 4
'''
tciid4 = 'dcfa0c7a-5855-4ed2-bc8c-4accae8bd155'
tco4 = '''Invalid format.'''

#测试用例5:动物还未出现就开始移动(第一次捕捉动物位置时没有移动信息)
tcidata5 = '''e4e87cb2-8e9a-4749-abb6-26c59344dfee
2016/09/02 22:30:46
cat1 10 9

351055db-33e6-4f9b-bfe1-16f1ac446ac1
2016/09/02 22:30:46
cat1 10 9 2 -1
cat2 2 3


dcfa0c7a-5855-4ed2-bc8c-4accae8bd155
2016/09/02 22:31:02
cat1 12 8 3 4
cat3 10 1 2 2
'''
tciid5 = 'dcfa0c7a-5855-4ed2-bc8c-4accae8bd155'
tco5 = '''Conflict found at dcfa0c7a-5855-4ed2-bc8c-4accae8bd155'''

#测试用例6:动物第二次新动物的形式出现(如果以前出现过该动物,那么下次出现一定是动物产生移动)
tcidata6 = '''e4e87cb2-8e9a-4749-abb6-26c59344dfee
2016/09/02 22:30:46
cat1 10 9

351055db-33e6-4f9b-bfe1-16f1ac446ac1
2016/09/02 22:30:52
cat1 10 9 2 -1
cat2 2 3

dcfa0c7a-5855-4ed2-bc8c-4accae8bd155
2016/09/02 22:31:02
cat1 12 8 3 4
cat1 10 9
'''
tciid6 = 'dcfa0c7a-5855-4ed2-bc8c-4accae8bd155'
tco6 = '''Conflict found at dcfa0c7a-5855-4ed2-bc8c-4accae8bd155'''

#测试用例7:违法时间(25:31:02)
tcidata7 = '''e4e87cb2-8e9a-4749-abb6-26c59344dfee
2016/09/02 22:30:46
cat1 10 9

351055db-33e6-4f9b-bfe1-16f1ac446ac1
2016/09/02 22:30:52
cat1 10 9 2 -1
cat2 2 3

dcfa0c7a-5855-4ed2-bc8c-4accae8bd155
2016/09/02 25:31:02
cat1 12 8 3 4
cat1 10 9
'''
tciid7 = 'dcfa0c7a-5855-4ed2-bc8c-4accae8bd155'
tco7 = '''Invalid format.'''
