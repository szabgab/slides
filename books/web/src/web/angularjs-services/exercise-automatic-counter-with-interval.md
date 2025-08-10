# Exercise: Automatic Counter with $interval

* $interval
* setInterval

Implement an automatic counter using the [$interval](https://docs.angularjs.org/api/ng/service/$interval) service

The $interval service of Angular will run its callback every N miliseconds so
we don't have to re-schedule it every time, on the other hand we will have to
call the `cancel` method to stop it when the user clicks on the `stop`
button.

