# No graph error


Look into `/var/log/jenkins/jenkins.log`

found error about:

```
WARNING: Error while serving http://jenkins.szabgab.com:8080/job/demo-flask-project/test/trend
...
Caused by: java.awt.AWTError: Assistive Technology not found: org.GNOME.Accessibility.AtkWrapper


Could not initialize class org.jfree.chart.JFreeChart
...
Caused by: java.lang.NoClassDefFoundError: Could not initialize class org.jfree.chart.JFreeChart
```

[Solution](https://askubuntu.com/questions/695560/assistive-technology-not-found-error-while-building-aprof-plot)

```
sudo vim /etc/java-8-openjdk/accessibility.properties
```

Comment out the following line:

```
#assistive_technologies=org.GNOME.Accessibility.AtkWrapper
```

```
vim /etc/init.d/jenkins
add `-Djava.awt.headless=true` to the line
```

```
$SU -l $JENKINS_USER --shell=/bin/bash -c "$DAEMON $DAEMON_ARGS -- $JAVA $JAVA_ARGS -Djava.awt.headless=true -jar $JENKINS_WAR $JENKINS_ARGS" || return 2
```

```
systemctl daemon-reload
service jenkins restart
```



