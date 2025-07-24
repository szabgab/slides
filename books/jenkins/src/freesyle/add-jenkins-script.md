# Add Jenkins script


In the project directory create the `run_jenkins.sh` file  with the following content:

```
#!/bin/bash

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

Make it executable by running:

```
chmod +x run_jenkins.sh
```

Commit it to the git repository and push it out.

Then click on "Build Now" on the Jenkins UI.

It should build successfully now.


