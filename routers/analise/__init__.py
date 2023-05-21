from flask import Blueprint

analise_blueprint = Blueprint('analise', __name__)

def set_dates(datas):
    def find_index_by_date(lista, data):
        for i, item in enumerate(lista):
            if item["date"] == data:
                return i
        return -1

    def update_row_db(rowDB, rowUpdate):
        newRow = {}

        for row in rowDB:
            newRow[row] = rowDB[row]

        for row in rowUpdate:
            if 'date' != row != 'total' and row != 'columns':
                if row not in newRow['columns']:
                    newRow['columns'].append(row)
                    newRow[row] = rowUpdate[row]
                else:
                    newRow[row] += rowUpdate[row]

        newRow['total'] += rowUpdate['total']

        return newRow

    date = datas['date']
    indice = find_index_by_date(dbUsers, date)

    if indice != -1:
        description_input = 'inputs'
        description_output = 'outputs'
        
        update_data_inputs = datas[description_input]
        row_db_inputs = dbUsers[indice][description_input]
        update_data_outputs = datas[description_output]
        row_db_outputs = dbUsers[indice][description_output]

        new_datas_inputs = update_row_db(row_db_inputs, update_data_inputs)
        new_datas_outputs = update_row_db(row_db_outputs, update_data_outputs)

        dbUsers[indice][description_input].update(new_datas_inputs)
        dbUsers[indice][description_output].update(new_datas_outputs)
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
        "date": "12/05/2023",
        "inputs": {
            "asd": 300,
            "caixa": 300,
            "cartao": 300,
            "columns": [
                "caixa",
                "cartao",
                "pix",
                "pix",
                "asd"
            ],
            "date": "12/05/2023",
            "pix": 600,
            "total": 1500
        },
        "outputs": {
            "asd": 300,
            "bvs": 300,
            "columns": [
                "asd",
                "qw",
                "bvs",
                "fd"
            ],
            "date": "12/05/2023",
            "fd": 10,
            "qw": 300,
            "total": 910
        }
    },
    {
        "date": "13/05/2023",
        "inputs": {
            "asd": 300,
            "caixa": 300,
            "cartao": 300,
            "columns": [
                "caixa",
                "cartao",
                "pix",
                "pix",
                "asd"
            ],
            "date": "13/05/2023",
            "pix": 600,
            "total": 1500
        },
        "outputs": {
            "asd": 300,
            "bvs": 300,
            "columns": [
                "asd",
                "qw",
                "bvs",
                "fd"
            ],
            "date": "13/05/2023",
            "fd": 10,
            "qw": 300,
            "total": 910
        }
    },
    {
        "date": "14/05/2023",
        "inputs": {
            "asd": 500,
            "caixa": 500,
            "cartao": 500,
            "columns": [
                "caixa",
                "cartao",
                "pix",
                "pix",
                "asd"
            ],
            "date": "14/05/2023",
            "pix": 500,
            "total": 1500
        },
        "outputs": {
            "asd": 300,
            "bvs": 300,
            "columns": [
                "asd",
                "qw",
                "bvs",
                "fd"
            ],
            "date": "14/05/2023",
            "fd": 10,
            "qw": 300,
            "total": 910
        }
    },
]
