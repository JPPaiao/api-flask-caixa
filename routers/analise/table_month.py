def order_list_month(data):
    return data['date']

def set_month(months):
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
    data_months = {}

    def create_entry(id, value, date, description, text):
        return {
            'id': id,
            'value': value,
            'date': date,
            'description': description,
            'text': text
        }
    
    for key, value in months.items():
        if key == 'date':
            continue  

        day, month, year = value['date'].split('/')
        month_name = all_months[int(month)]

        for column in value['columns']:
            entry = create_entry(id=1, value=column, date=value['date'], description=key, text=value[column])
            
            if month_name not in data_months:
                data_months[month_name] = {}

            if int(day) not in data_months[month_name]:
                data_months[month_name][int(day)] = []

            data_months[month_name][int(day)].append(entry)

    return data_months

