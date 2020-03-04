import hashlib

class Word:

    def __init__(self, word):
        self.word = word
        self.frequency = 1

    def __str__(self):
        return "Word:[{}]\t Frequency:[{}]".format(self.word, self.frequency)

class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = []

        for i in range(capacity):
            self.table.append(None)

        print(">> HashTable Object Created with Capacity:",capacity)

    def hashCode(self, word):
        index = int(hashlib.sha256(word.encode("utf-8")).hexdigest(), 16) % self.capacity
        print("## Index for", word, "is:", index)
        return index

    def put(self, data):

        idx = self.hashCode(data.word.lower())

        if self.table[idx] == None:
            self.size += 1
            self.table[idx] = data
        else:
            word = self.table[idx]
            word.frequency += 1

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

        for data in self.table:
            if data != None:
                print(data)


def main():
    """
    word = "institution"
    hashCode = int(hashlib.sha256(word.encode("utf-8")).hexdigest(), 16) % 100
    print(hashCode)
    """

    review1 = "Really good institution teachers are very helpful and caring also environment of this college is very attractive Proud to be a part of this college"
    review2 = "Best institution Education level is high"
    review3 = "What so ever I am today is due this technology Temple"
    review4 = "Nice place a big also it provides you good education"
    review5 = "Great institution with opportunities for those who want it"

    # revires = [review1, review2, review3, review4, review5]

    word1 = "institution"
    frequency1 = 0
    # We need to find frequency of occurrence of word institution in above 5 reviews

    # 1. Put the data in an effective data structures
    #    > HashTable | Capacity -> number of Words in number of Reviews
    # 2. Implement an Algorithm to calculate frequency
    #    > Whenever a collision will occur we will increment the count
    # 3. Implementation of OOPS with Data Structures is preferable :)
    #    > Word : word, frequency

    words1 = review1.split(" ")
    words2 = review2.split(" ")
    words3 = review3.split(" ")
    words4 = review4.split(" ")
    words5 = review5.split(" ")

    capacity = len(words1) + len(words2) + len(words3) + len(words4) + len(words5)

    hTable = HashTable(capacity)

    allWords = []

    allWords.extend(words1)
    allWords.extend(words2)
    allWords.extend(words3)
    allWords.extend(words4)
    allWords.extend(words5)

    print(allWords)
    print(len(allWords))

    for word in allWords:
        hTable.put(Word(word))

    hTable.iterate()



if __name__ == '__main__':
    main()