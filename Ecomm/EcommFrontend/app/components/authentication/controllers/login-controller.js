function LoginController($location, $scope, AuthService){
    var vm = this;
    activate();
    function activate(){
        console.log("calling activate");
      // If the user is authenticated, they should not be here.
      if (AuthService.isAuthenticated()){
          console.log("inside activate");
        window.location("/");
      }
    }
   vm.login =  function login(){
      AuthService.login(vm.email, vm.password);
    };
}
angular.module("Authentication")
    .controller("LoginController",[
        "$location",
        "$scope",
        "AuthService",
        LoginController
    ]);