function CallbackDetailsViewModel() {
    var self = this;
    self.callbackDetailsURI = window.location.origin+'/api'+window.location.pathname;
    self.callbackLengthURI = window.location.origin+'/api'+window.location.pathname;
    self.cb = 0;
    
//self.username = "thecallbacks";
//self.password = "ag5346hs3gf142g32h4h4";
    self.callback = ko.observableArray();
    self.filters = []; //[{"name":"details", "op":"any", "val":{"name":"status", "op":"like","val":"%pending"}}];
    self.ajax = function(uri, method, data) {
        var request = {
            url: uri,
            type: method,
            contentType: "application/json",
            accepts: "application/json",
            cache: false,
            dataType: 'json',
            data: {"q": JSON.stringify({"filters":self.filters})},
            //beforeSend: function (xhr) {
            //    xhr.setRequestHeader("Authorization",
            //        "Basic " + btoa(self.username + ":" + self.password));
            //},
            success: function(text) {
                $('#connection-danger').hide();
                $('#connection-lost').text("");
            },
            error: function(jqXHR) {
                $('#connection-danger').show();
                $('#connection-lost').text("Connection with the API has been lost.");
                console.log("ajax error " + jqXHR.status)
            }
        };
        return $.ajax(request);
    }

    self.markPlatform = function(platform) {
        if (platform.toLowerCase() == "linux") {
            platform.done(True);
        } else {
            platform.done(False);
        }
    }

    String.prototype.regexIndexOf = function ( pattern, startIndex ) {
        startIndex = startIndex || 0;
        var searchResult = this.substr( startIndex).search(pattern);
        return ( -1 === searchResult ) ? -1 : searchResult + startIndex;
    }

    function resetList() {
        self.cb = 0;
    }
    $('#new_post').hide();
    var posts = self.cb;
    function ajaxCall() {
        self.ajax(self.callbackLengthURI, 'GET').done(function(data) {
            if (data.details.length > self.cb) {
                if (self.cb > posts) {
                    posts++;
                    $('#new_post').show();
                    $('#new').html(posts+" changes");
                }
                self.ajax(self.callbackDetailsURI, 'GET').done(function(data) {
                    $('.tablesorter').trigger("update");
                    $('.msg').remove();
                    for (var i = 0; i < data.details.length; i++) {
                        var last_updated = moment(data.details[i].details[data.details[i].details.length - 1].updated).format('MMMM Do YYYY, h:mm:ss a');
                        var updated = moment(data.details[i].updated).format('MMMM Do YYYY, h:mm:ss a');
                        var created_moment = moment(data.details[i].created).fromNow();

                        if (data.platform.toLowerCase() == "linux") {
                            platform_fa = "fa fa-linux";
                        } else {
                            platform_fa = "fa fa-windows";
                        }

                        if (i == (data.details.length - 1)) {
                            var le = "last";
                        } else {
                            var le = "";
                        }

                        self.callback.push({
                            msg_id: ko.observable(le),
                            platform: ko.observable(data.platform),
                            platform_fa: ko.observable(platform_fa),
                            uri: ko.observable('/callbacks/'+data.id),
                            ticket_url: ko.observable(
                                'http://some.url/tickets/'+data.ticket),
                            ddi_url: ko.observable(
                                'http://some.url/account/'+data.ddi),
                            status: ko.observable(
                                data.details[i]["details"][data.details[i]["details"].length - 1].status),
                            ddi: ko.observable(data.ddi),
                            ticket: ko.observable(data.ticket),
                            message_title: ko.observable("Message Details - "+data.details[i].status+" at "+updated),
                            private_title: ko.observable("Private Note - "+data.details[i].status+" at "+updated),
                            message: ko.observable(data.details[i].details),
                            private: ko.observable(data.details[i].private),
                            name: ko.observable(data.name),
                            phone: ko.observable(data.phone),
                            created: ko.observable(created_moment),
                            updated: ko.observable(updated),
                        });
                    }
                    self.cb = data.details.length;
                    var last_entry = jQuery('#last_entry');
                    var last = jQuery('#last');
                    last_entry.html(last.children().clone());
                });
            }
        });
    }
    var timer=setInterval(ajaxCall, 5000);
    var timer=setInterval(resetList, 57000);
}
//$().ready(function() {
    ko.applyBindings(new CallbackDetailsViewModel());
//});
