app.factory('DataModel', ['$http',
    function ($http) {

        var url;

        // Constructor
        function DataModel(serviceUrl) {
            if (serviceUrl) {
                url = serviceUrl;
            }
        };

        // --------------------------------------
        // Public Methods
        // --------------------------------------

        DataModel.prototype = {
            setData: function (data) {
                angular.extend(this, data);
            },
            get: function (id) {
                var scope = this;
                if(id) {
                    return $http.get(url + '/' + id).success(function (response) {
                        if (response && response.Status == 0) {
                            angular.extend(scope, response.Data);
                        }
                    });
                } else {
                    return $http.get(url);
                }
            },
            delete: function () {
                return $http.delete(url + '/' + this.Id);
            },
            save: function () {
                if (this.Id) {
                    return $http.put(url + '/' + this.Id, this);
                } else {
                    return $http.post(url, this);
                }
            }
        };
        
        return DataModel;
    }
]);