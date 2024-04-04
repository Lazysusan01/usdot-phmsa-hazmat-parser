from flask import (
    Blueprint, flash, g, make_response, redirect, render_template, request, session, url_for, send_file, send_from_directory    
)

from . import db
from . import clean_text as ct
from . import code_lookup
from . import autocomplete

bp = Blueprint('packaging', __name__)
        

def check_packaging(unna, db):
    db.execute("SELECT pg FROM hazmat_table WHERE unna_code = '{}'".format(unna))
    pgs = db.fetchall()
    if len(pgs) > 1:
        #TO DO: render packaging.html so it shows the multiple PG options for the user to select.
        render_template('packaging.html')

@bp.route('/help', methods=['GET'])
def help():
    return render_template('help.html')

# @bp.route('/static/<path:path>')
# def static_file(path):
#     return send_file(path)

@bp.route('/',  methods=('GET', 'POST'))
def packaging():
    autocomplete_data = autocomplete.build_autocomplete(db.get_db())
    if request.method == 'POST':
        un_id = request.form['un_id']
        try:
            int(un_id)
            un_id=f"UN{un_id}"
        except:
            pass
        bulk = request.form.get('bulk')
        hazmat_db = db.get_db()
        if not request.form.get('packing-group'):
            #check_packaging(un_id, hazmat_db)
            pg = None
        else:
            pg = request.form['packing-group']
        error = None
        if not un_id:
            error = 'UNID is required.'
        else:
            render_results = code_lookup.build_results(
                un_id, 
                True if bulk == "on" else False,
                pg,
                hazmat_db)
        if render_results:
            return render_template(
                'packaging.html', len=len(render_results['text']), results=render_results, autocomplete_data=autocomplete_data)
        else:
            flash('UN number does not exist')
            return render_template('packaging.html', autocomplete_data=autocomplete_data)
        flash(error)
    return render_template('packaging.html', autocomplete_data=autocomplete_data)