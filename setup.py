#! /usr/bin/env python2
#
# author: Achim Gaedke
# created: May 2001
# file: pygsl/setup.py
# $Id$
#
# setup script for building and installing pygsl

import sys
from distutils.core import setup, Extension
from gsl_Extension import gsl_Extension

pygsl_const=gsl_Extension("const",
			  ['src/constmodule.c'],
                          gsl_min_version=(1,2),
                          python_min_version=(2,1)
                          )
pygsl_diff = gsl_Extension("diff",
                           ['src/diffmodule.c'],
                           gsl_min_version=(1,'0+'),
                           python_min_version=(2,1)
                           )
pygsl_histogram=gsl_Extension("histogram",
                              ['src/histogrammodule.c'],
                              gsl_min_version=(1,'0+'),
                              python_min_version=(2,2)
                              )
pygsl_histogram=gsl_Extension("matrix",
                              ['src/matrixmodule.c'],
                              gsl_min_version=(1,'0+'),
                              python_min_version=(2,2)
                              )
pygsl_histogram=gsl_Extension("multimin",
                              ['src/multiminmodule.c'],
                              gsl_min_version=(1,'0+'),
                              python_min_version=(2,2)
                              )
pygsl_ieee=gsl_Extension("ieee",
			 ['src/ieeemodule.c'],
                         gsl_min_version=(1,),
                         python_min_version=(2,1)
                         )
pygsl_init=gsl_Extension("init",
			 ['src/initmodule.c'],
                         gsl_min_version=(1,),
                         python_min_version=(2,1)
                         )
pygsl_rng=gsl_Extension("rng",
			 ['src/rngmodule.c'],
                         gsl_min_version=(1,'0+'),
                         python_min_version=(2,2)
                         )
pygsl_sf=gsl_Extension("sf",
		       ['src/sfmodule.c'],
		       gsl_min_version=(1,),
                       python_min_version=(2,1)
                       )
pygsl_statistics_uchar=gsl_Extension("statistics.uchar",
                                     ['src/statistics/ucharmodule.c'],
                                     gsl_min_version=(1,),
                                     python_min_version=(2,1)
                                     )
pygsl_statistics_char=gsl_Extension("statistics.char",
                                    ['src/statistics/charmodule.c'],
                                    gsl_min_version=(1,),
                                    python_min_version=(2,1)
                                    )
pygsl_statistics_double=gsl_Extension("statistics.double",
                                      ['src/statistics/doublemodule.c'],
                                      gsl_min_version=(1,),
                                      python_min_version=(2,1)
                                      )
pygsl_statistics_float=gsl_Extension("statistics.float",
                                     ['src/statistics/floatmodule.c'],
                                     gsl_min_version=(1,),
                                     python_min_version=(2,1)
                                      )
pygsl_statistics_long=gsl_Extension("statistics.long",
                                    ['src/statistics/longmodule.c'],
                                    gsl_min_version=(1,),
                                    python_min_version=(2,1)
                                    )
pygsl_statistics_int=gsl_Extension("statistics.int",
                                   ['src/statistics/intmodule.c'],
                                   gsl_min_version=(1,),
                                   python_min_version=(2,1)
                                   )
pygsl_statistics_short=gsl_Extension("statistics.short",
                                     ['src/statistics/shortmodule.c'],
                                     gsl_min_version=(1,),
                                     python_min_version=(2,1)
                                     )


setup (name = "pygsl",
       version = "0.1a",
       description = "GNU Scientific Library Interface",
       author = "Achim Gaedke",
       author_email = "AchimGaedke@users.sourceforge.net",
       url = "http://pygsl.sourceforge.net",
       py_modules = ['pygsl.errors',
                     'pygsl.statistics.__init__'
                     ],
       ext_package = 'pygsl',
       ext_modules = [pygsl_const,
                      pygsl_diff,
                      pygsl_histogram,
                      pygsl_ieee,
                      pygsl_init,
                      pygsl_rng,
                      pygsl_sf,
                      pygsl_statistics_char,
                      pygsl_statistics_uchar,
                      pygsl_statistics_double,
                      pygsl_statistics_float,
                      pygsl_statistics_int,
                      pygsl_statistics_long,
                      pygsl_statistics_short,
                      ]
       )



