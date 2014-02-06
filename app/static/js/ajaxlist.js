function CallbacksViewModel() {
    var self = this;
    self.callbacksURI = window.location.origin+'/api/callbacks';
//self.username = "thecallbacks";
//self.password = "ag5346hs3gf142g32h4h4";
    self.callbacks = ko.observableArray();
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

    self.callbacksLengthURI = window.location.origin+'/api/callbacks';
    self.cb = 0;
    function resetList() {
        self.cb = 0;
    }
    function ajaxCall() {
        self.ajax(self.callbacksLengthURI, 'GET').done(function(data) {
            if (data['num_results'] > self.cb) {
                self.ajax(self.callbacksURI, 'GET').done(function(data) {
                    $('.tablesorter').trigger("update");
                    $('.cb-row').remove();
                    for (var i = 0; i < data.objects.length; i++) {
                        if (data.objects[i].platform.toLowerCase() == "linux") {
                            platform_fa = "fa fa-linux";
                        } else {
                            platform_fa = "fa fa-windows";
                        }
                        var updated_moment = moment(data.objects[i]["details"][data.objects[i]["details"].length - 1].updated).fromNow();
                        var created_moment = moment(data.objects[i].created).fromNow();
                        if ((updated_moment.regexIndexOf(/([1-9][0-9]|[6-9])/, 0) > -1
                            || (updated_moment.indexOf('day') > -1
                                || updated_moment.indexOf('hour') > -1))
                            && !(updated_moment.indexOf('minutes') > -1)) {
                            var label = "cb-row danger";
                        } else if ((updated_moment.regexIndexOf(/([1-4][0-9])/, 0) > -1
                                   || updated_moment.indexOf('hours') > -1)) {
                            var label = "cb-row warning";
                        } else { 
                            var label = "cb-row success";
                        }
                        self.callbacks.push({
                            label: ko.observable(label),
                            platform: ko.observable(data.objects[i].platform),
                            platform_fa: ko.observable(platform_fa),
                            uri: ko.observable('/callbacks/'+data.objects[i].id),
                            ticket_url: ko.observable('http://some.url/tickets/'+data.objects[i].ticket),
                            ddi_url: ko.observable('http://some.url/account/'+data.objects[i].ddi),
                            status: ko.observable(data.objects[i]["details"][data.objects[i]["details"].length - 1].status),
                            ddi: ko.observable(data.objects[i].ddi),
                            ticket: ko.observable(data.objects[i].ticket),
                            name: ko.observable(data.objects[i].name),
                            phone: ko.observable(data.objects[i].phone),
                            created: ko.observable(created_moment),
                            updated: ko.observable(updated_moment),
                        });
                    }
                    self.cb = data['num_results'];
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
