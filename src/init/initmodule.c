/*
 * author: Pierre Schnizer
 * created: March 2004
 * file: pygsl/src/initmodule.c
 * $Id$
 *
 * Changes: 
 *     7. October 2003:
 *     Removed the error handler from this file. It is now in 
 *     Lib/error_helpers.c Each module must call init_pygsl()
 *     in its init routine. This is necessary to support platforms
 *     where the gsl library is statically linked to the various 
 *     modules.    
 */

#include <gsl/gsl_rng.h>
#include <gsl/gsl_ieee_utils.h>
#include <gsl/gsl_version.h>
#include <Python.h>
#define  _PyGSL_API_MODULE 1
/* #define  PyGSL_IMPORT_API 1  */
#include <pygsl/intern.h>
#include <pygsl/error_helpers.h>

/* Taken from Modules/getbuildinfo */
#ifndef DATE
#ifdef __DATE__
#define DATE __DATE__
#else
#define DATE "xx/xx/xx"
#endif
#endif

#ifndef TIME
#ifdef __TIME__
#define TIME __TIME__
#else
#define TIME "xx:xx:xx"
#endif
#endif
/* End */


static char pygsl_error_str[512];

#include "error_helpers.c"
#include "general_helpers.c"
#include "complex_helpers.c"
#include "block_helpers.c"
#include "function_helpers.c"
#include "rng_helpers.c"

static void * _PyGSL_API[PyGSL_NENTRIES_NUM];
static PyMethodDef initMethods[] = {
  {NULL,     NULL}        /* Sentinel */
};


static void
PyGSL_init_api(void)
{
     int i;
     
     for(i=0;i<PyGSL_NENTRIES_NUM; ++i){
	  _PyGSL_API[i] = NULL;
     }
     _PyGSL_API[PyGSL_RNG_ObjectType_NUM                       ] = NULL;
     _PyGSL_API[PyGSL_error_flag_NUM                           ] = (void *) &PyGSL_error_flag;
     _PyGSL_API[PyGSL_error_flag_to_pyint_NUM                  ] = (void *) &PyGSL_error_flag_to_pyint;
     _PyGSL_API[PyGSL_add_traceback_NUM                        ] = (void *) &PyGSL_add_traceback;    
     _PyGSL_API[PyGSL_module_error_handler_NUM                 ] = (void *) &PyGSL_module_error_handler;

     _PyGSL_API[PyGSL_error_string_for_callback_NUM            ] = (void *) & PyGSL_set_error_string_for_callback        ;
     _PyGSL_API[PyGSL_pyfloat_to_double_NUM                    ] = (void *) & PyGSL_pyfloat_to_double                    ;
     _PyGSL_API[PyGSL_pylong_to_ulong_NUM                      ] = (void *) & PyGSL_pylong_to_ulong                      ;
     _PyGSL_API[PyGSL_pylong_to_uint_NUM                       ] = (void *) & PyGSL_pylong_to_uint                       ;
     _PyGSL_API[PyGSL_check_python_return_NUM                  ] = (void *) & PyGSL_check_python_return                  ;
     _PyGSL_API[PyGSL_clear_name_NUM                           ] = (void *) & PyGSL_clear_name                           ;


     _PyGSL_API[PyGSL_PyComplex_to_gsl_complex_NUM             ] = (void *) & PyGSL_PyComplex_to_gsl_complex             ;
     _PyGSL_API[PyGSL_PyComplex_to_gsl_complex_float_NUM       ] = (void *) & PyGSL_PyComplex_to_gsl_complex_float       ;
     _PyGSL_API[PyGSL_PyComplex_to_gsl_complex_long_double_NUM ] = (void *) & PyGSL_PyComplex_to_gsl_complex_long_double ;

     _PyGSL_API[PyGSL_stride_recalc_NUM                        ] = (void *) & PyGSL_stride_recalc                        ;
     _PyGSL_API[PyGSL_PyArray_new_NUM                          ] = (void *) & PyGSL_New_Array                            ;
     _PyGSL_API[PyGSL_PyArray_copy_NUM                         ] = (void *) & PyGSL_Copy_Array                           ;
     _PyGSL_API[PyGSL_PyArray_prepare_gsl_vector_view_NUM      ] = (void *) & PyGSL_PyArray_prepare_gsl_vector_view      ;
     _PyGSL_API[PyGSL_PyArray_prepare_gsl_matrix_view_NUM      ] = (void *) & PyGSL_PyArray_prepare_gsl_matrix_view      ;
     _PyGSL_API[PyGSL_PyArray_generate_gsl_vector_view_NUM     ] = (void *) & PyGSL_PyArray_generate_gsl_vector_view     ;
     _PyGSL_API[PyGSL_PyArray_generate_gsl_matrix_view_NUM     ] = (void *) & PyGSL_PyArray_generate_gsl_matrix_view     ;
     _PyGSL_API[PyGSL_copy_pyarray_to_gslvector_NUM            ] = (void *) & PyGSL_copy_pyarray_to_gslvector            ;
     _PyGSL_API[PyGSL_copy_pyarray_to_gslmatrix_NUM            ] = (void *) & PyGSL_copy_pyarray_to_gslmatrix            ;
     _PyGSL_API[PyGSL_copy_gslvector_to_pyarray_NUM            ] = (void *) & PyGSL_copy_gslvector_to_pyarray            ;
     _PyGSL_API[PyGSL_copy_gslmatrix_to_pyarray_NUM            ] = (void *) & PyGSL_copy_gslmatrix_to_pyarray            ;

     _PyGSL_API[PyGSL_gsl_rng_from_pyobject_NUM                ] = (void *) & PyGSL_gsl_rng_from_pyobject                ;
     _PyGSL_API[PyGSL_function_wrap_helper_NUM                 ] = (void *) & PyGSL_function_wrap_helper                 ;
     
}

