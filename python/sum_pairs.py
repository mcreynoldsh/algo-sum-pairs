def sum_pairs(num_list, check_sum):
    pairs_list=[]
    for i, k in enumerate (num_list):
        check_list= num_list[i+1:]
        for n in check_list:
            if k + n == check_sum:
                pairs_list.append([k,n])
    if len(pairs_list) != 0:
        return pairs_list
    else:
        return  'unable to find pairs'            



