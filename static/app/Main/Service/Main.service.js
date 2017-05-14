angular.module('Main').factory('requestService', function ($http, $httpParamSerializerJQLike, SERVICE_URL) {
    return {
        serviceManager: function (type, url, inputs) {
            if (!angular.isUndefined(arguments[3])) {
                $http.defaults.headers.common.Authorization = arguments[3];
            }
            if (type === "post") {
                return $http.post(SERVICE_URL + url, $httpParamSerializerJQLike(inputs), {
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Accept": "application/json"
                    }
                });
          
            } else if (type === "postJson") {
                return $http.post(SERVICE_URL + url, inputs, {
                    headers: {
                        "Content-Type": "application/json;",
                        "Accept": "application/json"
                    }
                });
            } else if (type === "get") {
                return $http.get(SERVICE_URL + url);
            }
        }
    };
});
