
print("Loading two_sum module")

def two_sum(nums, target):
    print("Executing two_sum algorithm")
    return []

def main():
    print("Executing two_sum main")

def two_sum(nums, target):
    print("Executing two_sum algorithm")
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []


def main():
    nums = list(map(int, input().split()))
    target = int(input())

    result = two_sum(nums, target)

    print(result)


if __name__ == "__main__":
    main()