genderItem = []


def convertGender(gender):        
    if gender == 'man':
        genderItem = [0, 1]
    else:
        genderItem = [1, 0]
    return genderItem


if __name__ == "__main__":
    convertGender(gender="woman")