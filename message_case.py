def fun(message):

    match message:

        case [1,val,val2]:
            print(val,val2)
        case 2:
            print("two")


if __name__ == "__main__":

    fun((1,2,3))

