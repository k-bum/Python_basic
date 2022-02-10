a = [1, 2, 3, 4, 5]
for i in range(10) :
    try :
        print(10 / i)
        print(a[i])
    except ZeroDivisionError :
        print("Error")
        print("Not divided by 0")
    except IndexError as e :
        print(e)
    except Exception as e : # Exception이 어디서 발생했는지 알기 어렵다.
        print(e)