from flask import Blueprint, session, redirect, url_for


blueprint_auth = Blueprint('auth_bp', __name__, template_folder='templates')

@blueprint_auth.route('/')
def auth_index():
    user_group = 'admin'
    user_id = 1
    # заносится в словарь сессии
    session['user_group'] = user_group
    session['user_id'] = user_id
    print('Выполнена аутентификация')

    return redirect(url_for('main_session'))

