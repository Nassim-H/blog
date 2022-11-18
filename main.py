# This is a sample Python script.
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_genre(genre_id):
    conn = get_db_connection()
    genre = conn.execute('SELECT * FROM posts WHERE genre = ?',
                        (genre_id,)).fetchall()
    conn.close()
    if genre is None:
        abort(404)
    return genre




app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    # Use a breakpoint in the code line below to debug your script.
    return render_template("index1.html", posts=posts)  # Press Ctrl+F8 to toggle the breakpoint.



@app.route('/genre')
def genres():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    # Use a breakpoint in the code line below to debug your script.
    return render_template("genre.html", posts=posts)  # Press Ctrl+F8 to toggle the breakpoint.

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('postblog1.html', post=post)


@app.route('/<string:genre_id>')
def genre(genre_id):
    genre = get_genre(genre_id)
    return render_template('genre.html', genres=genre)

# Press the green button in the gutter to run the script.

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':

        title = request.form['title']
        acroche = request.form['acroche']
        content = request.form['content']
        origine = request.form['origine']
        genre = request.form['genre']


        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title,acroche, content, origine, genre) VALUES (?,?,?, ?, ?)',
                         (title, acroche,  content, origine, genre))
            conn.commit()
            conn.close()
            return redirect('/') #"yes" render_template('create.html', title=title, acroche=acroche, content=content, origine=origine)
    return render_template('create.html')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit1.html', post=post)


@app.route('/index')
def layout():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    # Use a breakpoint in the code line below to debug your script.
    return render_template("index.html", posts=posts)  # Press Ctrl+F8 to toggle the breakpoint.


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
