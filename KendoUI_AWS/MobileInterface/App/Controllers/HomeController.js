app.controller('HomeController', ['$scope', 'User',
    function ($scope, User) {

        var user = new User();

        user.get().then(function (response) {
            console.error('Success');
        }, function (response) {
            console.error('Error');
        });


    }
]);