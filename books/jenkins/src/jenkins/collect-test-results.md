# Collect test results: xUnit integration

* Use pytest --junitxml=test-results/$BUILD_NUMBER.xml
* Configure / Post-build Actions / Publish JUnit test results report / Test report XMLs: `test-results/*.xml`



