(function (angular) {
    angular.module('{{cookiecutter.project_slug}}')
        .factory('ngDemo', ["$http", "$q", function (globalConfig, $http, $q) {
            var get = function () {
                var deferred = $q.defer();
                $http.get(globalConfig.get("node/status", {hideLoading: true})
                    .then(function successCallback(response) {
                        return deferred.resolve(response.data)
                    }, function errorCallback(response) {
                        return deferred.reject(false)
                    })
                return deferred.promise;
            }

            return {get: get}
        }]);

})(window.angular);
