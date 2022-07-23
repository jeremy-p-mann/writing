Infrastructure as Code (IAC)
============================

IAC = Manage infrastructure with software techniques

Marker of IAC
-------------

How much effort would it take to deploy a copy of the system that was running
in production 2 years ago into a test environment?

Goal of IAC
-----------

Push a button.

Strategy: Immutable Infrastructure
----------------------------------

"The server is created from scratch for every change."

Features/Components:
~~~~~~~~~

#. Declarative Definition. Say what your system is, not how to build it.
#. Audit trail of infrastructure.
#. Simple and consistent scaling.
#. Eliminates manual execution errors, more generally configuration drift.
#. TESTABLE.

Warning: 
~~~~~~~~

Can be slow(er) to provision. Employ modern tooling, e.g. caching and 
incremental building.


Principles
----------

#. Systems can be easily reproduced. 
#. Systems are disposable
#. Systems are consistent
#. Processes are repeatable
#. Systems are always changing.


Practices
---------

#. Define your infrastructure in files ("soft infrastructure").
#. Treat server as cattle rather than pets
#. Make infrastructure "self-documenting". The system builds the docs.
#. Version-control everything. Your infrastructure are defined in files.
#. Continuously test systems & processes.
#. Make changes in small steps.
#. Keep services continuously available.
#. Prefer unattended execution over interactive use. Put a VCS between people 
   and system.

Acknowledgements
----------------

Copied from Farley's "What Is Infrastructure As Code?"
video.
