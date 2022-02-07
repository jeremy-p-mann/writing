Tables to Probabilities
=======================

Slide 1
-------

Hello. In this lecture, I'd like to describe a construction that goes from
things that can be represented in physical memory to a single mathematical
abstraction. The video represents “things that can be represented in physical
memory” as tables while probability distributions are the “single mathematical
abstraction”.

Slide 2
-------

So I need to produce a probability distribution from the data of a table.

Probability distributions are precisely defined objects. To make my life easier,
I will begin by giving a precise definition of a table that's convenient 
for our discussion.

Next, I'll introduce a general probabilistic construction.

We will then accomplish our goal by applying this construction to tables and
then describe the output.

To keep this video brief, I won't give much motivation to this construction.
Suffice it to say that math gives us lots of tools to do things with 
probability distributions.

Slide 3
-------


To anchor our discussion, let's review a specific table, called FooBar.

This table is indexed by a set, let's call it I, with 4 elements, 0, 1, 2, 3.
There are two columns, 'foo' and 'bar'. In other words the set of columns, 
let's call it J, has two elements.

Note that each row of FooBar is an element of a two dimensional space,
R J, the set of J-tuples of real numbers. Furthermore we can think of as the 
set of maps from the set of columns, J to the real numbers. 

Slide 4
-------

So let's see if we can extract a precise definition from this perspective on
tables. For simplicity, we'll only consider every entry in our table is  float
float.

A table is the data of:

An set of indices, I which parametrizes the rows of the table.

An set of columns, J

Finally, we have the entries of the table, which we can think of as a map 
from I to the set of J-tuples of real numbers.

In other words an association of, for every index i, J-many real number x i j.

Note that this definition is a "row-centric" definition.

That's a bit abstract. Let's recover some more familiar perspectives on tables.

Slide 5
-------

Let's say that there are N rows, and the index is 0 to N-1
Further, let's assume there are m columns, let's call them 0 to m-1.

In this case, the table is the data of for each whole number between 0 and
N-1, a vector of dimension m. I.e. N m-component vectors.

Alternatively, we can see this data as an n by m matrix of real numbers.

Although I should warn you that, although this 

Finally, hopefully it's clear that this data is the same as N samples 
each of which has m features.

So yea, that's the first part: a precise definition of a table. 
And now for the probabilistic construction.

Slide 6
-------

This construction takes two pieces of input:

First A map, let's call it pi, between two sets: X_0 to X_1.

Second, a probability distribution on the source of pi, X_0, let's call it rho.

The output of this construction is a probability distribution on the 
target of pi, X_1, pi star rho. We call this distribution the pushforward of 
rho along pi.

Of course, I still have to define this distribution. Recall that if you 
know how to compute expectation values of real-valued function with respect 
to a distribution, you know the distribution.

In our case, the pushforward of rho along pi is characterized by the following.

Note that, given a real-valued function on X_1, O, which I'll call an observable,
note that we obtain an observable on X_0 by first applying pi and then 
applying O. This new function is often to referred to as the pullback of
rho along pi.

As rho is a distribution on X_0 and the pullback of O along pi is an observable
on X_0, it. 

Therefore, we can use this maneuvre to define the expectation value of
O with respect to the pushforward of rho along pi as the expectation of 
the pullback of O along pi with respect to rho.

pushingforward as the adjoint of pulling back, aka precomposition.

Slide 7
-------

So just to summarize, given a map of sets pi, we obtain a function
that sends a probability distribution, rho, on the souce of the map to 
probability distribution, pi star rho, on the target of the map.

So we're used to thinking of probability distributions as associating
numbers to events. Therefore, we should probably address the question, how
do we compute probabilities with respect to the pushforward of a distribution
in terms of the the map and the original distribution?

Slide 8
-------

So our definition of is in terms observables. Therefore, if we want to say 
something about events, aka measurable subsets of the event space, we should 
think of events as a real-valued functions.

This is straight forward. Given a subset A, the function takes an element x to 1
if x is in A, and 0 otherwise. We'll call this function chi sub A, the 
characteristic function of A.

If you think a bit, you'll realize that the probability of A is the expectation
value of chi sub A. 

By definition, this is computed as the expectation value of the precomposition
of chi sub A with pi. 

I'll leave it as an exercise to show that this function is the characteristic
function of the pre-image of A with respect to pi.

Putting this all together, we see that the probability A with respect to pi 
star A is the probability of all elements of X_0 which map to A under pi
with respect to rho.

Goal accomplished. Now, let's go through some concrete examples.

Slide 9
-------

For example, let's say that pi projects a two dimensional space spanned by x 
and y onto the x coordinate and a probability distribution on R two.

In this case, we can compute the probability density, at least heuristically,
as the following integral.

Classically, this pushforward goes by the name of the marginal distribution
of rho associated to X.

Slide 10
--------

Let's say that pi is the inclusion of a finite subset, let's call it U,
of Euclidean space. 

Let's say we have the uniform distribution on X zero to X n.

In this case, the pushforward is a sum of dirac-delta distributions
supported on the subset.

So hopefully that's enough examples. Let's return to our original 
goal of creating a probability distribution from a tale.

Slide 11
--------

So let's say we have a table. Furthermore, let's assume that we have a
probability distribution on the set of indices of the table. Note that both
of these are finite data.

Now, since we defined a table to be a map, we can pushforward this 
distribution along the table to obtain a probability distribution on the
space of features.

Therefore, all we need to do is produce a natural probability distribution on
the set of indices of the table.

Slide 12
--------

Slide 13
--------

