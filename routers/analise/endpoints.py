from . import analise_blueprint
from .table_month import set_month, order_list_month
from .routers_table_month import set_month_day
from flask import request

@analise_blueprint.route('/tableMonth', methods=['POST'])
def table_month():
    req = request.get_json()
    month = req

    if month != None:
        month.sort(key=order_list_month)
        month = set_month_day(month)
        month = set_month(month)

        return month

    return month