inputVal = input("请输入数字：")
print(inputVal)

match inputVal:
    case "1":
        print("one")
    case "2":
        print("two")
    case "3":
        print("three")
    case _:
        print("other")
