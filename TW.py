#!/usr/bin/env python
#coding=utf-8
from datetime import *
import unittest
def getSnapshot(historyData, id):
    data = historyData.split('\n')
    lines = len(data)
    if lines < 2 :
        return 'Input is too short!'
    index = 0
    curid = ''
    idlist = dict()
    recordtime = ''
    animal_pos = dict()
    for i in range(lines):
        if len(data[i]) > 0:#id行
            if index == 0: #可能有id为空的情况未处理
                curid = data[i]
                index += 1
                if curid in idlist:#检查id是否冲突
                    return 'Conflict found at ' + curid
                else:
                    idlist[curid] = 1#保存新id
            elif index == 1:#日期行
                if len(data[i]) == 0:#检查日期是否为空
                    return 'Conflict found at ' + curid
                recordtime = data[i]
                index += 1
                try:#检查日期格式是否正确
                    t1 = datetime.strptime(recordtime, '%Y/%m/%d %H:%M:%S')
                except:
                    return 'Invalid format.'
            else:#数据行
                animal = data[i].split(' ')
                if len(animal) == 3:#如果是新动物,检查以前是否出现过
                    if animal[0] in animal_pos:
                        return 'Conflict found at ' + curid
                    else:
                        animal_pos[animal[0]] = [animal[1], animal[2]]
                elif len(animal) == 5:#如果是旧动物,检查以前是否出现过
                    if animal[0] not in animal_pos:
                        return 'Conflict found at ' + curid
                    else:#如果确实是旧动物,校验位置信息
                        ox = animal_pos[animal[0]][0]
                        oy = animal_pos[animal[0]][1]
                        if (ox != animal[1]) or (oy != animal[2]):#校验失败
                            return 'Conflict found at ' + curid
                        else:#校验成功,更新位置信息
                            animal_pos[animal[0]][0] = str(int(animal_pos[animal[0]][0]) + int(animal[3]))
                            animal_pos[animal[0]][1] = str(int(animal_pos[animal[0]][1]) + int(animal[4]))
        else:#一个快照数据读入完毕
            index = 0
        if(id == curid) and (index == 0 or i == lines-1):#查询的id就是当前快照点
            res = ''
            for k, v in animal_pos.iteritems():#拼接字符串
                tmp = k + ' ' + v[0] + ' ' + v[1]
                res += (tmp + '\n')
    return res

