# First solution: sort the array, find the max h_index where len(citations)-i <= citations[i] storing max h_index
# ex [3,3,3,3,3,3,3], len(citations)-i decreases as i increases, causing h index to decrease

def hIndex(citations):
    citations.sort()
    h_index = 0

    for i in range(len(citations)):
        if len(citations)-i <= citations[i]:
            h_index = max(h_index, len(citations)-i)
        # if citations[i] > h_index and citations[i] >= len(citations) - i:
        #     h_index = max(h_index, len(citations)-i)
    
    return h_index


print(hIndex([3,0,6,1,5]))
print(hIndex([1,3,1]))
print(hIndex([100]))