.. _GettingStarted:

Getting Started
===============

Downloading the Code
--------------------

The ALBM source code is hosted on GitHub. To download the repository, ensure
that ``git`` is installed on your machine and then type:

.. code:: shell

   git clone https://github.com/tanzeli1982/ALBM.git

Prerequisites
-------------

ALBM is written in Fortran and requires:

* A Fortran compiler that supports the Fortran 90 standard (e.g., ``gfortran`` or Intel ``ifort``)
* An MPI implementation (e.g., ``OpenMPI`` or ``MVAPICH2``) for parallel execution
* The NetCDF library (version 4 or later) with Fortran bindings
* PnetCDF (Parallel-NetCDF) for parallel NetCDF I/O

On most Linux systems these can be installed via the system package manager.
For example, on Ubuntu/Debian:

.. code:: shell

   sudo apt-get install gfortran libnetcdf-dev libnetcdff-dev

On macOS, a common setup is:

.. code:: shell

   brew install gcc open-mpi netcdf

PnetCDF can be downloaded from:

   https://parallel-netcdf.github.io/wiki/Download.html

Typical PnetCDF build steps are::

   ./configure --prefix=/path/to/pnetcdf/install
   make
   make install

Building the Model
------------------

Navigate to the ``src`` directory and compile using the provided Makefile:

.. code:: shell

   cd ALBM/src
   make

On successful compilation, an executable (commonly ``bLake.exe`` or
``ALBM.exe`` depending on the build script) will be produced in the
``src`` directory.

If you need to adjust compiler flags or NetCDF library paths, edit the
``Makefile`` directly before running ``make``.

If your ALBM source tree includes ``make.sh`` (Intel) or ``gnu_make.sh``
(GNU), set ``NETCDF_HOME`` in the script to your PnetCDF installation
directory and then run the corresponding script.

Running the Model
-----------------

ALBM is controlled through the Fortran namelist file ``namelist.bLake``
located in the ``src`` directory. Before running, edit this file to set
the paths to your input data and choose the simulation period and modules
to activate. See :ref:`Inputs` for a full description of all namelist
parameters.

Once the namelist is configured, run the model from the ``src`` directory:

.. code:: shell

   ./ALBM.exe namelist.bLake

For MPI runs on Linux or macOS workstations, use:

.. code:: shell

   mpirun -np <ncores> ./ALBM.exe namelist.bLake

On Linux clusters, edit the job script (e.g., ``bLakeJob.sub``) to load
compiler/MPI modules and set ``NETCDF_HOME``, then submit with:

.. code:: shell

   sbatch bLakeJob.sub

Model output will be written to the directory specified by ``archive_dir``
in the ``[archive]`` namelist group. See :ref:`ModelOutput` for details
on the output format.

Input Data
----------

Input data required to run ALBM (lake morphometry, climate forcing, and
auxiliary gridded datasets) are available for download from:

   https://doi.org/10.6084/m9.figshare.22635064

After downloading, update the relevant path variables in ``namelist.bLake``
to point to your local copies.
