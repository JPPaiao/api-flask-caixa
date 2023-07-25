def order_list_month(data):
    return data['date']

def set_total_day(list_day):
    total = 0

    for day in list_day:
        if day == 'days':
            for row in list_day[day]:
                if row['description'] == 'inputs':
                    total += row['value']
                else: 
                    total -= row['value']

    return total

def create_entry(id, value, date, description, text):
    return {
        'id': id,
        'value': value,
        'date': date,
        'description': description,
        'text': text
    }

def set_month(months):
    data_months = {}
    all_months = [
        'janeiro',
        'fevereiro',
        'março',
        'abril',
        'maio',
        'junho',
        'julho',
        'agosto',
        'setembro',
        'outubro',
        'novembro',
        'dezembro'
    ]
    
    for key, value in months.items():
        if key == 'date':
            continue  

        day, month, year = value['date'].split('/')
        month_name = all_months[int(month)]

        for column in value['columns']:
            entry = create_entry(id=1, value=value[column], date=value['date'], description=key, text=column)

            if month_name not in data_months:
                data_months[month_name] = {}

            if int(day) not in data_months[month_name]:
                data_months[month_name][int(day)] = {
                    'total_day': 0,
                    'days': []
                }

            data_months[month_name][int(day)]['days'].append(entry)
    
    for month in data_months:
        for day in data_months[month]:
            total_day = set_total_day(data_months[month][day])
            data_months[month][day]['total_day'] = total_day

    return data_months

