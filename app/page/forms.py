from flask.ext.wtf import Form
from wtforms import TextAreaField, TextField, BooleanField, validators, ValidationError
from wtforms.validators import Required

class CallbackSubmit(Form):
    #rec = TextField('TestRecipient', [validators.Required('Please enter the testing recipient')])
    ddi = TextField('DDI', [validators.Required('Please enter the DDI')])
    ticket = TextField('Ticket')
    phone = TextField('Phone', [validators.Required('Please enter the ticket number')])
    name = TextField('Name', [validators.Required('Please enter the contact name')])
    platform = TextField('Platform', [validators.Required('Please enter the Platform, Linux or Windows')])
    details = TextAreaField('Call Details')
    
class CallbackUpdate(Form):
    status = TextField('Status', [validators.Required('Please enter the status')])
    details = TextAreaField('Call Details')
