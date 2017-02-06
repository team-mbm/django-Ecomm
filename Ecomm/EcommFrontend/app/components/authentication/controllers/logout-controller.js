function LogoutController($location, $scope, AuthService){
    var vm = this;
    activate();
    function activate(){
        console.log("calling activate");
      // If the user is authenticated, they should not be here.
      if (AuthService.isAuthenticated()){
        $location.url('/404');
      }
    }
}
angular.module("Authentication")
    .controller("LogoutController",[
        "$location",
        "$scope",
        "AuthService",
        LogoutController
    ]);