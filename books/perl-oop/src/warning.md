# A warning

One of the problems I see when teaching new things to programmers is that they (we) get a bit too enthusiastic and they will start to use the new knowledge everywhere.

I am sure you remember when you first learned regular expressions and then you wanted to use it everywhere, including parsing of HTML.

So I'd like to tell you up-front that OOP is not the solution to every problem.

We saw this very clearly when in the mid '90s with the introduction of Java people started to use OOP and specifically inheritance everywhere.

The well known example, though it is entirely possible I made that up, was the representations of household items: cats and dogs.
As both cats and dogs are mammals it sounded like a good idea to create a class called "Mammal" and to make the class "Cat" and the class "Dog" both inherit from that class.
After all there are a lot of common features between cats and dogs.
So instead of implementing almost everything twice we can implement them in the "Mammal" class and then make the specializations in the "Cat" and "Dog" classes.

This was fine. However, the need arose to also represent other things around the house: chairs and tables.

At that point some overly enthusiastic person noticed that all 4 types: chairs, tables, cats, and dogs have legs. So they created a class call "LeggedThings" and made
all 4 classes inherit from that.

In the name of code-reuse and DRY they created a totally unmaintainable mess.

Of course one does not need OOP to create an unmaintainable mess, but OOP is also just a tool. One needs to weight various possible solutions and makes sure nothing is overused.



