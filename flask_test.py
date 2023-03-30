from flask import Flask, request, render_template
import pickle
import Gender
import ClassLevel


app = Flask(__name__)
model = pickle.load(open('randomforest.sav', 'rb'))


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    inputItems = []
    # data = dict(request.headers)
    # inputItems.append(float(data['Age']))
    # classNo = data['Class']
    # gender = data['Gender']
    age = float(request.form['age'])
    inputItems.append(age)
    classNo = request.form['class']
    classNoItem = ClassLevel.convertClass(classNo)
    gender = request.form['gender']

    # if classNo == "first":
    #     classNoItem = [1, 0, 0]
    # elif classNo == "second":
    #     classNoItem = [0, 1, 0]
    # else:
    #     classNoItem = [0, 0, 1]
    inputItems = inputItems + classNoItem
    genderItem = Gender.convertGender(gender)

    # if gender == 'man':
    #     genderItem = [1, 0]
    # else:
    #     genderItem = [0, 1]
    inputItems = inputItems + genderItem

    print(inputItems)

    element = [inputItems]

    possibility = model.predict(element)[0]

    if possibility == 1:
        result = "survival"
    else:
        result = "unsurvival"
    print(result)
    return render_template("index.html", **locals())


# define a route for adding a new item to the list
@app.route('/',  methods=['GET', 'POST'])
def indexPage():
    result = ''
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
