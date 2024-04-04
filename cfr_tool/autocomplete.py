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
    autocomplete_list = [{'label': row[0].strip().replace('\n',''), 'value': row[1]} for row in results]
    return autocomplete_list
