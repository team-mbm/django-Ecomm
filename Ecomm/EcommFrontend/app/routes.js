function routesConfig($routeProvider) {  
  $routeProvider
    .when("/", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/products/products.html",
      label: "Products"
    })
    .otherwise({
      templateUrl: _urlPrefixes.TEMPLATES + "404.html"
    });
}

routesConfig.$inject = ["$routeProvider"];

module.exports = routesConfig; 