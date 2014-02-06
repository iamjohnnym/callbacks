from internalapi.api import GlobalApi
from sendmail.mail import SendMail
from page.forms import CallbackSubmit, CallbackUpdate
from models import Callbacks
from flask import render_template, flash, redirect, session, url_for, request, Markup
from app import app, db
import datetime
import requests


@app.route('/callbacks/add', methods = ['GET', 'POST'])
def add():
    iapi = GlobalApi()
    form = CallbackSubmit()
    if form.validate_on_submit():
        created = str(datetime.datetime.now())
        updated = str(datetime.datetime.now())
        vars = {'ddi':form.ddi.data,
                'ticket':form.ticket.data,
                'name':form.name.data,
                'phone':form.phone.data,
                'platform':form.platform.data,
                'details':[
                    { 'details': form.details.data,
                      'updated':updated,
                      'private':None}
                    ]
                }
        try:
            id = iapi.post('callbacks', vars)
        except requests.exceptions.RequestException,e:
            print e
        sendmail = SendMail(recipient='john.martin@rackspace.com',
                            status='New',
                            id=id['id'],
                            **vars)
        message = sendmail.run()
        msg = Markup("New callback has been created for {0}.  To view, go here: <a href=\"/callbacks/{1}\">View</a>".format(vars['name'], id['id']))
        flash(msg)
        return redirect(url_for('index'))
    return render_template("sb-admin/add.html",
        title='CallBack Form',
        test='Create a Callback Email',
        form=form,
        )

@app.route('/', methods=['GET', 'POST'])
@app.route('/callbacks', methods=['GET', 'POST'])
def index():
    iapi = GlobalApi()
    callbacks = iapi.get_all('callbacks')
    return render_template("sb-admin/list.js.html",
        title='Current Callbacks',
        test='Current Callbacks',
        callbacks=callbacks,
        )

@app.route('/callbacks/<case>', methods=['GET', 'POST', 'PUT'])
def callback(case):
    iapi = GlobalApi()
    form = CallbackUpdate()
    callbacks = iapi.get('callbacks', case)
    if form.validate_on_submit():
        updated = str(datetime.datetime.now())
        dictionary = {'details':{'add':{'details': form.details.data,
                      'status': form.status.data,
                      'private': form.private.data,
                      'updated': updated,
                      }}}
        put = iapi.put('callbacks', case, dictionary)
        form = CallbackUpdate()
        # redundant.  fix the iapi.put() to return the correct data
        callbacks = iapi.get('callbacks', case)
#|        sendmail = SendMail(recipient='john.martin@rackspace.com',
#|                        ddi=callbacks['callback']['ddi'],
#|                            name=callbacks['callback']['name'],
#|                            phone=callbacks['callback']['phone'],
#|                            ticket=callbacks['callback']['ticket'],
#|                            platform=callbacks['callback']['platform'],
#|                            id=case,
#|                            **dictionary
#|                            )
#|        message = sendmail.run()
        return render_template("sb-admin/details.js.html",
            title='Current Callbacks',
            test='Current Callbacks',
            callbacks=callbacks,
            form=form
            )
    return render_template("sb-admin/details.js.html",
        title='Current Callbacks',
        test='Current Callbacks',
        callbacks=callbacks,
        form=form
        )
