# Chat server

{% embed include file="src/examples/net/chat.js" %}

This works, but when someone disconnects, the dead socket remains in the array and when we try to write to it it will blow up.


