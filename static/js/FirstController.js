angular.module('myApp').controller('FirstController',['$scope','$http',function($scope,$http) {
var url="http://127.0.0.1:8000/post/";
   $http.get(url).success( function(response) {
                           $scope.students = response;
                        });
 
}]);
