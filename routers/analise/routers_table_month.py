def set_total_month(data):
    total = 0
    for day in data:
        if 'date' !=  day != 'total' and day != 'columns':
            total += data[day]

    return total

def set_columns_day(data):
    control_day = {
        "inputs": {
            "columns": [],
        },
        "outputs": {
            "columns": [],
        },
        "date": data[0]['date']
    }

    for row in data:
        if row['description'] == 'inputs':
            if not control_day['inputs'].get(row['column']):
                control_day['inputs'][row['column']] = 0
                if row['column'] not in control_day['inputs']['columns']:
                    control_day['inputs']['columns'].append(row['column'])
        else:
            if not control_day['outputs'].get(row['column']):
                control_day['outputs'][row['column']] = 0
                if row['column'] not in control_day['outputs']['columns']:
                    control_day['outputs']['columns'].append(row['column'])

    for row in data:
        row['value'] = int(row['value'])
        if row['description'] == 'inputs':
            control_day['inputs'][row['column']] += row['value']
            control_day['inputs']['date'] = row['date']
        else:
            control_day['outputs'][row['column']] += row['value']
            control_day['outputs']['date'] = row['date']

    inputsTotal = set_total_month(control_day['inputs'])
    outputsTotal = set_total_month(control_day['outputs'])

    control_day['inputs']['total'] = inputsTotal
    control_day['outputs']['total'] = outputsTotal

    return control_day

def set_month_day(data):
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
    new_month = list(map(lambda x: set_columns_day(month[x]), set_dates))

    return new_month[0]
