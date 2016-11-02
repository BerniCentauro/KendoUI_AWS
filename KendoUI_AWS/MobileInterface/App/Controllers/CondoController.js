app.controller('CondoController', ['$scope', 'Condo',
    function ($scope, Condo) {

        //variables

        var sourceOptions = {
            transport: {
                read: function (options) {
                    $scope.condo.get().then(function (response) {
                        //success
                        if (response.status === 200) {
                            var data;

                            if (response.data.Count > 0) {
                                data = {
                                    items: response.data.Items,
                                    total: response.data.Count
                                }
                            } else {
                                data = {
                                    items: [],
                                    total: 0
                                }
                            }

                            options.success(data);
                        }
                    }, function (response) {
                        // TODO: Handler error
                    });
                }
            },
            schema: {
                data: 'items',
                total: 'total'
            }
        };

        //------------------------
        //functions
        //------------------------

        $scope.init = function () {
            $scope.condo = new Condo();
            $scope.source = new kendo.data.DataSource(sourceOptions);
        }

        $scope.add = function () {

            $scope.condo.save().then(function (response) {
                console.info('Success');
            }, function (response) {
                console.error('Error');
            });

        }

        $scope.edit = function () {

        }

        $scope.delete = function () {

        }

    }
]);