angular.module('Form').controller('companyCtrl', ['$scope','FormService', '$state', function($scope, formService, $state) {
	$scope.materials = [];
	function getCompanies() {
		formService.loadingDisplay();
		requestData = {
			'material_id': formService.material.id,
			'stl_uuid': formService.uuid
		}
		formService.getCompanies().then(function (companies){
			formService.loadingNone();
			$scope.companies = companies;
		},function (error){
			formService.loadingNone();
			
		});
	}
	getCompanies();
	$scope.finalSubmit = function (company) {
		var orderData = {"stl_uuid":formService.uuid, "material_id":formService.material.id, "company_id": company.id};
		formService.loadingDisplay();
		formService.createOrder(orderData).then(function (){
			formService.uuid = '';
			formService.material = {};
			formService.loadingNone();
			$state.go('thanks');
		},function (error){
			formService.loadingNone();
			$state.go('thanks');
		});
	};
}]);
