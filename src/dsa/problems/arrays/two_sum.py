def two_sum(nums, target):
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