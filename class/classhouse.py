class Europe:
    lastname = "신"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다." %(self.fullname, where))
    def love(self, other):
        print("%s, %s 축구보러감" %(self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 귀국함" %(self.fullname, other.fullname))

class HouseKim(Europe):
    lastname="조"
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네" %(self.fullname, where, day))

class dodo(Europe):
    lastname = "고"
    def travel(self, where):
        print("%s, %s여행 합류!!" %(self.fullname, where))


pey = Europe("쭌")
pey.travel("프라하")

ozil = HouseKim("성")
ozil.travel('런던',7)

pey.love(ozil)
pey + ozil

koko = dodo("핸도")
koko.travel('부다페스트')
