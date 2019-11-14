.. _chapter-workflow:

Workflow
========

Having a solid and documented workflow is paramount to maintaining a clean
codebase when multiple contributors are involved. In this chapter, I'm
highlighting some of the conventions I adopted, while also trying to discuss
the reasons leading me to these choices.

The following diagram documents how this template makes use of automation and
continuous integration platforms, and where they can impact your development
workflow. You will find more information about goals and configuration
requirements in the :ref:`chapter-ci`  and :ref:`chapter-standard-tools`
chapters.

.. graphviz:: assets/flow/ci.gv
    :align: center
    :caption: High-level development flow and Quality Gates`

.. toctree::
    :maxdepth: 4
    :caption: Table of Content:

    ci/index.rst
    conventions/index.rst
    structure/index.rst
