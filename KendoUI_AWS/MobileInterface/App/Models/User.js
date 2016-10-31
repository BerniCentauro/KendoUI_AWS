app.factory('User', ['DataModel', 'Config',
    function (DataModel, Config) {

        // Constructor
        function User(data) {
            if (data) {
                this.setData(data);
            }
        };

        // Methods
        User.prototype = new DataModel(Config.ApiHost + '/api/user');

        return User;
    }
]);