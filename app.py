from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Saluton, mondo!'
    return render_template('index.html', title=title)


@app.route('/about')
def about():
    title = 'About Me'
    return render_template('about.html', title=title)


@app.route('/my-table')
def my_table():
    title = 'My Table'
    table_rows = [
        {
            'pic': 'http://placehold.it/100x100?text=A',
            'name': 'A',
            'notes': 'Lorem ipsum...'
        },
        {
            'pic': 'http://placehold.it/100x100?text=B',
            'name': 'B',
            'notes': 'Ipsum lorem...'
        },
        {
            'pic': 'http://placehold.it/100x100?text=C',
            'name': 'C',
            'notes': 'Ipsum lorem ipsum...'
        },
    ]
    return render_template('my_table.html', title=title, table_rows=table_rows)


if __name__ == '__main__':
    # This only runs if you run the script from the command line, not in the REPL
    app.run(debug=True, port=5001)
