# from itertools import combinations
from util import Queue
import random


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(0, numUsers):
            self.addUser(user)

        # Create friendships
        totalFriendships = numUsers * avgFriendships
        times_to_call_addFriendship = totalFriendships // 2

        userIds = range(1, numUsers + 1)

        # make a list of all possible friendship combinations
        friends = []
        for user in userIds:
            for friend in range(user + 1, numUsers + 1):
                friends.append((user, friend))

        # shuffle the list
        random.shuffle(friends)

        friends_to_make = friends[:times_to_call_addFriendship]

        for friendship in friends_to_make:
            self.addFriendship(friendship[0], friendship[1])

        # friendship_combinations = combinations(userIds, 2)
        # print(list(friendship_combinations))
        # shuffle the list

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        path = [userID]

        q.enqueue(path)
        while q.size() > 0:
            current_path = q.dequeue()

            current_node = current_path[-1]

            if current_node not in visited.keys():
                visited[current_node] = current_path
                friends = self.friendships[current_node]

                for friend in friends:
                    path_copy = current_path[:]

                    path_copy.append(friend)

                    q.enqueue(path_copy)


            # if current_node not in visited.keys():
            #     friends = self.friendships[current_node]
            #     visited[current_node] = friends

            #     for friend in friends:
            #         q.enqueue(friend)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
