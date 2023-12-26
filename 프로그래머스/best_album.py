def solution(genres, plays):
    music = dict()
    list1= []
    limit = dict()
    for idx,g in enumerate(genres):
        list1.append([idx,g,plays[idx]])

    for  g,p in zip(genres,plays):
        if g not in music:
            music[g] =p
        else:
            music[g] +=p
    for  i in list1:
        if i[1] in music:
            i.append(music[i[1]])

    list1.sort(key = lambda x : (-x[3],-x[2],x[0]))
    ans =[]
    for i in list1:
        if i[1] not in limit:
            limit[i[1]] =1
            ans.append(i[0])
        elif limit[i[1]] <2:
            limit[i[1]]+=1
            ans.append(i[0])
        
        else:
            continue


    return ans




print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))	#[4, 1, 3, 0]