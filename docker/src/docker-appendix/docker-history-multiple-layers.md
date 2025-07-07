# Docker history - multiple layers

If you run the same command on the mydocker image we have just created you can see that it has 2 more layers.
Each **RUN** command created a layer.

Layers are created separately so having multiple layers makes our development process faster.
However having many layers is not recommended so once in a while we usually merge the RUN instructions together
and rebuild the image to have less layers. We'll talk about this later.


```
docker history mydocker
```

{% embed include file="src/examples/dock/history_mydocker.out" %}


