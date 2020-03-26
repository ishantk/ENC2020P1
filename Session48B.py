# Graph Data Structure
# PS: https://visualgo.net/en/graphds
# G(V, E) | V is Vertices/Nodes and E id Edges

# Graph Data Structure UnDirected/BiDirectional Graph
# Kind of implementing Facebook Use Case

class User:
    def __init__(self, uid, name, phone, email):
        self.uid = uid
        self.name = name
        self.phone = phone
        self.email = email

    def getUserDetails(self):
        return "{} | {} | {} | {}".format(self.uid, self.name, self.phone, self.email)

class FaceBookGraph:

    def __init__(self):
        self.users = dict() # vertices/nodes in Graph :)
        print(">> FaceBook Graph Created and users are:", self.users, "and size:", len(self.users))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # addVertex
    def registerUser(self, user):
        self.users[user] = [] # empty List is a FriendList | Adjacency List

    # printVertices
    def printUsers(self):

        print("Total Users:", len(self.users))

        keys = self.users.keys()

        for key in keys:
            print(key.getUserDetails())

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # addEdge
    def connectUser(self, user1, user2):

        # For UnDirected Graph we got connection both ways
        # Kind of adding an edge and constructing Adjacency List in your graph
        self.users[user1].append(user2)
        self.users[user2].append(user1)

    # printGraphWithAdjacencyList
    def printUsersWithFriendList(self):

        print("Total Users:", len(self.users))

        keys = self.users.keys()

        for key in keys:
            print("User:", key.getUserDetails())
            friendList = self.users[key]
            for friend in friendList:
                print("Friend:", friend.getUserDetails())

            print("====================")

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def main():

    u0 = User(0, "John", "90909 89898", "john@example.com")
    u1 = User(1, "Jennie", "87665 89898", "jennie@example.com")
    u2 = User(2, "Sia", "91909 33898", "sia@example.com")
    u3 = User(3, "Leo", "89909 44898", "leo@example.com")
    u4 = User(4, "Fionna", "88909 99998", "fionna@example.com")
    u5 = User(5, "Kim", "90111 77778", "kim@example.com")
    u6 = User(6, "Mike", "91231 11198", "mike@example.com")

    graph = FaceBookGraph()

    graph.registerUser(u0)
    graph.registerUser(u1)
    graph.registerUser(u2)
    graph.registerUser(u3)
    graph.registerUser(u4)
    graph.registerUser(u5)
    graph.registerUser(u6)

    graph.printUsers()

    graph.connectUser(u0, u1)
    graph.connectUser(u0, u2)
    graph.connectUser(u1, u2)
    graph.connectUser(u1, u3)
    graph.connectUser(u2, u4)
    graph.connectUser(u3, u4)
    graph.connectUser(u4, u5)
    graph.connectUser(u5, u6)

    graph.printUsersWithFriendList()


if __name__ == '__main__':
    main()


