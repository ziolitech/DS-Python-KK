


def max_freq(arr):
    freq_nums = {}
    max_freq = -1

    for i in range(len(arr)):
        freq = -1
        if arr[i] in freq_nums:
            freq = freq_nums[arr[i]] + 1
        else:
            freq = 1

        freq_nums[arr[i]] = freq
        if max_freq < freq:
            max_freq = freq

    return max_freq




def main():
    arr = list(map(int, input().split()))
    result = max_freq(arr)
    if result == -1:
        print(result)
    else:
        ## min operations.
        print(len(arr)-result)
    

if __name__ == "__main__":
    main()