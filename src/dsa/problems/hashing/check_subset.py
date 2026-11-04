# Check if the array 'b' is a subset of array 'a'. There are no duplicates in both the arrays

# Logic using set has O(n+m) time complexity
# If we use brute force way to check then the complexity would be O(n*m)

# Similar Problem: Check this if arrays have duplicates .. we use a hashmap rather than a HashSet or set.

def check_subset(arr1, arr2):
    #using set here
    arr1_set = set()

    # adding items to the set
    for i in range(len(arr1)):
        arr1_set.add(arr1[i])

    for i in range(len(arr2)):
        if arr2[i] not in arr1_set:
            print("Arr2 is not a subset of arr1")
            return False

    print("arr2 is a subset of arr1")
    return True



def main():
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    result = check_subset(arr1, arr2)
    print(result)


if __name__ == "__main__":
    main()