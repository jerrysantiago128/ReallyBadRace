import random


class Racer:
    def __init__(self):
        self.speed = None

    def __int__(self, name, speed):
        self.name = name
        self.speed = speed

    def calc_speed(self):
        self.speed = random.randrange(0, 5, 1)
        return self.speed


def race_start(list1, list2):
    for position in range(10):
        list1.append(" ___ ")
    for position in range(10):
        list2.append(" ___ ")

    print(list1)
    print(list2)


def show_race(d1, d2, list1, list2):
    length = len(list1)
    for position in range(10):
        if list1[position] == r1.name:
            list1[position] = " ___ "
        elif list1[d1 - 1] == " ___ ":
            list1[d1 - 1] = r1.name

    for position in range(10):
        if list2[position] == r2.name:
            list2[position] = " ___ "
        elif list2[d2 - 1] == " ___ ":
            list2[d2 - 1] = r2.name

    print(list1)
    print(list2)


r1 = Racer()
r1.name = "Patricia"
r1.speed = 1
r2 = Racer()
r2.name = "Marco"
r2.speed = 1

distance1, distance2 = r1.speed, r2.speed
START = 0
END = 10
l1 = []
l2 = []

race_start(l1, l2)
print(f' {r1.name} is racing at: {r1.speed} mph, putting them at position:  {distance1}')
print(f'{r2.name} is racing at: {r2.speed} mph, putting them at position: {distance2}')

while distance1 < END and distance2 < END:

    if distance1 > distance2:
        print(f' {r1.name} is in first place')
    elif distance1 == distance2:
        print(f"'Both racer's are tied'")
    else:
        print(f' {r2.name} is in first place')

    if distance1 + r1.calc_speed() >= END:
        distance1 = END
    elif distance2 + r2.calc_speed() >= END:
        distance2 = END
    else:
        distance1 += r1.calc_speed()
        distance2 += r2.calc_speed()

    if r1.speed > r1.calc_speed():
        print(f' {r1.name} slows down: {r1.speed} mph, putting them at position: {distance1}')
    elif r1.speed < r1.calc_speed():
        print(f' {r1.name} speeds up to: {r1.speed} mph, putting them at position: {distance1}')
    else:
        print(f' {r1.name} is racing at: {r1.speed} mph, putting them at position: {distance1}')

    if r2.speed > r2.calc_speed():
        print(f' {r2.name} slows down: {r2.speed} mph, putting them at position:  {distance2}')
    elif r2.speed < r2.calc_speed():
        print(f' {r2.name} speeds up to: {r2.speed} mph, putting them at position:  {distance2}')
    else:
        print(f' {r2.name} is racing at: {r2.speed} mph, putting them at position:  {distance2}')

    show_race(distance1, distance2, l1, l2)


if distance1 >= END > distance2:
    print(f'Congratulations {r1.name}! You won the race')

elif distance2 >= END > distance1:
    print(f'Congratulations {r2.name}! You won the race')


print(f' {r1.name} final speed: {r1.speed} and final distance: {distance1}')
print(f' {r2.name} final speed: {r2.speed} and final distance: {distance2}')
