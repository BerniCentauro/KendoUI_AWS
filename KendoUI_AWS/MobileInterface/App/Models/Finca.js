app.factory('Finca', ['DataModel', 'Config',
    function (DataModel, Config) {

        // Constructor
        function Finca(data) {
            if (data) {
                this.setData(data);
            }
        };

        // Methods
        Finca.prototype = new DataModel(Config.ApiHost + '/api/fincafilial');

        return Finca;
    }
]);