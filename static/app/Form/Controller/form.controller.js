angular.module('Form').controller('formCtrl', ['$scope','FormService', '$state', function($scope, formService, $state) {
	$scope.uploadFile = function(files) {
		allowedExtensions = new Array('stl');
		ext = files[0].name.split('.').pop();
		if(allowedExtensions.indexOf(ext) >= 0) {
			formService.loadingDisplay();
			var formData = new FormData();
			formData.append("file", files[0]);
			formService.uploadDesign(formData).then(function (uuid){
				formService.loadingNone();
				formService.uuid = uuid;
				$state.go('material');
			},function (error){
				formService.loadingNone();
				
				$state.go('material');
			});
		}
		else {
			alert('Invalid Image')
		}
	};
}]);
