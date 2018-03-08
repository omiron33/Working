class Call(object):
    def __init__(self, ident, name, phone, time, reason):
        self.id = ident
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
        

    def display_all(self):
        print self.id, self.name, self.phone, self.time, self.reason
        return self

class CallCenter(object):
    def __init__(self):
        self.call_list = []
        self.queue = 0

    
    def add(self, user):
        self.call_list.append(user)
        self.queue += 1

    def printIt(self):
        for i in range(0,len(self.call_list)):
            print self.call_list[i].name
            print self.call_list[i].phone
        print self.queue

    def remove(self, user):
        self.call_list.pop(0)
        self.queue -= 1

    def ninja(self, phone):
        self.temp = self.call_list.index(phone)
        
        self.call_list.remove(self.temp)

  




user1 = Call(1,"Jane","222-2222","10:00","Disgruntled")
user2 = Call(2,"Jim","333-3333","10:15","Question")
user3 = Call(3,"Jacey","444-4444","12:00","Irritated")
user4 = Call(4,"Bill","555-5555","13:00","Asleep")

colocation = CallCenter()

colocation.add(user1)
colocation.add(user2)
colocation.add(user3)
colocation.add(user4)


colocation.remove(user3)

colocation.printIt()

colocation.ninja("555-5555")

colocationl.printIt()













