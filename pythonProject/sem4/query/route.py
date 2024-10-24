from flask import render_template, Blueprint, current_app
from database.select import select_dict
from sem4.access import group_required

blueprint_query = Blueprint('query_bp', __name__, template_folder='templates')

@blueprint_query.route('/')

# неявное обращение к декоратору, декорируем функцию query_index
@group_required
def query_index():
    prod_category = 1
    _sql = f"""select prod_name, prod_measure, prod_price from product
               where prod_category = {prod_category}"""
    result = select_dict(current_app.config['db_config'], _sql)

    if result:
        prod_title = 'Результат из БД'
        return render_template('dynamic.html', prod_title = prod_title, products = result)
    else:
        return 'Результат не получен'

