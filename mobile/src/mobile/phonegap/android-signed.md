# Android Signed


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




