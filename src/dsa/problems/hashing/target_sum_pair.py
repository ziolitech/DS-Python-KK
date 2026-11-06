# Target sum pair exists
# Approach:
# Brute force: Check every pair .. TC = N-1 + N-2 + N-3 .. + 1 ~= O(N²)
# With Running Hashmap/Hashset .. which stores if a num has occurred earlier: 
# With this we can just do this in O(N)
# Assumptions : All numbers are positive

def check_target(arr,target_sum):
    seen = set()

    for i in range(len(arr)):
        num = arr[i]
        need = target_sum - num
        if need in seen:
            return True
        else:
            seen.add(arr[i])

    return False
            



def main():
    arr = list(map(int, input().split()))
    target_sum = int(input())

    result = check_target(arr,target_sum)
    print(result)


if __name__ == "__main__":
    main()                                