from . import analise_blueprint
from flask import request

def set_total_month(data):
    total = 0
    for day in data:
        if 'date' !=  day != 'total':
            total += data[day]

    return total

def arrange_list(data):
    control_day = {
        'date': '',
        'Caixa': 0,
        'Cartao': 0,
        'Pix': 0,
        'Ifood': 0,
        'total': 0
    }

    for row in data:
        control_day['date'] = row['date']
        control_day[row['column']] += row['value']

    total = set_total_month(control_day)
    control_day['total'] += total
    return control_day

def set_month(data):
    month = {}
    new_month = []
    set_dates = []
    date = data[0]['date']
    month[date] = []

    for days in data:
        date = days['date']
        if date not in set_dates:
            set_dates.append(days['date'])
        if days['date'] == date:
            month[days['date']] = []

    date = data[0]['date']
    for row in data:
        if row['date'] in month:
            month[row['date']].append(row)

    date = data[0]['date']
    new_month = list(map(lambda x: arrange_list(month[x]), set_dates))

    return new_month

def order_list_month(data):
    return data['date']

@analise_blueprint.route('/tableMonth')
def table_month():
    req = request.get_json()

    data = req['data']
    data.sort(key=order_list_month)
    month = set_month(data)
    
    return month
