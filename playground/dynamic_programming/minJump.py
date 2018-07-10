def minJump(arr, n):
    if n <= 1:
        return 0

    if arr[0] == 0:
        return -1

    maxR = arr[0]
    step = arr[0]
    jump = 1

    for i in range(1, n):
        if i == n - 1:
            return jump

        maxR = max(maxR, i+arr[i])
        step -= 1
        if step == 0:
            jump += 1
            if i >= maxR:
                return -1

            step = maxR - i
    return -1

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)

if __name__ == '__main__':
    print(minJump(arr, size))
