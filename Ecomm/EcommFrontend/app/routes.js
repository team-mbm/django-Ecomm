function routesConfig($routeProvider) {  
  $routeProvider
    .when("/", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/products/products.html",
      label: "Products"
    })
    .when("/login",{
      templateUrl: _urlPrefixes.TEMPLATES + "components/authentication/views/login.html",
      label: "Login"
    })
    .when("/logout",{
      templateUrl: "",
      label: "Logout"
    })
    .when("/signup",{
      templateUrl: _urlPrefixes.TEMPLATES + "components/authentication/views/signup.html",
      label: "Signup"
    })
    .otherwise({
      templateUrl: _urlPrefixes.TEMPLATES + "404.html"
    });
}

routesConfig.$inject = ["$routeProvider"];

module.exports = routesConfig; 