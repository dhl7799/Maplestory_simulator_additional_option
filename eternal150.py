from random import randint
import os
import random

def getLevel(table):
    Level = randint(0,99)
    return table[Level]

def returnName(num):
    return name[num]

table = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
         2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
         2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
         3,3,3,3,3,3,3,3,3,3,4]

option = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]


item = ["STR","DEX","INT","LUK","최대 HP","최대 MP","올스텟%","공격력","마력",
        "이동속도","점프력","방어력","착용 레벨 감소"]

print("영환불 바를 갯수를 입력하세요:")
x = int(input())

for num in range(0,x):
    additional = set()
    baseoption=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    #           힘덱인럭체마올공마이점방착
    while len(additional)<4:
        additional.add(random.randint(0,18))
    print("시도",num)
    for i in range(0,4):
        Level = getLevel(table)
        
        #힘
        if list(additional)[i] ==0:
            if Level ==1:
                baseoption[0] += 32
            elif Level ==2:
                baseoption[0] += 40
            elif Level ==3:
                baseoption[0] += 48
            elif Level ==4:
                baseoption[0] += 56
                
        #덱스        
        if list(additional)[i] ==1:
            if Level ==1:
                baseoption[1] += 32
            elif Level ==2:
                baseoption[1] += 40
            elif Level ==3:
                baseoption[1] += 48
            elif Level ==4:
                baseoption[1] += 56
                
        #인트
        if list(additional)[i] ==2:
            if Level ==1:
                baseoption[2] += 32
            elif Level ==2:
                baseoption[2] += 40
            elif Level ==3:
                baseoption[2] += 48
            elif Level ==4:
                baseoption[2] += 56
                
        #럭
        if list(additional)[i] ==3:
            if Level ==1:
                baseoption[3] += 32
            elif Level ==2:
                baseoption[3] += 40
            elif Level ==3:
                baseoption[3] += 48
            elif Level ==4:
                baseoption[3] += 56
                

        #힘덱
        if list(additional)[i] ==4:
            if Level ==1:
                baseoption[0] += 16
                baseoption[1] += 16
            elif Level ==2:
                baseoption[0] += 20
                baseoption[1] += 20
            elif Level ==3:
                baseoption[0] += 24
                baseoption[1] += 24
            elif Level ==4:
                baseoption[0] += 28
                baseoption[1] += 28

        #힘인
        if list(additional)[i] ==5:
            if Level ==1:
                baseoption[0] += 16
                baseoption[2] += 16
            elif Level ==2:
                baseoption[0] += 20
                baseoption[2] += 20
            elif Level ==3:
                baseoption[0] += 24
                baseoption[2] += 24
            elif Level ==4:
                baseoption[0] += 28
                baseoption[2] += 28

        #힘럭
        if list(additional)[i] ==6:
            if Level ==1:
                baseoption[0] += 16
                baseoption[3] += 16
            elif Level ==2:
                baseoption[0] += 20
                baseoption[3] += 20
            elif Level ==3:
                baseoption[0] += 24
                baseoption[3] += 24
            elif Level ==4:
                baseoption[0] += 28
                baseoption[3] += 28

        #덱인
        if list(additional)[i] ==7:
            if Level ==1:
                baseoption[1] += 16
                baseoption[2] += 16
            elif Level ==2:
                baseoption[1] += 20
                baseoption[2] += 20
            elif Level ==3:
                baseoption[1] += 24
                baseoption[2] += 24
            elif Level ==4:
                baseoption[1] += 28
                baseoption[2] += 28

        #덱럭
        if list(additional)[i] ==8:
            if Level ==1:
                baseoption[1] += 16
                baseoption[3] += 16
            elif Level ==2:
                baseoption[1] += 20
                baseoption[3] += 20
            elif Level ==3:
                baseoption[1] += 24
                baseoption[3] += 24
            elif Level ==4:
                baseoption[1] += 28
                baseoption[3] += 28

        #인럭
        if list(additional)[i] ==9:
            if Level ==1:
                baseoption[2] += 16
                baseoption[3] += 16
            elif Level ==2:
                baseoption[2] += 20
                baseoption[3] += 20
            elif Level ==3:
                baseoption[2] += 24
                baseoption[3] += 24
            elif Level ==4:
                baseoption[2] += 28
                baseoption[3] += 28

        #HP        
        if list(additional)[i] ==10:
            if Level ==1:
                baseoption[4] += 1800
            elif Level ==2:
                baseoption[4] += 2250
            elif Level ==3:
                baseoption[4] += 2700
            elif Level ==4:
                baseoption[4] += 3150

        #MP
        if list(additional)[i] ==11:
            if Level ==1:
                baseoption[5] += 1800
            elif Level ==2:
                baseoption[5] += 2250
            elif Level ==3:
                baseoption[5] += 2700
            elif Level ==4:
                baseoption[5] += 3150

        #올스텟
        if list(additional)[i] ==12:
            if Level ==1:
                baseoption[6] += 4
            elif Level ==2:
                baseoption[6] += 5
            elif Level ==3:
                baseoption[6] += 6
            elif Level ==4:
                baseoption[6] += 7

        #공격력
        if list(additional)[i] ==13:
            if Level ==1:
                baseoption[7] += 4
            elif Level ==2:
                baseoption[7] += 5
            elif Level ==3:
                baseoption[7] += 6
            elif Level ==4:
                baseoption[7] += 7

        #마력
        if list(additional)[i] ==14:
            if Level ==1:
                baseoption[8] += 4
            elif Level ==2:
                baseoption[8] += 5
            elif Level ==3:
                baseoption[8] += 6
            elif Level ==4:
                baseoption[8] += 7

        #이속
        if list(additional)[i] ==15:
            if Level ==1:
                baseoption[9] += 4
            elif Level ==2:
                baseoption[9] += 5
            elif Level ==3:
                baseoption[9] += 6
            elif Level ==4:
                baseoption[9] += 7

        #점프
        if list(additional)[i] ==16:
            if Level ==1:
                baseoption[10] += 4
            elif Level ==2:
                baseoption[10] += 5
            elif Level ==3:
                baseoption[10] += 6
            elif Level ==4:
                baseoption[10] += 7

        #방어력
        if list(additional)[i] ==17:
            if Level ==1:
                baseoption[11] += 32
            elif Level ==2:
                baseoption[11] += 40
            elif Level ==3:
                baseoption[11] += 48
            elif Level ==4:
                baseoption[11] += 56

        #착감
        if list(additional)[i] ==18:
            if Level ==1:
                baseoption[12] += -20
            elif Level ==2:
                baseoption[12] += -25
            elif Level ==3:
                baseoption[12] += -30
            elif Level ==4:
                baseoption[12] += -35

    for k in range(0,13):
        if baseoption[k] != 0:
            print(item[k],baseoption[k],end="\n")

    print("\n")
                

                
        
os.system('pause')





