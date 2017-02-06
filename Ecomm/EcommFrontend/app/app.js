//http://gregblogs.com/how-the-do-i-build-a-django-django-rest-framework-angular-1-1-x-and-webpack-project
/* Libs */
require("angular/angular");
require("angular-route/angular-route");
require("angular-resource/angular-resource");
require("angular-cookies/angular-cookies");
/* Globals */
_ = require("lodash");  
_urlPrefixes = {  
  API:"api/",
  TEMPLATES:"static/app/"
};
/* Components */
require("./components/products/products");
require("./components/authentication/authentication");

/* App Dependencies */
angular.module("myApp", [
  "Products",
  "Authentication",
  "ngResource",
  "ngRoute",
  'ngCookies'
]);

/* Config Vars */
var routesConfig = require("./routes");
// @TODO in Step 13.

/* App Config */
angular.module("myApp").config(routesConfig); 