(function(){

var app = angular.module('app.main', [
	'ui.router',
	'restangular',
	'ui.bootstrap'
]);

app.config(function(RestangularProvider){
	RestangularProvider.setBaseUrl('/api');
});
app.run(function($rootScope){
	$rootScope.app_base = '/';
});

app.config(function($stateProvider, $urlRouterProvider) {
	$urlRouterProvider.otherwise('/');
	$stateProvider
		.state('root', {
			url: '/',
			templateUrl: 'templates/root.html',
			controller: 'MainAuthController'
		});
});

app.controller('MainAuthController', function($rootScope, Restangular, $state, $scope, $http){
	$scope.words = "";
	$scope.results = "Try search something first!";
	$scope.isSearching = false;
	$scope.button = "Search";
	$scope.SendWords = function(){
		$scope.isSearching = true;
		$scope.button = "Loading";
		$scope.results = "Waiting for results";
		console.log($scope.words);
		var words = "{\"input\": \""+$scope.words+"\"}";
		$http.post('http://52.221.229.121/hadoop/input/',words).success(function(data){
						$scope.results = data+"";
						console.log("Data : "+data);
						$scope.isSearching = false;
						$scope.button = "Search";
        });
	};

});

})();
