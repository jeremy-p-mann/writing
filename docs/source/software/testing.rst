Testing
=======

Costs, benefits, risks of tests, along with tips based on the principles that 
we should maximize benefits and minimize costs and risks.

Benefits of Tests
-----------------

Tests can increase the cost of (undesirable) changes.

Tests can provide valuable feedback.

Test code can document requirements.

The side effects of the execution of test code within an environment document
how the application is meeting the requirements.

Cost of Tests
-------------

Tests cost time.

Tests cost money.

Risks of Tests
--------------

Tests can increase the cost of desirable changes.

Testing Tips
------------

Maximize Benefits
~~~~~~~~~~~~~~~~~

Tests should be reproducible.

Tests which test the code should give the same results irrespective of 
the environment in which it is being deployed.

Apply scientific reasoning.

All code should be tested. Test code is code. Tests can fail to fail.

Make the answer to the question: "what is the subject of the test" obvious.

Tests should only test the subject of the test.

The type of changes that the test make hard can be used as a descriptor a test.

Subsets of tests

Minimize Risks
~~~~~~~~~~~~~~

Tests should only test requirements.

Tests should be conservative with the changes it makes more difficult.

Minimize Costs
~~~~~~~~~~~~~~

We should get computers to execute tests.

We make our test suite parallelizable.

We should make our tests faster, e.g. by minimizing i/o.

Tests should localize their side effects to standard out and standard error.

