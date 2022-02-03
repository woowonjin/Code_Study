def solution(n, arr1, arr2):
    answer = []
    for val1, val2 in zip(arr1, arr2):
        res = val1 | val2
        bin_res = bin(res)[2:]
        bin_res = "0"*(n-len(bin_res)) + bin_res
        bin_res = bin_res.replace("0", " ")
        bin_res = bin_res.replace("1", "#")
        answer.append(bin_res)
    return answer