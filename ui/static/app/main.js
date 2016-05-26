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
	$scope.results = "";

	$scope.SendWords = function(){
		console.log($scope.words)
		var words = "{\"input\": "+$scope.words+"}"
		$http.post('http://52.221.229.121/hadoop/input/',words).success(function(data){
        	
        });
	}

	$scope.ShowResults = function(){
		console.log("show");
		$http.get('http://52.221.229.121/hadoop/input/').success(function(data){
        	$scope.results = data
        });
	}
});

})();