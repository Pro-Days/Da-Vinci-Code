###2인용
import random


Block_list = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122]

User1_list = [random.choice(Block_list) for i in range(4)]
for i in User1_list:
    Block_list.remove(i)
User2_list = [random.choice(Block_list) for i in range(4)]
for i in User2_list:
    Block_list.remove(i)

print(User1_list, User2_list, Block_list)

User1_list.sort()
User2_list.sort()

print(User1_list, User2_list, Block_list)


if 121 in User1_list: