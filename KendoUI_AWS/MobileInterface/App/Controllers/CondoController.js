app.controller('CondoController', ['$scope', 'Condo',
    function ($scope, Condo) {

        //variables

        var sourceOptions = {
            transport: {
                read: function (options) {
                    $scope.condo.get().then(function (response) {
                        //success
                        if (response.status == 200) {
                            var data = {
                                items: response.data.Condos.Items,
                                total: response.data.Condos.Count
                            }

                            options.success(data);
                        }
                    }, function (response) {

                    });
                }
            },
            schema: {
                data: 'items',
                total: 'total',
            }
        };

        //-----------------------
        //Scope
        //-----------------------
        $scope.condo = new Condo();
        $scope.source = new kendo.data.DataSource(sourceOptions);

        //------------------------
        //functions
        //------------------------
        $scope.init = function () {

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