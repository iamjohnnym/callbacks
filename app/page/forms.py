from flask.ext.wtf import Form
from wtforms import TextAreaField, TextField, BooleanField, validators, ValidationError, IntegerField
from wtforms.validators import Required, NumberRange, Regexp


class CallbackSubmit(Form):
    #rec = TextField('TestRecipient', [validators.Required('Please enter the testing recipient')])
    ddi = IntegerField('DDI',
                    [Required('Please enter the DDI'),
                    Regexp(regex='\d{4,10}',
                           message="Must enter at least 4 digits")])
    ticket = IntegerField('Ticket',
                       [Regexp(regex='\d{4,10}',
                               message='Must enter at least 4 digits')])
    phone = IntegerField('Phone',
                      [Required('Please enter the phone number'),
                      Regexp(regex='\d{10,15}',
                                  message='Must enter 10 digits')])
    name = TextField('Name',
                     [Required('Please enter the contact name')])
    platform = TextField('Platform',
                         [Required('Please enter the Platform, Linux or Windows')])
    details = TextAreaField('Call Details')

class CallbackUpdate(Form):
    status = TextField('Status',
                       [Required('Please enter the status')])
    details = TextAreaField('Call Details')
