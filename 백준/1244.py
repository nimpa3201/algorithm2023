n = int(input())
swich = [0]+list(map(int,input().split()))
student = int(input())



def recusionfuntion(k):                                                     #num 받음
    if  0>=k or k>n:                    #범위 이탈하면  swich 반환
        return swich                                                        
    if recusionfuntion(swich[k-1]) != recusionfuntion(swich[k+1]) : #비대칭이면 swich 반환
        return swich
    else: #ㄱrecusionfuntion(swich[k-1]) == recusionfuntion(swich[k+1])를 의미한다고 생각함
        if swich[k] ==1:    #그래서 받은 인자값 바꿔줌
            swich[k]=0
        else :
            swich[k]=1



for _ in range(student):
    gender,num = map(int,input().split())
    
    
    if gender ==1:
        for i in range(1,len(swich)):
            if i%num ==0 :
                if swich[i] ==1:
                    swich[i]=0
                else:
                    swich[i]=1
    if gender ==2:
        print(recusionfuntion(num,))   #num 기준으로 대칭이면 숫자 바꿔야 된다.
        
        
        
        
        #if swich[num] ==1:
        #     swich[num]=0
        # else:
        #     swich[num]=1
        # L =num-1             여기는 재귀함수 안쓰려고 짠거
        # R =num+1
        # while 0<L and R<n:
        #     if swich[L]==swich[R]:
        #         if swich[L] ==1:
        #             swich[L]=0
        #             swich[R]=0
        #         else:
        #             swich[L]=1
        #             swich[R]=1
        #     if swich[L]==0 != swich[R]:
        #         break
        #     L-=1
        #     R+=1

for idx,i  in enumerate( swich[1:]):
    if (idx+1 )% 20  ==0 :
        print(i)
    
    else:
        print(i,end=' ') 

 