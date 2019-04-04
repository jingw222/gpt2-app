from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import TextForm
from .. import db
from ..models import Line
from .gpt2.gpt2_model import interact_model


@main.route('/', methods=['GET', 'POST'])
def index():
    form = TextForm()
    if form.validate_on_submit():
        old_text = session.get('text', None)
        if old_text is not None and old_text != form.text.data:
            flash('New input submitted!')
            
        session['text'] = form.text.data
        session['output'] = interact_model(form.text.data)

        line = Line.query.filter_by(text=form.text.data).first()
        if line is None:
            line = Line(
                type='custom',
                text=session.get('text', None),
                output=session.get('output', None))
            db.session.add(line)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True

        return redirect(url_for('.index'))
    return render_template(
        'index.html', form=form,
        text=session.get('text', None),
        output=session.get('output', None)
        )


@main.route('/page/<type>')
def user(type):
    return render_template('page.html', type=type)
