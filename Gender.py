genderItem = []


def convertGender(gender):        
    if gender == 'man':
        genderItem = [1, 0]
    else:
        genderItem = [0, 1]
    return genderItem


if __name__ == "__main__":
    convertGender(gender="woman")