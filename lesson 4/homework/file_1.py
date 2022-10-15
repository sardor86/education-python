list1 = ["Плов", "Торт", "Чебурек"]
list2 = list1.copy()

list1.append("Самса")
list2.append("Какоето блюдо")

if list1 != list2:
    print("Списки не одинаковые")
    print(list1)
    print(list2)