angular.module('threeurmind', ['ngRoute', 'ui.router', 'Form']).config(function ($routeProvider, $stateProvider, $locationProvider, $qProvider) {
	$qProvider.errorOnUnhandledRejections(false);
	$locationProvider.html5Mode(false);
	$locationProvider.hashPrefix('!');
    $routeProvider.when('/', {
        templateUrl: "static/app/Form/View/upload.tpl.html",
        controller: 'formCtrl'
    }).when('/material', {
        templateUrl: "static/app/Form/View/material.tpl.html",
        controller: 'materialCtrl'
    }).when('/company', {
        templateUrl: "static/app/Form/View/company.tpl.html",
        controller: 'companyCtrl'
    }).when('/thanks', {
        templateUrl: "static/app/Form/View/thanks.tpl.html",
        controller: 'formCtrl'
    });
    $stateProvider.state('material', {
        url: '/material',
        templateUrl: 'static/app/Form/View/material.tpl.html',
        controller: 'materialCtrl',
        cache: false
    }).state('company', {
        url: '/company',
        templateUrl: 'static/app/Form/View/company.tpl.html',
        controller: 'companyCtrl',
        cache: false
    }).state('upload', {
        url: '/upload',
        templateUrl: 'static/app/Form/View/upload.tpl.html',
        controller: 'formCtrl',
        cache: false
    }).state('thanks', {
        url: '/thanks',
        templateUrl: 'static/app/Form/View/thanks.tpl.html',
        controller: 'formCtrl',
        cache: false
    });
}).constant('SERVICE_URL', 'http://localhost:7000')
