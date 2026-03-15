.. _GettingStarted:

Getting Started
===============

Downloading the Code
--------------------

The ALBM source code is hosted on GitHub. To download the repository, ensure
that ``git`` is installed on your machine and then type:

.. code:: shell

   git clone https://github.com/tanzeli1982/ALBM.git

or downloading the new CH₄ branch

.. code:: shell

   git clone -b CH4_new https://github.com/tanzeli1982/ALBM.git

Prerequisites
-------------

ALBM is written in Fortran and requires:

* A Fortran compiler that supports the Fortran 90 standard (e.g., ``gfortran`` or Intel ``ifort``)
* A Message Passing Interface (MPI) implementation (e.g., ``OpenMPI`` or ``MVAPICH2``) for parallel execution
* PnetCDF (Parallel-NetCDF) for parallel NetCDF I/O

On most Linux systems these can be installed via the system package manager.
For example, on Ubuntu/Debian:

.. code:: shell

   sudo apt-get install gfortran
   sudo apt-get install openmpi-bin openmpi-common libopenmpi-dev

or

.. code:: shell

   sudo apt-get install gfortran
   sudo apt-get install mvapich2 libmvapich2-dev

After installation, ensure that the installed binaries and libraries (usually located in ``/usr/local/bin`` 
and ``/usr/local/lib``) are in your system's environment variables (e.g., ``PATH`` and ``LD_LIBRARY_PATH``). 
For example, 

.. code:: shell

   export PATH=/path/to/openmpi/bin:$PATH
   export LD_LIBRARY_PATH=/path/to/openmpi/lib:$LD_LIBRARY_PATH

In Linux clusters, Fortran compiler and MPI modules may have been installed as modules. 
You need to load the appropriate Fortran compiler and MPI modules before building ALBM and PnetCDF.

.. code:: shell

   module load gcc openmpi

or

.. code:: shell

   module load intel mvapich2


On macOS, a common setup is:

.. code:: shell

   brew install gcc open-mpi

or

.. code:: shell

   brew install gcc mpich

After installation, ensure that the installed binaries and libraries (usually located in ``/opt/homebrew/bin`` 
and ``/opt/homebrew/lib``) are in your system's environment variables (e.g., ``PATH`` and ``LD_LIBRARY_PATH``).

.. code:: shell

   export PATH=/path/to/openmpi/bin:$PATH
   export LD_LIBRARY_PATH=/path/to/openmpi/lib:$LD_LIBRARY_PATH

PnetCDF can be downloaded from (the versions <= 1.14.1 have been tested with ALBM):

   https://parallel-netcdf.github.io/wiki/Download.html

Typical PnetCDF build steps are:

.. code:: shell
   
   ./configure --prefix=/path/to/pnetcdf/install
   make
   make install

Building the Model
------------------

Navigate to the ``src`` directory and compile using the provided make script 
(e.g., ``make.sh`` for Intel or ``gnu_make.sh`` for GNU compilers). 
Ensure that you have set the correct path (``NETCDF_HOME``) to your PnetCDF installation 
(``/path/to/pnetcdf/install``) in the script:

.. code:: shell

   cd ALBM/src
   ./gnu_make.sh

For debug mode, run:

.. code:: shell

   ./gnu_make.sh clean
   ./gnu_make.sh debug

For a clean rebuild, run:

.. code:: shell

   ./gnu_make.sh clean
   ./gnu_make.sh

On successful compilation, an executable (``ALBM.exe``) will be produced in the
``src`` directory.

If you need to adjust compiler flags or NetCDF library paths, edit the
``Makefile`` directly before running the make script.

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

or 

.. code:: shell

   srun -n <ncores> ./ALBM.exe namelist.bLake

where ``<ncores>`` is the number of CPU cores to use for parallel execution.

On Linux clusters, edit the job script (e.g., ``bLakeJob.sub``) to load
compiler/MPI modules and set ``NETCDF_HOME``, then submit with:

.. code:: shell

   sbatch bLakeJob.sub

Model output will be written to the directory specified by ``archive_dir``
in the ``[archive]`` namelist group. See :ref:`ModelOutput` for details
on the output format.

Input Data
----------

Example input data to run ALBM (lake morphometry, climate forcing, and
auxiliary gridded datasets) are available for download from:

   https://doi.org/10.6084/m9.figshare.22635064

After downloading, update the relevant path variables in ``namelist.bLake``
to point to your local copies. See :ref:`Inputs` for details on the required input data formats 
and generating your own input data.