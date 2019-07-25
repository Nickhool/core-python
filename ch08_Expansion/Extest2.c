#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Python.h"

int fac(int n)
{
    if (n < 2) return(1); /* 0!== 1! == 1 */
    return n * fac(n-1); /* n! == n*(n-1) */
}

char *reverse(char *s)
{
    register char t,                 /* tmp */
            *p = s,                  /* fwd */
            *q = (s + (strlen(s)-1));/* bwd */

    while (p < q)           /* if p < q */
    {                       /* swap & mv ptrs */
        t = *p;
        *p++ = *q;
        *q-- = t;
    }
    return s;
}

int test()
{
    char s[BUFSIZ];
    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    printf("12! == %d\n", fac(12));
    strcpy(s, "abcdef");
    printf("reversing 'abcdef', we get '%s'\n", reverse(s));
    strcpy(s, "madam");
    printf("reversing 'madam', we get '%s'\n", reverse(s));
    return 0;
}

static PyObject *
Extest_fac(PyObject *self, PyObject *args) {
    int num;
    if (!PyArg_ParseTuple(args, "i", &num))
        return NULL;
    return (PyObject*)Py_BuildValue("i", fac(num));
}

static PyObject *
Extest_doppel(PyObject *self, PyObject *args) {
    char *orig_str;     // original string
    char *dupe_str;
    PyObject* retval;

    if (!PyArg_ParseTuple(args, "s", &orig_str)) return NULL;
    retval = (PyObject*)Py_BuildValue("ss", orig_str, dupe_str=reverse(strdup(orig_str)));
    free(dupe_str);
    return retval;
}

static PyObject*
Extest_test(PyObject *self, PyObject *args) {   // 添加测试函数
    test();
//    return (PyObject*)Py_BuildValue("");  // 采用空字符串返回None
    Py_INCREF(Py_None); // 采用引用计数返回None
    return Py_None;
}

static PyMethodDef
ExtestMethods[] = {
    {"fac", Extest_fac, METH_VARARGS },
    {"doppel", Extest_doppel, METH_VARARGS },
    {"test", Extest_test, METH_VARARGS },
    {NULL, NULL},
};

void initExtest() {
    Py_InitModule("Extest", ExtestMethods);
}