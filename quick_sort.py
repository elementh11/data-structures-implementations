def quicksort(arr, left, right):
    '''
    Implementation of the quicksort algoritm
    '''
    
    if left >= right:
        return

    pivot = arr[(left + right)/2]

    index = partition(arr, left, right, pivot)

    quicksort(arr, left, index - 1)
    quicksort(arr, index, right)

def partition(arr, left, right, pivot):

    while(left <= right):
        while(arr[left] < pivot):
            left += 1

        while(arr[right] > pivot):
            right -= 1

        if (left <= right):
            #swap(arr, left, right)
            arr[left], arr[right] = arr[right], arr[left]
            
            left += 1
            right -= 1

    return left
