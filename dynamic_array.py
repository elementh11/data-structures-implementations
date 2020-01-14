class ArrayList:
    '''
    ArrayList class implements a dynamic array using static arrays
    '''

    def __init__(self, size=10):
        self.capacity = size # maximum memory capacity
        self.list = [None] * self.capacity # allocate array
        self.size = 0 # current actual size (number of elements)

    def add(self, value):
        """
        Append element at the end of array
        """
        if self.size == self.capacity: # check if enough memory capacity
            self._increase_size()
        self.list[self.size] = value
        self.size += 1

    def _increase_size(self):
        """
        doubles the array capacity
        """
        new_max_size = self.capacity * 2 # double memory size
        new_list = [None] * new_max_size
        for i in range(0, self.capacity): # copy old list to new list
            new_list[i] = self.list[i]
        self.capacity = new_max_size
        self.list = new_list

    def search(self, index):
        """
        locate the element at specified index
        """
        if index >= self.size or index < 0:
            raise Exception('Invalid index')

        return self.list[index]

    def delete(self, index):
        """
        remove the element at specified index
        """
        if index >= self.size or index < 0:
            raise Exception('Invalid index')

        # shift list from deleted index onwards
        # element before index are not affected by deletion
        for _ in range(index, self.size): 
            self.list[index] = self.list[index+1]
        self.size -= 1
