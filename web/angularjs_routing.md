# AngularJS - Routing
{id: angularjs-routing}

## Routing
{id: routing}
{i: ngRoute}
{i: ui-router}

* "Pages" we saw earlier
* [ngRoute](https://docs.angularjs.org/api/ngRoute)
* [ui-router](https://github.com/angular-ui/ui-router)



## Simple routing
{id: routing-simple}
{i: ng-view}
{i: $route}
{i: $routeProvider}

* template - inline template
* templateUrl - URL of template file on server
* templateUrl - id of embedded template inside the Controller

![](examples/angular/simple_routing.html)
![](examples/angular/simple_routing.js)
![](examples/angular/second.html)



## Routing from code
{id: routing-from-code}
{i: $location}
![](examples/angular/routing_from_code.html)
![](examples/angular/routing_from_code.js)


## Two Angular controllers on the same page
{id: angular-two-conrollers}
![](examples/try/two.html)
![](examples/try/two.js)


## Two Angular Apps on the same page
{id: angular-two-apps-on-same-page}


<a href="http://stackoverflow.com/questions/18571301/angularjs-multiple-ng-app-within-a-page">Multiple apps</a>




## Routing with controller
{id: routing-with-controller}
![](examples/angular/routing_controller.html)
![](examples/angular/routing_controller.js)


## Routing with parameters
{id: routing-with-parameters}
![](examples/angular/routing_params.html)
![](examples/angular/routing_params.js)


## Exercise: Routing
{id: exercise-routing}

* Change the TODO application so you will have a main page listing all the items with links to /item/ID and those pages showing the details and have a link to /edit/ID that will allow the user to edit details about the item.






