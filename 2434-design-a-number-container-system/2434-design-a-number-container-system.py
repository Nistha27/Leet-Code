class NumberContainers(object):

    def __init__(self):
        self.index_to_number = {}  # Maps index to number
        self.number_to_indices = {}  # Maps number to a min-heap of indices
        self.valid_indices = {}


    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.number_to_indices:
                self.valid_indices[old_number].discard(index)  # Mark old index as invalid
        
        self.index_to_number[index] = number
        if number not in self.number_to_indices:
            self.number_to_indices[number] = []
            self.valid_indices[number] = set()
        
        heapq.heappush(self.number_to_indices[number], index)
        self.valid_indices[number].add(index)
        

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number in self.number_to_indices and self.number_to_indices[number]:
            while self.number_to_indices[number] and self.number_to_indices[number][0] not in self.valid_indices[number]:
                heapq.heappop(self.number_to_indices[number])  # Remove invalid indices
            
            if self.number_to_indices[number]:
                return self.number_to_indices[number][0]  # Get the smallest index
        return -1



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)