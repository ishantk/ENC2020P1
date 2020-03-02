class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = []  # Assignment : Replace with Your LinkedList Implementation
        for i in range(capacity):
            self.table.append(None)

    def hashCode(self, data):
        idx = id(data) % self.capacity
        return idx

    def put(self, data):

        idx = self.hashCode(data)

        if self.table[idx] == None:
            self.size += 1
        else:
            print(">> COLLISION DETECTED FOR", data)

        self.table[idx] = data
        print(">> Data {} Inserted at Index {}".format(data, idx))

    def find(self, data):
        idx = self.hashCode(data)
        if self.table[idx] == data:
            return idx
        else:
            return -1

    def delete(self, data):
        idx = self.hashCode(data)
        if self.table[idx] == data:
            self.table[idx] = None
            self.size -= 1
            print("Data Deleted", data)
        else:
            print("Data Not Found", data)

    def iterate(self):
        """
        for i in range(self.capacity):
            if self.table[i] != None:
                print(self.table[i])
        """

        for data in self.table:
            if data != None:
                print(data)


"""
class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = []  # Assignment : Replace with Your LinkedList Implementation
        for i in range(capacity):
            self.table.append(None)

    def hashCode(self, data):
        idx = data % self.capacity
        return idx

    def put(self, data):

        idx = self.hashCode(data)

        if self.table[idx] == None:
            self.size += 1

        self.table[idx] = data
        print(">> Data {} Inserted at Index {}".format(data, idx))

    def find(self, data):
        idx = self.hashCode(data)
        if self.table[idx] == data:
            return idx
        else:
            return -1

    def delete(self, data):
        idx = self.hashCode(data)
        if self.table[idx] == data:
            self.table[idx] = None
            self.size -= 1
            print("Data Deleted", data)
        else:
            print("Data Not Found", data)

    def iterate(self):
        
        # for i in range(self.capacity):
        #     if self.table[i] != None:
        #         print(self.table[i])

        for data in self.table:
            if data != None:
                print(data)

def main():

    hTable1 = HashTable(12)
    # hTable2 = HashTable(20)

    hTable1.put(20)
    hTable1.put(12)
    hTable1.put(13)
    hTable1.put(14)
    hTable1.put(19)
    hTable1.put(24)     # Collision

    hTable1.delete(13)
    hTable1.delete(300)

    print("~~~~~~~~~~~~")

    # print(hTable1.table)
    hTable1.iterate()   # Data will be shown as UNORDERED Due to HASHING :)

    print("~~~~~~~~~~~~")

    print(hTable1.size)

if __name__ == "__main__":
    main()

"""