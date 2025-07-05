# Integrate pylint reporting


* Install the "Violations" plugin
* Add the Violations to the "Post-build Actions" of the project
* In the pylint line put: pylint.log
* In "Source Path Pattern" put **/
* **pip install pylint**
* **pylint --generate-rcfile > pylint.cfg**
* Update the run_jenkins file to run pylint


