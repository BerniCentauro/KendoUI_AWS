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
                        if(response.status == 200) {
                            var data = {
                                items: response.data.FincaFilial.Items,
                                total: response.data.FincaFilial.Count
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
        // Scope
        // ---------------------------

        $scope.finca = new Finca();
        $scope.source = new kendo.data.DataSource(sourceOptions);

        // ---------------------------
        // Functions
        // ---------------------------

        $scope.init = function () {

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