array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    # start와 end값이 같다는건 배열에 남아있는 값이 1개라는 뜻 [ 정렬이 모두 끝남 ]
    if start >= end:
        return
    # pivot을 시작점으로 한다
    pivot = start

    # pivot보다 큰 값을 찾기위한 left
    left = start + 1

    # pivot보다 작은 값을 찾기위한 right
    right = end

    # left가 right보다 작아야 실행한다 [ right가 더 큰 경우는 left와 right가 엇갈린 경우 ]
    while left <= right:
        # 피벗이 큰 데이터를 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # left와 right가 엇갈린 경우
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]

        # 엇갈리지 않고 실행 한 경우
        else:
            array[left], array[right] = array[right], array[left]

    # 분할 이후, pivot을 기점으로 왼쪽과 오른쪽에서 정렬 재실행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array)-1)

print(array)