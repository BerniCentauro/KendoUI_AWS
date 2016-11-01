app.controller('UserController', ['$scope', 'User',
    function ($scope, User) {

        //Variables
        var sourceOptions = {
            transport: {
                read: function (options) {
                    $scope.user = new User();
                    $scope.user.get().then(function (response) {
                            //Success
                            if (response.status === 200) {
                                var data = {
                                    items: response.data.Users.Items,
                                    total: response.data.Users.Count
                                }

                                options.success(data);
                            }
                        },
                        function (response) {
                            //Error
                        });
                }
            },
            schema: {
                data: 'items',
                total: 'total'
            }
        };

        //Functions
        $scope.init = function () {
            $scope.user = new User();
            $scope.source = new kendo.data.DataSource(sourceOptions);
        }

        $scope.add = function() {

            $scope.user.save().then(function() {
                console.info('Success');
            }, function() {
                console.error('Error');
            });

        }

        $scope.edit = function() {
            
        }

        $scope.delete = function() {
            
        }
    }
]);