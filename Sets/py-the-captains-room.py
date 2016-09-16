"""
https://www.hackerrank.com/challenges/py-the-captains-room
language: Python 3

Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

Sample Output

8
"""

_ = int(input())
room_numbers = [int(x) for x in input().split()]

captain_room = set()
tourist_rooms = set()

for n in room_numbers:
    if n not in tourist_rooms:
        if n not in captain_room:
            captain_room.add(n)
        else:
            captain_room.remove(n)
            tourist_rooms.add(n)
            
print(captain_room.pop())