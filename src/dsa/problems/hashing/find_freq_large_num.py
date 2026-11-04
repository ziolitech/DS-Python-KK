# Given an array, find the frequency of each element given the size of the an element 10⁹.
# As the num can be very large we dont use the Hash Array rather we use HasingMap or Dict in python.

def find_freq(arr):
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] +=1
        else:
            freq_dict[num] = 1

    return freq_dict




def main():
   arr = list(map(int,input().split()))
   result = find_freq(arr)
   print(result)


# needed if we want to execute directly using below command:
# python $module_path or python src/dsa/problems/arrays/two_sum.py
if __name__ == "__main__":
    main()