DL_EXPORT(void) initinit(void)
{
  PyObject *m = NULL, *d = NULL, *version=NULL, *date=NULL, *api = NULL;

  m = Py_InitModule("pygsl.init", initMethods);
  import_array();
  
  
  if(m == NULL){
       fprintf(stderr, "I could not init pygsl.init!");
       return;
  }

  d = PyModule_GetDict(m);
  if(d == NULL){
       fprintf(stderr, "I could not get the module dict for  pygsl.init!");
       return;
  }

  PyGSL_init_api();
  PyGSL_API = _PyGSL_API;
  PyGSL_SET_ERROR_HANDLER();

  api = PyCObject_FromVoidPtr((void *) PyGSL_API, NULL);
  assert(api);
  if (PyDict_SetItemString(d, "_PYGSL_API", api) != 0){
       PyErr_SetString(PyExc_ImportError, 
		       "I could not add  _PYGSL_API!");
       return;
  }

  version = PyString_FromString(GSL_VERSION);
  if(version == NULL){
       fprintf(stderr, "I could not create the version string for pygsl.init!");
       return;
  }
  if(PyDict_SetItemString(d, "compiled_gsl_version", version) != 0){
       fprintf(stderr, "I could not add the compile version string to the module dict of pygsl.init!");
       return;
  }

  version = PyString_FromString(gsl_version);
  if(version == NULL){
       fprintf(stderr, "I could not create the version string for pygsl.init!");
       return;
  }
  if(PyDict_SetItemString(d, "run_gsl_version", version) != 0){
       fprintf(stderr, "I could not add the run version string to the module dict of pygsl.init!");
       return;
  }

  date = PyString_FromString(DATE " " TIME);
  if(version == NULL){
       fprintf(stderr, "I could not create the date string for pygsl.init!");
       return;
  }
  if(PyDict_SetItemString(d, "compile_date", date) != 0){
       fprintf(stderr, "I could not add the date version string to the module dict of pygsl.init!");
       return;
  }

  /*
   * These functions will be moved to the approbriate modules and the user will
   * have to call them explicitly when needed.
   */
  /* setup gsl mode and ieee modes from environment variable GSL_IEEE_MODE */
  gsl_ieee_env_setup();
  /* setup default random generator from environment variables */
  gsl_rng_env_setup();
  
  return;
}
