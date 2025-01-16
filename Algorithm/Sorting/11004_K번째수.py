"""
문제
수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.
"""

"""
입력
첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.

둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)
"""

"""
출력
A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.
"""

import sys
input = sys.stdin.readline


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[-1]

#     left = [x for x in arr[:-1] if x <= pivot]
#     right = [x for x in arr[:-1] if x > pivot]

#     return quick_sort(left) + [pivot] + quick_sort(right)

# 루머의 파티션을 이용한 퀵 정렬
# def quick_sort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         # print(f"pi => {pi}")

#         quick_sort(arr, low, pi-1)
#         quick_sort(arr, pi+1, high)


# def partition(arr, low, high):
#     pivot = arr[high]
#     # print(f"pivot => {pivot}")
#     i = low - 1
#     # print(f"i => {i}")

#     for j in range(low, high):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#             print(f"for -> {arr}")

#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     # print(f"partition -> {arr}")

#     return i + 1


# def main():
#     N, K = map(int, input().split())
#     nlist = list(map(int, input().split()))

#     quick_sort(nlist, 0, len(nlist)-1)

#     # print(nlist)
#     print(nlist[K-1])

#     # rlist = quick_sort(nlist)

#     # print(rlist)

#     # print(rlist[K-1])


# if __name__ == "__main__":
#     main()


input = sys.stdin.readline

N, K = map(int, input().split())
nlist = list(map(int, input().split()))

print(sorted(nlist)[K-1])  # 병합 정렬 + 삽입 정렬 하이브리드 알고리즘  / 시간 복잡도 O(nlogn)

# sort()와 sorted() 차이
# sorted()는 새로운 리스트를 반환하므로 원본 데이터를 그대로 보존
# sort() 원본 데이터를 변경, 즉 리스트를 직접 수정 / 반환 값이 없다!
