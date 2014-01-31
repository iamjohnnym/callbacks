import smtplib


class SendMail():
    def __init__(self, recipient, ddi, ticket, name, phone, platform, details, status):
        self.recipient = recipient
        self.platform = platform
        self.details = details
        self.status = status
        self.ticket = ticket
        self.phone = phone
        self.name = name
        self.ddi = ddi

    def mail(self):
        message = """From: CallBack <test@ohaiworld.com>
To: {0}
Subject: {6} Call Back - Ticket {4}
DDI: {1}
Name: {2}
Phone Number: {3}
Ticket: https://rackspacecloud.zendesk.com/tickets/{4}

Call Details:
{5}
        """.format(self.recipient,
                   self.ddi,
                   self.name,
                   self.phone,
                   self.ticket,
                   self.details,
                   self.platform
                   )
        print message
        return message

    def run(self):
        message = """From: CallBack <postmaster@cb.ohaiworld.com>
To: {0}
Subject: {7}: {6} Call Back - Ticket {4}

DDI: {1}
Name: {2}
Phone Number: {3}
Ticket: https://rackspacecloud.zendesk.com/tickets/{4}

Call Details:
{5}
        """.format(self.recipient,
                   self.ddi,
                   self.name,
                   self.phone,
                   self.ticket,
                   self.details,
                   self.platform,
                   self.status
                   )
        try:
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail('test@domain.com', self.recipient, message)
            return message
        except SMTPException,e:
            print e
            return "Error: Unable to send email"
