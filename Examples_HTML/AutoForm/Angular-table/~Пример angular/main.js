var myApp = angular.module('myApp', []);

myApp.controller("AppCtrl", function($scope, $http) {
	$scope.mytab = 		
		[
			{"modelj": "Загрузка"}	
		];
	$http.get('http://localhost:4388/ham/odata/Mashina?$expand=postavshik,prodaga')
	
	.then(function(response) {
        console.log(response.data.value);
		$scope.mytab = response.data.value;
	});
});	
