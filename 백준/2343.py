n,m = map(int,input().split())
arr= list(map(int,input().split()))
L,R=-0,sum(arr) # 블루레이 크기 조절 그래서 L,R 을 잘 설정해줘야돼 
                #블루레이의 크기의 최솟값은 0 / 아무리 블루레이가 커봤자 arr 합 이 최대
ans =R+1






        
        
def is_possible(target): #미드값이 여기로 계속들어와(블루레이의 크기)
 
    tmp=0
    cnt=0
    piv=0
    for i in arr: 
        tmp+=i
        tp = tmp
        if tmp >target: #tmp는 노래 합 .. 그리고 target은 블루레이 크기
            cnt+=1 # 내상각엔 일단 이 함수 다시 짜야되는데 어쨌든 tmp 크기가 블루레이보다 크면 cnt 1 증가...
            tmp=i #tmp는 i로 초기화
        
        elif tmp ==target:
            cnt+=1
            tmp=0
        print(target,tmp,cnt,tp)
    if target <tp:
        cnt+=1
    return cnt<=m #이게 조건이 T 아님 F 로 나오겠지 ..   만약에 그래서 cnt 가 m 보다 작아 그러면 T 잖아 




while L <= R:               # L 이 R 보다 작다는 전제하에 mid 값을 계속 조절해줘야해 
    mid = (L+R)//2 #이게미드
    #print(mid)
    if is_possible(mid):    # 만약에 어떤 조건을 만족하면 (근데 보통 조건 설계를 먼저해 나는 그래서 말을 하자면 ...) cnt 가 m 보다 작은경우 cnt 값을 가능할때 미드 값을 줄여줘 그래야 cnt가 커질테니깐 
        R =mid-1
        ans = min(ans,mid)  #미드 값을 여기는 지금 최소값을 구하잖아 .. 그래서 그 가능한 것 중 최솟값을 계속 업데이트 한다
    
    else:
        L =mid+1 #이건 불가능한 경우 니깐 mid 값을 높여줘야 하는것 ... 미드값이 높아지면 cnt는 줄어드니깐 ....
print(ans) #최솟값이 답


#s_possible(17)