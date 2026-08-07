def calculator(n, m, li):
    sep_list = [li[i : i + m] for i in range(0, len(li), m)]
    # print("sep list is: ", sep_list)
    sum_list = []
    for i in sep_list:
        sum_list.append(sum(i))
    # print("sum list is:", sum_list)

    for i in range(0, len(sum_list)):
        if i % 2 != 0:
            sum_list[i] = -abs(sum_list[i])

    # print("sum lsit after negativation:", sum_list)
    # print("sum of sum_list values and the final result is : ", sum(sum_list))
    
    return sum(sum_list)
    
