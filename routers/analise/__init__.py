from flask import Blueprint

analise_blueprint = Blueprint('analise', __name__)

def set_dates(datas):
    def find_index_by_date(lists, data):
        for i, item in enumerate(lists):
            if item["date"] == data:
                return i
        return -1

    def update_row_db(row_db, row_update):
        new_row = {}

        for row in row_db:
            new_row[row] = row_db[row]

        for row in row_update:
            if 'date' != row != 'total' and row != 'columns':
                if row not in new_row['columns']:
                    new_row['columns'].append(row)
                    new_row[row] = row_update[row]
                else:
                    new_row[row] += row_update[row]

        new_row['total'] += row_update['total']

        return new_row

    date = datas['date']
    index = find_index_by_date(dbUsers, date)

    if index != -1:
        description_input = 'inputs'
        description_output = 'outputs'

        update_data_inputs = datas[description_input]
        row_db_inputs = dbUsers[index][description_input]
        update_data_outputs = datas[description_output]
        row_db_outputs = dbUsers[index][description_output]

        new_datas_inputs = update_row_db(row_db_inputs, update_data_inputs)
        new_datas_outputs = update_row_db(row_db_outputs, update_data_outputs)

        dbUsers[index][description_input].update(new_datas_inputs)
        dbUsers[index][description_output].update(new_datas_outputs)
    else:
        new_data = {
            'date': date,
            'inputs': datas['inputs'],
            'outputs': datas['outputs'],
            'total': 0
        }
        dbUsers.append(new_data)

    return dbUsers

dbUsers = [
    {
        "date": "12/07/2023",
        "inputs": {
            "mercado": 300,
            "caixa": 300,
            "cartao": 300,
            "columns": [
                "caixa",
                "cartao",
                "pix",
                "mercado",
            ],
            "date": "12/07/2023",
            "pix": 300,
            "total": 1200
        },
        "outputs": {
            "mercado": 300,
            "caixa": 300,
            "cartao": 300,
            "columns": [
                "caixa",
                "cartao",
                "pix",
                "mercado",
            ],
            "date": "12/07/2023",
            "pix": 300,
            "total": 1200
        },
    },
    {
        "date": "13/07/2023",
        "inputs": {
            "mercado": 300,
            "caixa": 300,
            "cartao": 300,
            "columns": [
                "caixa",
                "cartao",
                "pix",
                "mercado",
            ],
            "date": "13/07/2023",
            "pix": 300,
            "total": 1200
        },
        "outputs": {
            "mercado": 300,
            "caixa": 300,
            "cartao": 300,
            "columns": [
                "caixa",
                "cartao",
                "pix",
                "mercado",
            ],
            "date": "13/07/2023",
            "pix": 300,
            "total": 1200
        },
    },
    {
        "date": "14/07/2023",
        "inputs": {
            "mercado": 300,
            "caixa": 300,
            "cartao": 300,
            "columns": [
                "caixa",
                "cartao",
                "pix",
                "mercado",
            ],
            "date": "14/07/2023",
            "pix": 300,
            "total": 1200
        },
        "outputs": {
            "mercado": 300,
            "caixa": 300,
            "cartao": 300,
            "columns": [
                "caixa",
                "cartao",
                "pix",
                "mercado",
            ],
            "date": "14/07/2023",
            "pix": 300,
            "total": 1200
        },
    },
]
