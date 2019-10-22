from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)

from flask_login import current_user, login_required
from flaskblog.universe import models
from flaskblog.universe.forms import InputForm

universe = Blueprint('universe', __name__)


@universe.route('/nlp', methods=['GET', 'POST'])
@login_required
def nlp():
    query = models.QueryMapper()

    content = ''
    final_query = ''
    if request.method == 'POST':
        content = request.form['input_string']
        flash('Successful request!', category='success')

        final_query = query.get_results(str(request.form['input_string']))
        # print(input_string)
        # input_string.resample('4W').sum().plot()

    form = InputForm()

    return render_template('universe/nlp.html',  title='Nlp Tester', form=form, legend='NLP ENGINE', results=content, test=final_query)
