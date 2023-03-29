classNoItem = []


def convertClass(classNo):        
    if classNo == "first":
        classNoItem = [1, 0, 0]
    elif classNo == "second":
        classNoItem = [0, 1, 0]
    else:
        classNoItem = [0, 0, 1]
    return classNoItem


if __name__ == "__main__":
    convertClass(classNo="second")