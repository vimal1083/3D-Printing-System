angular.module('Form').controller('materialCtrl', ['$scope','FormService', '$state', function($scope, formService, $state) {
	$scope.materials = [];
	function getMaterials() {
		formService.loadingDisplay();
		formService.getAvailableMaterials().then(function (materials){
			formService.loadingNone();
			$scope.materials = materials.data;
			
		},function (error){
			formService.loadingNone();
			
		});
	}
	getMaterials();
	$scope.selectMaterial = function (material) {
		formService.material = material;
		$state.go('company');
	};
}]);
