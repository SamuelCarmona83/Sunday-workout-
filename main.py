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
    for friend in person.get_friends():#iterate over the user list of friends
        current_friend = Person.get_user(friend)#for every friend
        #if len(recomemded) < cutoff_k:
        for candidate in current_friend.get_friends():
            if user_id != candidate:
                recomemded.append(candidate)
                
    #at here you have at recommended a long list with the the reaped values of the more common friends
    #now its matter of intarate over that list a retive the most commons under de cutoff value and return it
    #most_recc
    aux = {}
    for item in set(recomemded):
        count = 0
        for elm in recomemded:
            if(item == elm):
                count = count + 1
        aux[item] = count    
    

    def get_max(dict_items: dict):
        top = None
        topValue = 0
        for key, value in dict_items.items():
            if(value > topValue):
                top = key
                topValue = value
        return top

    for leader in range(0,cutoff_k):
        if(leader - 1>= len(aux.items())):
            return most_repeated
        max_item = get_max(aux)
        if(max_item == None):
            return []
        max_value = aux.pop(max_item)
        if leader < cutoff_k:
            most_repeated.append(max_item)
    return most_repeated


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
dan.add_friend(alessandro)


alice.add_friend(bob)
alice.add_friend(dan)
alice.add_friend(abel)

bob.add_friend(carlos)
bob.add_friend(ivan)
bob.add_friend(eve)
bob.add_friend(charlie)

abel.add_friend(alessandro)

print([Person.get_user(pana).name for pana in get_top_k_recommended_friends(samuel.id, 2) ])