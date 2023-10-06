from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input values from the form
        new_row = [float(request.form.get(f'feature_{i}')) for i in range(1, 23)]

        # Load the model
        model = pickle.load(open('model.pkl', 'rb'))

        # Predict using the loaded model
        prediction = model.predict([new_row])

        return render_template('result.html', prediction=prediction[0])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    