# Minimal Travis-CI exit 1 failure

In the previous example our script was a simple echo that was successful. Now let's see what would happen if the script exited with an exit code different
from 0. For this we replace our script with a simple `exit `. After this triggers the build you'll probably get an e-mail reporting that the build
failed. You can also look at the UI in Travis-CI to see the failure.


{% embed include file="src/examples/minimal-exit-1/.travis.yml" %}


