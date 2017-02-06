function ProductsController($scope, $http){
  $scope.products = [];
  $http({
  method: "GET",
  url: "./api/product/?format=json"
}).then(function successCallback(response) {
  console.log(response);
    $scope.products = response.data;
  }, function errorCallback(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
    $scope.products = response;
  });
  console.log($scope.products);
}
angular.module("Products")
	.controller("ProductsController",[
    "$scope",
    "$http",
    ProductsController
]);