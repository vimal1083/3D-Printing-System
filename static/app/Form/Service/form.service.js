angular.module('Form').factory('FormService', function(requestService) {
    this.uuid = '';
    this.material = {};
    return {
        uploadDesign: function(imageData) {
            return requestService.serviceManager('post', '/api/upload-stl/', imageData);
        },
	getAvailableMaterials: function() {
            return requestService.serviceManager('get', '/api/available-materials/', {});
	},
	getCompanies: function(selectedData) {
            return requestService.serviceManager('postJson', '/api/available-companies/', selectedData);
	},
	createOrder: function(orderData) {
            return requestService.serviceManager('postJson', '/api/create-order/', orderData);
	},
		loadingDisplay: function () {
			document.querySelector('div.loading').style.display = 'block';
		},
		loadingNone: function () {
			document.querySelector('div.loading').style.display = 'none';
		},
        uuid :this.uuid,
        material :this.material
    };
});
