class Heap:
    def __init__(self):
        self.heap = []

    def clear(self):
        self.heap = []

    def add(self, n):
        self.heap.append(n)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        if not self.heap:
            print("CANNOT")
            return
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sift_down(0)
        print(max_value)

    def _sift_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)

    def _sift_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._sift_down(largest)

def main():
    heap = Heap()
    data = []
    with open("input.txt", "r") as file:
        data = [x.strip().split() for x in file.readlines()]
    for command in data:
        if command[0] == "CLEAR":
            heap.clear()
        elif command[0] == "ADD":
            heap.add(int(command[1]))
        elif command[0] == "EXTRACT":
            heap.extract()

if __name__ == "__main__":
    main()