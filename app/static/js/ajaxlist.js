function CallbacksViewModel() {
    var self = this;
    self.callbacksURI = window.location.origin+'/api/v1.0/callbacks';
    self.username = "thecallbacks";
    self.password = "ag5346hs3gf142g32h4h4";
    self.callbacks = ko.observableArray();
    self.ajax = function(uri, method, data) {
        var request = {
            url: uri,
            type: method,
            contentType: "application/json",
            accepts: "application/json",
            cache: false,
            dataType: 'json',
            data: JSON.stringify(data),
            beforeSend: function (xhr) {
                xhr.setRequestHeader("Authorization",
                    "Basic " + btoa(self.username + ":" + self.password));
            },
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

    self.callbacksLengthURI = window.location.origin+'/api/v1.0/length';
    self.cb = 0;
    function resetList() {
        self.cb = 0;
    }
    function ajaxCall() {
        self.ajax(self.callbacksLengthURI, 'GET').done(function(data) {
            if (data.callbacks > self.cb + 1) {
                self.ajax(self.callbacksURI, 'GET').done(function(data) {
                    $('.tablesorter').trigger("update");
                    $('.cb-row').remove();
                    for (var i = 0; i < data.callbacks.length; i++) {
                        if (data.callbacks[i].platform.toLowerCase() == "linux") {
                            platform_fa = "fa fa-linux";
                        } else {
                            platform_fa = "fa fa-windows";
                        }
                        var updated_moment = moment(data.callbacks[i]["details"][data.callbacks[i]["details"].length - 1].updated).fromNow();
                        var created_moment = moment(data.callbacks[i].created).fromNow();
                        if ((updated_moment.regexIndexOf(/([1-9][0-9]|[6-9])/, 0) > -1
                            || updated_moment.indexOf('day') > -1)
                            && !(updated_moment.indexOf('minutes') > -1)) {
                            var label = "cb-row danger";
                        } else if ((updated_moment.regexIndexOf(/([1-5])/, 0) > -1)
                                   && !(updated_moment.indexOf('minutes')))  {
                            var label = "cb-row warning";
                        } else { 
                            var label = "cb-row success";
                        }
                        self.callbacks.push({
                            label: ko.observable(label),
                            platform: ko.observable(data.callbacks[i].platform),
                            platform_fa: ko.observable(platform_fa),
                            uri: ko.observable('/callbacks/'+data.callbacks[i].id),
                            ticket_url: ko.observable('http://some.url/tickets/'+data.callbacks[i].ticket),
                            ddi_url: ko.observable('http://some.url/account/'+data.callbacks[i].ddi),
                            status: ko.observable(data.callbacks[i]["details"][data.callbacks[i]["details"].length - 1].status),
                            ddi: ko.observable(data.callbacks[i].ddi),
                            ticket: ko.observable(data.callbacks[i].ticket),
                            name: ko.observable(data.callbacks[i].name),
                            phone: ko.observable(data.callbacks[i].phone),
                            created: ko.observable(created_moment),
                            updated: ko.observable(updated_moment),
                        });
                        self.cb = i;
                    }
                });
            }
        });
    }
    var timer=setInterval(ajaxCall, 5000);
    var timer=setInterval(resetList, 57000);
}
//$().ready(function() {
    ko.applyBindings(new CallbacksViewModel());
//});
