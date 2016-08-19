angular.module('{{cookiecutter.project_slug}}', ['ngRoute', 'pascalprecht.translate'])
    .config(["$translateProvider", function ($translateProvider) {

        var appResource = resources['{{cookiecutter.project_slug}}'];
        $translateProvider
            .translations('en-us', appResource.us)
            .translations('zh-cn', appResource.cn)
            .translations('zh-tw', appResource.tw);
    }])
    .config(["$routeProvider", function ($routeProvider) {
        $routeProvider
            .when("/{{cookiecutter.project_slug}}/demo", {
                templateUrl: "/modules/{{cookiecutter.project_slug}}/app/demo/index.html",
                controller: 'DemoCtrl'
            })
    }])
    .version = '0.0.1';