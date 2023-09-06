def heapify(nums, heap_size, root_index):
    largest = root_index
    left_el = (2 * root_index) + 1
    right_el = (2 * root_index) + 2

    if left_el < heap_size and nums[left_el] > nums[largest]:
        largest = left_el

    if right_el < heap_size and nums[right_el] > nums[largest]:
        largest = right_el

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    # Построение Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # Извлечение элементов из кучи и сортировка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]  # Перемещаем корень Max Heap в самый конец списка
        heapify(nums, i, 0)

random_list = [7, 18, 13, 82, 28, 3, 45]
heap_sort(random_list)
print(random_list)
