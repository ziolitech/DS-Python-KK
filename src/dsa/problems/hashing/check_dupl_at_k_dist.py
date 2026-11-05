# find if a duplicate element present at k dist.
# Approaches
# Brute Force ..
#  for each element navigate upto k elements to see if the duplicate element exists. TC = O(N*K)
# Or we hashmap - with key as element as first position where the element is found
# if the element is present beyond the k window ... the. we update the position 



def check_dupl_at_k_dist(arr,window):
    pos_dict = {}

    for i in range(len(arr)):
        if arr[i] in pos_dict:
            # check if it is within k dist
            pos = arr[i]
            if i - pos <= window:
                return True
            else:
               # update the position if prev post exists beyond the window
               pos_dict[arr[i]] = i
        else:
            # update with position
            pos_dict[arr[i]] = i

    return False

    




def main():
    arr = list(map(int,input().split()))
    window = int(input())
    result = check_dupl_at_k_dist(arr,window)

    print(result)


if __name__ == "__main__":
    main()
    






