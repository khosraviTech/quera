# https://quera.org/problemset/235088

# input
n = int(input())
lr=input()

floor=int(lr.split(' ')[0])
ceiling=int(lr.split(' ')[1])

# algorithem

day_on_floor = n // floor
remain_day_on_floor = n % floor

day_on_ceiling = n // ceiling
remain_day_on_ceiling = n % ceiling

hight = ceiling - floor

for_ceiling = day_on_ceiling + remain_day_on_ceiling
for_floor = day_on_floor + remain_day_on_floor

if((hight==0) and remain_day_on_ceiling == 0 ): #7 3,3 OK
    print(day_on_ceiling)

if((for_ceiling < for_floor) and remain_day_on_ceiling == 0 ): #4 1,2 OK
    print(day_on_ceiling)

if((for_ceiling < for_floor) and floor < remain_day_on_ceiling < ceiling  ): #10 3,6 OK
    print(day_on_ceiling+1)

elif( remain_day_on_floor <= hight and n==(day_on_floor-1)*floor+ceiling  ): #10 3,4 OK
    print(day_on_floor-1+1)



# new algorithem:

day_on_floor = n // floor
remain_day_on_floor = n % floor

day_on_ceiling = n // ceiling
remain_day_on_ceiling = n % ceiling

hight = ceiling - floor
# 22 3,4
def dividing(n=n,floor=floor,ceiling=ceiling,hight=hight,day_on_ceiling=day_on_ceiling,remain_day_on_ceiling=remain_day_on_ceiling)-> int:   
    
    if(n<floor or (hight==0 and remain_day_on_ceiling!=0)):
        return -1

    if(hight==0 and remain_day_on_ceiling==0):
        return day_on_ceiling
    
    if(remain_day_on_ceiling > ceiling):

        if(dividing(n=remain_day_on_ceiling)== -1):

            day_on_ceiling = day_on_ceiling -1
            dividing(day_on_ceiling=day_on_ceiling, remain_day_on_ceiling = n - (day_on_ceiling*ceiling))

        elif():
            pass
    elif(remain_day_on_ceiling < ceiling):
        pass


