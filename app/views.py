from flask import render_template, redirect, url_for
from app import app
from .forms import SearchForm
from app import util as u
from config import THEME

@app.route('/')
@app.route('/main', methods=['GET', 'POST'])
def main():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        return redirect(url_for('search_results', query=search_form.search.data))
    return render_template(THEME + '_index.html', form=search_form)#main.html is the regular render template

@app.route('/search_results/<query>')
def search_results(query):
    results = u.db_query(query)
    return render_template(THEME + '_search_results.html',
                           query=query,
                           results=results)