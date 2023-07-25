#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

PyObject *sum_float_arr(PyObject* self, PyObject* args) {
    PyObject *pList;
    PyObject *pItem;
    Py_ssize_t n;
    int i;
    double total = 0;
    
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &pList)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be a list.");
        return NULL;
    }
    n = PyList_Size(pList);
    for (i=0; i<n; i++) {
        pItem = PyList_GetItem(pList, i);
        total += PyFloat_AsDouble(pItem);
    }
    return PyFloat_FromDouble(total);
}

PyObject *sum_int_arr(PyObject* self, PyObject* args) {
    PyObject *pList;
    PyObject *pItem;
    Py_ssize_t n;
    int i;
    long total = 0;
    
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &pList)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be a list.");
        return NULL;
    }
    n = PyList_Size(pList);
    for (i=0; i<n; i++) {
        pItem = PyList_GetItem(pList, i);
        if(!PyLong_Check(pItem)) {
            PyErr_SetString(PyExc_TypeError, "list items must be integers (long).");
            return NULL;
        }
        total += PyLong_AsLong(pItem);

    }
    return PyLong_FromLong(total);
}

PyObject *sum_arr(PyObject* self, PyObject* args) {
    PyObject *pList;
    PyObject *pItem;
    Py_ssize_t n;
    int i;
    long l_total = 0;
    double d_total = 0;
    bool list_has_floats = false;

    
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &pList)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be a list.");
        return NULL;
    }
    n = PyList_Size(pList);
    for (i=0; i<n; i++) {
        pItem = PyList_GetItem(pList, i);
        if (PyFloat_Check(pItem)) {
            list_has_floats = true;
            d_total += PyFloat_AsDouble(pItem);
        }
        else if(PyLong_Check(pItem)) {
            l_total += PyLong_AsLong(pItem);
        }
        else {
            PyErr_SetString(PyExc_TypeError, "list items must be integers or floats.");
            return NULL;
        }
    }
    if (list_has_floats) {
        return PyFloat_FromDouble(d_total + l_total);
    }
    return PyLong_FromLong(l_total);
}

static PyMethodDef methods[] = {
    {"sum_float_arr", sum_float_arr, METH_VARARGS, "sum of an array of floats"},
    {"sum_int_arr", sum_int_arr, METH_VARARGS, "sum of an array of integers"},
    {"sum_arr", sum_arr, METH_VARARGS, "sum of two numbers with type checking"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef csum = {
    PyModuleDef_HEAD_INIT,
    "csum",
    "sum functions",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_csum(void) {
    return PyModule_Create(&csum);
}
