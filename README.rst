
.. image:: https://badge.fury.io/py/sequana-depletion.svg
     :target: https://pypi.python.org/pypi/sequana_depletion

.. image:: http://joss.theoj.org/papers/10.21105/joss.00352/status.svg
    :target: http://joss.theoj.org/papers/10.21105/joss.00352
    :alt: JOSS (journal of open source software) DOI

.. image:: https://github.com/sequana/depletion/actions/workflows/main.yml/badge.svg
   :target: https://github.com/sequana/depletion/actions/workflows    




This is is the **depletion** pipeline from the `Sequana <https://sequana.readthedocs.org>`_ project

:Overview: select or deplete reads from input FastQ files given a reference
:Input: Fastq Files
:Output: Fastq Files
:Status: production
:Citation: Cokelaer et al, (2017), ‘Sequana’: a Set of Snakemake NGS pipelines, Journal of Open Source Software, 2(16), 352, JOSS DOI doi:10.21105/joss.00352


Installation
~~~~~~~~~~~~

Install this package as follows::

    pip install sequana_depletion

it requires https://sequana.readthedocs.io and https://bioconvert.readthedocs.io for the bam to fastq conversion


Usage
~~~~~

::

    sequana_depletion --help
    sequana_depletion --input-directory DATAPATH --reference hg38.fa --mode depletion
    sequana_depletion --input-directory DATAPATH --reference covid.fa --mode selection

This creates a directory with the pipeline and configuration file. You will then need
to execute the pipeline::

    cd depletion
    sh depletion.sh  # for a local run

This launch a snakemake pipeline. If you are familiar with snakemake, you can
retrieve the pipeline itself and its configuration files and then execute the pipeline yourself with specific parameters::

    snakemake -s depletion.rules -c config.yaml --cores 4 --stats stats.txt

Or use `sequanix <https://sequana.readthedocs.io/en/master/sequanix.html>`_ interface.

Requirements
~~~~~~~~~~~~

This pipelines requires the following executable(s):

- bwa
- bioconvert
- samtools
- bamtools

#.. image:: https://raw.githubusercontent.com/sequana/depletion/master/sequana_pipelines/depletion/dag.png


Details
~~~~~~~~~

This pipeline runs **depletion** in parallel on the input fastq files (paired or not). 
A brief sequana summary report is also produced.


Rules and configuration details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the `latest documented configuration file <https://raw.githubusercontent.com/sequana/depletion/master/sequana_pipelines/depletion/config.yaml>`_
to be used with the pipeline. Each rule used in the pipeline may have a section in the configuration file. 

Changelog
~~~~~~~~~

========= ====================================================================
Version   Description
========= ====================================================================
0.1.0     **First release.**
========= ====================================================================


