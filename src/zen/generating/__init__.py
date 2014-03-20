"""
The ``zen.generating`` package contains functions for generating various standard graphs and networks.  
As in other modules, calling and return conventions have been standardized wherever possible.

In this package, a network is generated by a single call to a generation function.  Generation functions have specialized parameters
which will be the first positional arguments.  Optional keyword arguments may include:

	* ``directed [=False]`` (boolean): for functions that support the option of generating either a directed or undirected network, this
	  parameter indicates which should be generated.
	* ``seed [=-1]`` (int): set the seed for a random generator being used to generate the network.  Note that deterministic generation
	  algorithms will not support (or need) this argument.  The default value causes no internal seed to be set, producing the
	  effect of causing the generator to use whatever the current seed is. This value is passed directly to the ``srand(...)`` system
	  function, so reference documentation on the system random number generator for more details about usage of this parameters.

.. note::
	Except where noted, the generating function ``<gen_fxn>`` is available as ``zen.generating.<gen_fxn>`` (meaning that you don't have to import
	the function's containing module).
	
Random graph models
-------------------

.. autofunction:: zen.generating.erdos_renyi(n,p[,directed=False,self_loops=False,seed=-1])

.. autofunction:: zen.generating.barabasi_albert(n,m[,directed=False,seed=-1])

.. autofunction:: zen.generating.local_attachment(n,m,r[,seed=-1])

.. autofunction:: zen.generating.local_attachment(n,m,r[,seed=-1,graph=None])

.. autofunction:: zen.generating.duplication_divergence_iky(n,s[,directed=False,seed=-1,graph=None])

"""

from rgm import *
from duplication import *
from local import *
