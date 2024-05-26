# Sorts a given list in ascending order, using merge sort.
def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    pivot = len(nums) // 2
    left_arr = merge_sort(nums[:pivot])
    right_arr = merge_sort(nums[pivot:])

    return _merge_lists(left_arr, right_arr)


# Takes two lists, mergers them in ascending order and returns them
def _merge_lists(left_arr, right_arr):
    l = r = 0
    res = []
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            res.append(left_arr[l])
            l += 1
        else:
            res.append(right_arr[r])
            r += 1

    # add remaining elements, if any
    res.extend(left_arr[l:])
    res.extend(right_arr[r:])
    return res


def main():
    nums = [1, 5, 5, -13, 20, 11, 17]
    sorted_nums = merge_sort(nums)
    assert sorted_nums == sorted(nums)
    print(f"original = {nums}")
    print(f"sorted   = {sorted_nums}")


if __name__ == "__main__":
    main()
