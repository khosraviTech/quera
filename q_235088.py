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

work_hight = ceiling - floor

for_ceiling = day_on_ceiling + remain_day_on_ceiling
for_floor = day_on_floor + remain_day_on_floor

if((work_hight==0) and remain_day_on_ceiling == 0 ): #7 3,3 OK
    print(day_on_ceiling)

if((for_ceiling < for_floor) and remain_day_on_ceiling == 0 ): #4 1,2 OK
    print(day_on_ceiling)

if((for_ceiling < for_floor) and floor < remain_day_on_ceiling < ceiling  ): #10 3,6 OK
    print(day_on_ceiling+1)

#10 3,4?    
# if((for_ceiling < for_floor) and floor < remain_day_on_ceiling < ceiling  ): #10 3,6 OK
#     print(day_on_ceiling+1)