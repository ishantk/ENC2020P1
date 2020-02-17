import threading
import requests
"""
class PrintingTask:

    def printDocument(self, name, copies):
        for i in range(1, copies+1):
            print(">> Printing {} Copy #{}".format(name, i))
"""

class FetchNewsTask(threading.Thread):

    def run(self):
        url = "http://newsapi.org/v2/everything?q=bitcoin&from=2020-01-17&sortBy=publishedAt&apiKey=31c21508fad64116acd229c10ac11e84"
        response = requests.get(url)
        print(response.text)

# IS-A Relationship -> PrintingTask IS-A Thread
class PrintingTask(threading.Thread):

    """
    def __init__(self, name, copies):
        threading.Thread.__init__(self) # Execute Parent's __init__
        self.name = name
        self.copies = copies
    """

    def addPrintingDetails(self, name, copies):
        self.name = name
        self.copies = copies

    def run(self):
        for i in range(1, self.copies+1):
            print(">> Printing {} Copy #{}".format(self.name, i))


def main():
    print(">> App Started")

    task = PrintingTask()
    task.addPrintingDetails("LearningPython.pdf", 10)
    newsTask = FetchNewsTask()
    # task.printDocument("LearningPython.pdf", 10)
    task.start()
    newsTask.start()

    for i in range(1, 11):
        print(">> i is:", i)

    print(">> App Finished")


if __name__ == "__main__":
    main()


# Parallel Programming i.e. Asynchronous Tasks in the Background :)