from flask import Flask, current_app, g, has_app_context, jsonify
from flask.cli import with_appcontext
import sqlite3

DATABASE_PATH = '../hazmat-parser/instance'

def get_db():
    if has_app_context():
        if 'db' not in g:
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row

        return g.db
    else:
        db = sqlite3.connect(DATABASE_PATH + '/hazmat-parser.sqlite')
        return db


def build_autocomplete(db):
    db_query = '''
    SELECT proper_shipping_name AS label, unna_code AS value
    FROM hazmat_table
    JOIN proper_shipping_names ON hazmat_table.row_id = proper_shipping_names.row_id
    WHERE unna_code IS NOT NULL
    '''
    cursor = db.execute(db_query)
    results = cursor.fetchall()

    # Transform results into the desired format
    autocomplete_list = [{'label': row[0], 'value': row[1]} for row in results]
    return autocomplete_list

print(build_autocomplete(get_db()))
