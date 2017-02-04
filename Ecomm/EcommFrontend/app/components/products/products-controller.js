function ProductsController(){
  var that = this;
  that.foo = "products app";
  console.log(that);
}

angular.module("Products")
	.controller("ProductsController",[
  ProductsController
]);