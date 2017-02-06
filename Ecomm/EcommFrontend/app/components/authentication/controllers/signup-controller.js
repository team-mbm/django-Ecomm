function SignupController($http, $cookies, $location, AuthService){
    var vm = this;
    vm.signup = function (){
        AuthService.signup(vm.email,vm.username, vm.password, vm.confirm_password, vm.address);
    }; 
    activate();
    function activate() {
      // If the user is authenticated, they should not be here.
      if (AuthService.isAuthenticated()) {
        $location.url("/");
      }
    }
}
angular.module("Authentication")
    .controller("SignupController",[
        "$http",
        "$cookies",
        "$location",
        "AuthService",
        SignupController
    ]);