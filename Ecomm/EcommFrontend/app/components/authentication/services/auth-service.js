angular.module("Authentication")
    .factory("AuthService",AuthService);
AuthService.$inject = ['$cookies', '$http']; 
function AuthService($cookies, $http) {
    var AuthService = {
      getAuthenticatedAccount: getAuthenticatedAccount,
      isAuthenticated: isAuthenticated,
      login: login,
      logout: logout,
      signup: signup,
      setAuthenticatedAccount: setAuthenticatedAccount,
      unauthenticate: unauthenticate
    };

    return AuthService;

    function getAuthenticatedAccount() {
      if (!$cookies.authenticatedAccount) {
        return;
      }

      return JSON.parse($cookies.authenticatedAccount);
    };

    function isAuthenticated() {
      console.log("isAuthenticated");
      return !!$cookies.authenticatedAccount;
    };

    function login(email, password) {
      console.log("inside login");
      return $http.post("./auth/login/", {
        email: email, password: password
      }).then(loginSuccessFn, loginErrorFn);
      function loginSuccessFn(data, status, headers, config) {
        AuthService.setAuthenticatedAccount(data.data);

        window.location = '/';
      };

      function loginErrorFn(data, status, headers, config) {
        console.error('login err fn');
        console.log(data,status,headers);
      };
    };
    function logout() {
      console.log("logout in AuthService");
      return $http.post('./auth/logout/')
        .then(logoutSuccessFn, logoutErrorFn);

      function logoutSuccessFn(data, status, headers, config) {
        AuthService.unauthenticate();

        window.location = '/';
      };

      function logoutErrorFn(data, status, headers, config) {
        console.error('logout Epic failure!');
      };
    };

    function signup(email, username, password, confirm_password, address) {
      return $http.post('./api/customer/', {
        username: username,
        password: password,
        confirm_password:confirm_password,
        email: email,
        address:address
      }).then(registerSuccessFn, registerErrorFn);

      
      function registerSuccessFn(data, status, headers, config) {
        console.log("registersuccess fn");
        console.log(data,status,headers);
        AuthService.login(email, password);
      };

      function registerErrorFn(data, status, headers, config) {
        console.error('Error');
        console.log(data,status,headers);
      };
    };
    function setAuthenticatedAccount(account) {
      $cookies.authenticatedAccount = JSON.stringify(account);
    };

    function unauthenticate() {
      delete $cookies.authenticatedAccount;
    };
}