angular.module("Products", []).config(["$httpProvider", function($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = "csrftoken";
	$httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
}]);
require("./products-controller");