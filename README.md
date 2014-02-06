# Callback
==================

### Overview

A simple API driven web application to track the calls that need to be 
transferred.  It sends out an email when a new request is made, adds it to a
list to be monitored.  You can go view each one, where you can see all notes
regarding the callback.  You can update the callback, which also sends out an
email, same when updating the status.

### Installation

`git clone https://github.com/3cko/callbacks.git`

Once in the repo:

`python virtualenv.py flask`

`flask/bin/pip -r Requirements.txt`

`python db_create.py`

Once you have your servers IP, run the application from within:

`flask/bin/python run.py runserver -h xxx.xxx.xxx.xxx -p 8182`

### Usage

#### Web

Load up the URL in your favorite browser.

#### API

The API only accepts and returns JSON

| HTTP Method  | URI                                             |                     Action |
| :----------- | :---------------------------------------------- | :------------------------- |
| GET          | http://[hostname]/api/callbacks            | Retrieve list of callbacks |
| GET          | http://[hostname]/api/callbacks/[callback_id] | Retrieve a callback        |
| POST         | http://[hostname]/api/callbacks            | Create new callback        |
| PUT          | http://[hostname]/api/callbacks/[callback_id] | Update a callback          |

##### POST request accepts all fields

- **ddi**: account number. Numeric type.
- **name**: persons name. String type.
- **phone**: persons phone number. Numeric type.
- **ticket**: persons associated ticket number. Numeric type.
- **platform**: windows or linux?  String type.
- **details**: detail informatuon about the call.  Text type.
- **status**: the status of the callback.  String type

##### PUT requests accept 2 fields

- **details**: detail informatuon about the call.  Text type.
- **status**: the status of the callback.  String type

##### All fields

- **id**: unique identifer for callbacks. Numeric type.
- **ddi**: account number. Numeric type.
- **name**: persons name. String type.
- **phone**: persons phone number. Numeric type.
- **ticket**: persons associated ticket number. Numeric type.
- **platform**: windows or linux?  String type.
- **details**: detail informatuon about the call.  Text type.
- **status**: the status of the callback.  String type.
- **created**: when the callback was created.  DateTime type.
- **updated**: when the callback was last updated. DateTime type.

### To-Do

- Better error handling for web interface and the API
- User Login
- Admin Panel
- ~~Consistant updates to the callback list~~
- ~~Email threading~~
- Consider migrating the database to mongodb
- Pageination
- Commenting Code
- Refractor**
- Better docs
