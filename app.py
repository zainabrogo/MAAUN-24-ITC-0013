from flask import Flask, render_template, request, redirect
from models import Business

app = Flask(__name__)

businesses = []
recent_stack = []   # Stack for recently added businesses


@app.route('/')
def home():
    return render_template('home.html', businesses=businesses)


@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        location = request.form['location']

        new_business = Business(name, category, location)

        businesses.append(new_business)

        # Stack feature
        recent_stack.append(new_business)

        return redirect('/')

    return render_template('add.html')


@app.route('/recent')
def recent():
    return render_template('home.html', businesses=recent_stack[-5:])


if __name__ == '__main__':
    app.run(debug=True)