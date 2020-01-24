# PhoneGap
{id: phonegap}

## PhoneGap
{id: phonegap-intro}

* Open Source
* [download](http://phonegap.com/)
* [register](https://build.phonegap.com/apps) and use online (Adobe or Github user)



## Install PhoneGap
{id: install-phonegap}

For Android:


* [Java SE JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
* [Android SDK](http://developer.android.com/sdk/index.html)
* [PhoneGap](http://phonegap.com/)

For Apple:

* ...

And some more set-up work...


## PhoneGap Build
{id: phonegap-build}

[register](https://build.phonegap.com/apps) and use online (Adobe or Github user)


## Sign up for Android
{id: android}

* [publish](https://play.google.com/apps/publish/) ($25, 2 days)
* [publish](https://support.google.com/googleplay/android-developer/answer/113468?hl=en&amp;ref_topic=2365624)


## Android Signed
{id: android-signed}

Generating the keys:

```
$ keytool -genkey -v -keystore ~/.keystore -alias alias_name
   -keyalg RSA -keysize 2048 -validity 10000

Enter keystore password: some_global_secret_that_will_be_shared_with_phonegap
Re-enter new password:
What is your first and last name?
  [Unknown]:  Foo Bar
What is the name of your organizational unit?
  [Unknown]: me
What is the name of your organization?
  [Unknown]:
What is the name of your City or Locality?
  [Unknown]:
What is the name of your State or Province?
  [Unknown]:
What is the two-letter country code for this unit?
  [Unknown]:
Is CN=Foo Bar, OU=me, O=Unknown, L=Unknown, ST=Unknown, C=Unknown correct?
  [no]:  y

Generating 2,048 bit RSA key pair and self-signed certificate (SHA256withRSA)
    with a validity of 10,000 days
	for: CN=Gabor Szabo, OU=me, O=Unknown, L=Unknown, ST=Unknown, C=Unknown
Enter key password for alias_name
	(RETURN if same as keystore password):
    (a secondary password of the specic key, also shared with PhoneGap)
New certificate (self-signed):
```


```
-keystore path/to.keystore  (defaults to ~/.keystore)
-alias  (8 significant characers?)
```

`keytool -v -list -keystore ~/.keystore` can list the existing keys and their aliases in verbose mode.

You will need to provide the alias, and the two passwords to the PhoneGap build system.


## Apple
{id: apple}

* [Sign up](https://developer.apple.com/)
* Then sign up to the "iOS Developer Program" for $99/year at [ios](https://developer.apple.com/programs/ios/)
* They promise to process your request in 2 workdays.
* Then follow this [guide](https://build.phonegap.com/docs/ios-builds)
* Need the uuid of the device. Use the application called 'udid sender' to fetch it.



## Process
{id: process-and-exercise}

* Create a directory for yor project and put a www/ subdirectory in it
* In the www/ subdirectory create a file called index.html, use external javascript and CSS.
* Create a Git repository, and push it to Github
* Add a www/config.xml and push that to Github as well
* Use Build PhoneGap to generate the application
* Download the APK file for Android, connect your mobile device to the computer, copy the APK file and from the device click on it to install it.



## Git and Github
{id: git}

* $ git init
* $ git add .
* $ git ci -m'initial version'
* Github


## Config
{id: phonegap-config}
![](examples/phonegap/config.xml)

* id            set something for yourself
* versionCode   start from 1
* version       start from 0.0.1
* name
* description
* author
* phonegap-version   The Phonegap Build will tell you when to change this.
* permissions   See the comment and the docs
* [confg-xml](https://build.phonegap.com/docs/config-xml)


## Exercise: PhoneGap Build
{id: phonegap-exercise}


Follow the "Process" in the earlier slide: creat a simple web application, eg. an input box, and a button,
and when the button is clicked, show the content of the input box elsewhere on the page. Then push it out to github.




Sign up to PhoneGap and set this project as an open source project and build it.




Try to install it on your mobile device.



Then update your application and install it again.






