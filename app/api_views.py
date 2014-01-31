from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from sendmail.mail import SendMail
from flask.views import MethodView
from page.forms import CallbackSubmit
from models import Callbacks, CallbackDetails
from flask import abort, jsonify, request, url_for, make_response
from app import api, app, db
import datetime


details = {'updated':fields.DateTime,
           'details':fields.String,
           'status':fields.String,
}
callback_fields = {
    'id': fields.String,
    'ddi': fields.String,
    'name': fields.String,
    'phone': fields.String,
    'ticket': fields.String,
    'platform': fields.String,
    'details': fields.Nested(details),
    'created': fields.DateTime,
    #'uri': fields.Url('callback')
}

class CallbackListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name',
                                   type=str,
                                   required=True,
                                   help="No contact name given",
                                   location="json"
                                   )
        self.reqparse.add_argument('platform',
                                   type=str,
                                   required=True,
                                   help="No platform given",
                                   location="json"
                                   )
        self.reqparse.add_argument('details',
                                   type=str,
                                   required=True,
                                   help="No details given",
                                   location="json"
                                   )
        self.reqparse.add_argument('phone',
                                   type=int,
                                   required=True,
                                   help="No phone number given",
                                   location="json"
                                   )
        self.reqparse.add_argument('ddi',
                                   type=int,
                                   required=True,
                                   help="No DDI given",
                                   location="json"
                                   )
        self.reqparse.add_argument('ticket',
                                   type=str,
                                   help="Ticket Information",
                                   location="json"
                                   )
        super(CallbackListAPI, self).__init__()

    def get(self):
        cb_list = []
        callbacks = Callbacks.query.all()
        for callback in callbacks:
            cb = {'id':callback.id,
                  'name':callback.name,
                  'phone':callback.phone,
                  'ddi':callback.ddi,
                  'ticket':callback.ticket,
                  'details':[],
                  'platform':callback.platform,
                  'created':callback.created,
                  }
            deets = callback.cb_details.all()
            for deet in deets:
                details = {'updated':deet.updated,
                           'details':deet.details,
                           'status':deet.status,
                    }
                cb['details'].append(details)
            cb_list.append(cb)
        return { 'callbacks': map(lambda t: marshal(t, callback_fields), cb_list) }

    def post(self):
        cb_list = []
        args = self.reqparse.parse_args()
        cb = {'name':args['name'],
              'phone':args['phone'],
              'ddi':args['ddi'],
              'ticket':args['ticket'],
              'platform':args['platform'],
              'created':datetime.datetime.utcnow(),
              }
        insert = Callbacks(**cb)
        db.session.add(insert)
        db.session.commit()
        id = Callbacks.query.get(insert.id)
        cb['id'] = id.id
        cb['details'] = []
        cb_details = {'details':args['details'],
                      'updated':datetime.datetime.utcnow(),
                      'status':'New',
                      'comments':id
                      }
        cb['details'].append(cb_details)
        details = CallbackDetails(**cb_details)
        db.session.add(details)
        db.session.commit()
        #case = Callbacks.query.filter_by(
        return { 'callback': marshal(cb, callback_fields) }, 201


class CallbackAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name',
                                   type=str,
                                   help="No contact name given",
                                   location="json"
                                   )
        self.reqparse.add_argument('status',
                                   type=str,
                                   help="No contact name given",
                                   location="json"
                                   )
        self.reqparse.add_argument('platform',
                                   type=str,
                                   help="No platform given",
                                   location="json"
                                   )
        self.reqparse.add_argument('details',
                                   type=str,
                                   help="No details given",
                                   location="json"
                                   )
        self.reqparse.add_argument('phone',
                                   type=int,
                                   help="No phone number given",
                                   location="json"
                                   )
        self.reqparse.add_argument('ddi',
                                   type=int,
                                   help="No DDI given",
                                   location="json"
                                   )
        self.reqparse.add_argument('ticket',
                                   type=str,
                                   help="Ticket Information",
                                   location="json"
                                   )
        super(CallbackAPI, self).__init__()

    def get(self, id):
        cb_list = []
        callbacks = Callbacks.query.filter_by(id=id)
        for callback in callbacks:
            cb = {'id':callback.id,
                  'name':callback.name,
                  'phone':callback.phone,
                  'ddi':callback.ddi,
                  'ticket':callback.ticket,
                  'details':[],
                  'platform':callback.platform,
                  'created':callback.created,
                  }
            deets = callback.cb_details.all()
            for deet in deets:
                details = {'updated':deet.updated,
                           'details':deet.details,
                           'status':deet.status,
                    }
                cb['details'].append(details)
            cb_list.append(cb)
        callback = filter(lambda t: t['id'] == id, cb_list)
        if len(callback) == 0:
            abort(404)
        return { 'callback' : marshal(callback[0], callback_fields) }

    def put(self, id):
        args = self.reqparse.parse_args()
        id = Callbacks.query.get(id)
        cb = {'name':id.name,
              'phone':id.phone,
              'ddi':id.ddi,
              'ticket':id.ticket,
              'details':[],
              'platform':id.platform,
              'created':datetime.datetime.utcnow(),
              }
        cb_details = {'details':args['details'],
                      'updated':datetime.datetime.utcnow(),
                      'status':args['status'],
                      'comments':id
                      }
        details = CallbackDetails(**cb_details)
        db.session.add(details)
        db.session.commit()
        cb['details'].append(cb_details)
        #case = Callbacks.query.filter_by(
        return { 'callback': marshal(cb, callback_fields) }, 201

#    def put(self, id):
#        callbacks = Callbacks.query.filter_by(id=id)
#        for callback in callbacks:
#            cb = [{'id':int(callback.id),
#                  'name':callback.name,
#                  'phone':callback.phone,
#                  'ddi':int(callback.ddi),
#                  'ticket':callback.ticket,
#                  'status':callback.status,
#                  'details':callback.details,
#                  'platform':callback.platform,
#                  'created':callback.created,
#                  'updated':callback.updated,
#                  }]
#        callback = filter(lambda t: t['id'] == id, cb)
#        if len(callback) == 0:
#            abort(404)
#        callback = callback[0]
#        args = self.reqparse.parse_args()
#        for k, v in args.iteritems():
#            if v != None:
#                callback[k] = v
#        return { 'callback': marshal(callback, callback_fields) }

    def delete(self, id):
        pass

api.add_resource(CallbackListAPI, '/api/v1.0/callbacks', endpoint="endpoints")
api.add_resource(CallbackAPI, '/api/v1.0/callbacks/<int:id>', endpoint="endpoint")

