from re import A


def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

class Person():

    all_users = []

    def __init__(self, name):
        self.id = len(self.__class__.all_users) + 1
        self.name = name
        self.friends = []
        self.__class__.all_users.append(self)

    def add_friend(self, person):
        if(contains( self.friends, lambda x : person.id == x.id)):
            return False
        self.friends.append(person)
        person.add_friend(self)
        return True

    def get_friends(self):
        return [ friend.id for friend in self.friends ]

    @classmethod
    def get_all_users(cls):
        return [ friend.id for friend in cls.all_users ]

    @classmethod
    def get_user(cls, id):
        for search in cls.all_users:
            if(search.id == id):
                return search
        else:
            return None

    def __repr__(self) -> str:
        	return  str(self.name)+str([ friend.id for friend in self.friends ])

def most_common(lst):
    return max(set(lst), key=lst.count)

def get_top_k_recommended_friends(user_id: int, cutoff_k: int):
    recomemded = []
    #array to push friend recoemndations during the search
    most_repeated = []
    person = Person.get_user(user_id)
    #capture de person to get de list of friends for that user
    #iterarte over the user direct friends
    aux = {}
    for friend in person.get_friends():#iterate over the user list of friends
        current_friend = Person.get_user(friend)#for every friend evaluate candidates
        for candidate in current_friend.get_friends():
            aux[candidate] = 0
            if user_id != candidate:#validates the person is not already friend of this candidate
                aux[candidate] = aux[candidate] + 1 #count candidates frecuency

    

    def get_max(dict_items: dict):#function that gets de top index from a dictonary
        top = None
        topValue = 0
        for key, value in dict_items.items():
            if(value > topValue):
                top = key
                topValue = value
        return top

    for leader in range(0,cutoff_k):#reatrive only the n elements of recomendations
        if(leader - 1>= len(aux.items())):#verify if already has fill the query
            return most_repeated
        max_item = get_max(aux)#get the most valuable candidate
        if(max_item == None):#verify if the user has no friends
            return []
        max_value = aux.pop(max_item)#remove the candidate from the aux dictionary
        if leader < cutoff_k:
            most_repeated.append(max_item)#append the candidate to the list of most_repeated person and return
    return most_repeated

#just testing
alice = Person("Alice")
dan = Person("Dan")
bob = Person("Bob")
eve = Person("Eve")
charlie = Person("Charlie")
carlos = Person("Carlos")
alessandro = Person("Alessandro")
ivan = Person("Ivan")
abel = Person("Abel")
samuel = Person("Samuel")



dan.add_friend(eve)
dan.add_friend(ivan)
dan.add_friend(alessandro)


alice.add_friend(bob)
alice.add_friend(dan)
alice.add_friend(abel)

bob.add_friend(carlos)
bob.add_friend(ivan)
bob.add_friend(eve)
bob.add_friend(charlie)

abel.add_friend(alessandro)

print([Person.get_user(pana).name for pana in get_top_k_recommended_friends(alice.id, 4) ])