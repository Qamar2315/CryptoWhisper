from itertools import permutations
import random

def generateKey():
    finalStr=[]
    codeLib=['!','@','#','$','%','^','&','*','(',')','-','+','=','~']
    while len(finalStr) != 5:
        elem=codeLib[random.randint(0,len(codeLib)) - 1]
        if not elem in finalStr:
            finalStr.append(elem)
    return finalStr

def mapDictionary():
    key=generateKey()
    seq= list(permutations(key))
    alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','1','2','3','4','5','6','7','8','9']
    dic={}
    for i in range(len(alpha)):
        dic[alpha[i]]=seq[i]
    return dic,key

def codeMssgList(mssg):
    seqDic,key= mapDictionary()
    mssg= mssg.lower()
    codedMssg=[]
    for i in range(len(mssg)):
        codedMssg.append(seqDic[mssg[i]])
    key.insert(0,'{')
    key.insert(6,"}")
    key=tuple(key)
    codedMssg.insert(random.randint(0,len(codedMssg)),key)
    return codedMssg

def toString(mssg):
    finalStr=""
    codedTupleList=codeMssgList(mssg)
    for i in range(len(codedTupleList)):
        for j in range(len(codedTupleList[i])):
            finalStr+=codedTupleList[i][j]
    return finalStr