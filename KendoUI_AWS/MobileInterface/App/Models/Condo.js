app.factory('Condo', ['DataModel', 'Config',
    function (DataModel, Config) {
        // Constructor
        function Condo(data) {
            if (data) {
                this.setData(data);
            }
        };

        // Methods
        Condo.prototype = new DataModel(Config.ApiHost + '/api/condo');

        return Condo;
    }
]);