class time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minut = m
        self.second = s

    def sum(self, mehman):
        t3 = time(0, 0, 0)
        t3.hour = self.hour + mehman.hour
        t3.minut = self.minut + mehman.minut
        t3.second = self.second + mehman.second
        if t3.second >= 60 :
            t3.second-=60
            t3.minut+=1
        if t3.minut >= 60 :
            t3.minut-=60
            t3.hour+=1     
        return t3
    
    def sub(self , mehman):
        t3 = time(0, 0, 0)
        t3.hour = self.hour - mehman.hour
        t3.minut = self.minut - mehman.minut
        t3.second = self.second - mehman.second
        if t3.second < 0 :
            t3.second+=60
            t3.minut-=1
        if t3.minut < 0 :
            t3.minut+=60
            t3.hour-=1     
        return t3

    def time_to_s(self):
        sec = (self.hour * 3600) + (self.minut * 60) + self.second
        return sec

    def s_to_time(self):
        t3 = time(0,0,0)
        t3.hour = self // 3600
        t3.minut = (self % 3600) // 60
        t3.second = (self % 3600) % 60
        return t3

    def show(self):
        print(self.hour, ':', self.minut, ':', self.second)

t1 = time(1 , 20, 45)
t2 = time(3 , 30, 4)

x=int(input('your choice: \n1.sum\n2.sub\n3.time to second\n4.second to time\n'))

if x==1:
    a = t1.sum(t2)
    a.show()

if x==2:
    if t1.hour > t2.hour:
        b = t1.sub(t2)
    else:
        b = t2.sub(t1)

    b.show()

if x==3:
    c = t1.time_to_s()
    print(c ,'s')

if x==4:
    d = int(input('please enter second: '))
    e = time.s_to_time(d)
    e.show()