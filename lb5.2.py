
import random
name1 = ["інженер", "професор", "балерина", "хлопець", "корова", "мікроб"]
name2 = ["повільно", "страшно", "класно", "Тихо"]
name3 = ["Стоїть", "Грає", "Ходить", "Говорить", "Дивиться"]
list = [name1, name2, name3]
def Random():
    int1 = random.randint(0, len(list)-1)
    print(list[int1][random.randint(0, len(list[int1])-1)])
    list.pop(int1)
    int2 = random.randint(0, len(list) - 1)
    print(list[int2][random.randint(0, len(list[int2])-1)])
    list.pop(int2)
    int3 = random.randint(0, len(list) - 1)
    print(list[int3][random.randint(0, len(list[int3])-1)])
Random() 