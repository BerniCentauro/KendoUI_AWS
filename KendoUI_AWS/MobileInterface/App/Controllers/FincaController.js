app.controller('FincaController', ['$scope', 'Finca',
    function ($scope, Finca) {

        // ---------------------------
        // Variables
        // ---------------------------

        var sourceOptions = {
            transport: {
                read: function (options) {
                    $scope.finca.get().then(function (response) {
                        // Success
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

        // ---------------------------
        // Functions
        // ---------------------------

        $scope.init = function () {
            $scope.finca = new Finca();
            $scope.source = new kendo.data.DataSource(sourceOptions);
        }

        $scope.add = function () {
            $scope.finca.save().then(function (response) {
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