from email.generator import DecodedGenerator
from itertools import permutations

def getKey(mssg):
    key=[]
    for i in range(0, len(mssg)):
        if mssg[i] == '{':
                key.append(mssg[i+1])
                key.append(mssg[i+2])
                key.append(mssg[i+3])
                key.append(mssg[i+4])
                key.append(mssg[i+5])
                break
    return key

def mapDictionaryReverse(codedMssg):
    key=getKey(codedMssg)
    pureMssg=remKey(codedMssg)
    seq= list(permutations(key))
    alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','1','2','3','4','5','6','7','8','9']
    dic={}
    for i in range(len(alpha)):
        dic[seq[i]]=alpha[i]
    return dic,pureMssg

def remKey(mssg):
    pureMssg=""
    index=0
    for i in range(0, len(mssg)):
        if mssg[i] == "{":
            index=i
    pureMssg=mssg.replace(mssg[index:index+7],'')
    return pureMssg

def createTupleList(mssg):
    tupleList=[]
    for i in range(0,len(mssg),5):
        alphaTuple=(mssg[i],mssg[i+1],mssg[i+2],mssg[i+3],mssg[i+4])
        tupleList.append(alphaTuple)
    return tupleList

def deCodeMssgList(mssg):
    seqDic,pureMssg= mapDictionaryReverse(mssg)
    tupleList=createTupleList(pureMssg)
    deCodedMssg=[]
    for i in range(len(tupleList)):
        deCodedMssg.append(seqDic[tupleList[i]])
    return deCodedMssg

def toString(mssg):
    finalStr=""
    deCodedMessageList=deCodeMssgList(mssg)
    for i in range(len(deCodedMessageList)):
        finalStr+=deCodedMessageList[i]
    return finalStr