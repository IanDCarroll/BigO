# BigO
This is a repository exploring some basics of Big O Notiation.

###What is Big O Notation?
"Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. It is a member of a family of notations invented by Paul Bachmann, Edmund Landau, and others, collectively called Bachmann–Landau notation or asymptotic notation." -Wikipedia

that just sounds like a whole bunch of academic words! How are you supposed to figure anthing out from all that, let alone apply it?!

###Here's a simpler (If possibly wrong) definition:
Big O Notation is used to classify and evaluate a function's performance with increasingly large data sets. It helps to answer the question "But what if we pass it a billion values?" "What if 100 million users hit the login page?" "How well does this stand up to DDOS attacks?" and so on.

To be sure, there are many more tools for evaluating and optimizing an app for speed and scale. Big O is not enough in and of itself to do this for you. But it is something to consider if you want to make things go fast. You definitely want to apply this to a performance bottleneck.

###And what does the O even stand for? Why the flibbit is it Big?!
The O stands for the "Order of the function". Confused? You bet! "Order" has nothing to do with how the function is organized. Nor does it care in what sequence things are done. Instead, it's "Order" as in "Order of Infinity", or "Order of Magnitude". It basically means how the function performs as the values it has to chug through approaches infinity.

It is big because it always assumes the worst case scenario, the "Biggest" problem possible for the code to search through. Big O doesn't care about a search algorythm that just happens to find what it's looking for in the first value it evaluates. It assumes the algorythm will operate like you do when you can't find your car keys. They'll turn up only after you've searched everywhere up to the box of ice cream sandwiches you stashed in the back of your freezer.

###Ok, cool, so what are the basic types of Big O seen in code?
These have meaning if you are a math-ite, but even without that, it's not hard to get a good picture of them. This is not a complete list, these are just some common types.

__O(1)__ = Constant at scale. No matter how many values you plug into this, it always performs the same. The bottleneck to an algorythm like this will instead be how the language is executed, the hardware, or (most likely) another function you wrote that this one needs.

__O(N)__ = Linear slow-down to scale. For every value you add to input, it takes aritmatically that much longer to output.

__O(N^2)__ = Double linear slow-down to scale. For every value you add to input, it takes that times 2 to output.

__O(2^N)__ = Exponential slow-down to scale. For every value you add input, the function takes that number times itself to output. If you run one of these you'll notice it grind to a halt after a certain point. It really just can't be used at scale.

__O(logN)__ = Initially slow, but it evens out at scale. A function like this takes its slowness upfront and then approaches a set limit as time goes on. A binary search is a good example of this.

__O(Nlog(N))__ = slower than linear, but not as slow as exponential. This will have performance problems at large scales. In the smaller scale it appears to behave very similarly to linear, but Big O is about answering how things will perform as the scale apporaches infinity. Python's sort() function is of this kind.

###Confused still? Did I miss something? Am I just plain wrong?
Then I'm probably not explaining this right. <a href="https://github.com/IanDCarroll/BigO/issues/new">Raise an issue.</a> :smile: 
