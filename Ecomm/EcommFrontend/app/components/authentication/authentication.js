angular.module("Authentication", []).config(["$httpProvider", function($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = "csrftoken";
	$httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
}]);
require("./controllers/signup-controller");
require("./controllers/login-controller");
require("./services/auth-service");
require("./controllers/logout-controller");