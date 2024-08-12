package main

/*
#include <stdio.h>
#include <stdint.h>
#include <errno.h>

#define MAX_SIZE 300

int mult_matrix(size_t test_size){

int a[MAX_SIZE][MAX_SIZE],
	b[MAX_SIZE][MAX_SIZE],
	c[MAX_SIZE][MAX_SIZE];

	size_t i, j, k;

	if (test_size > MAX_SIZE){
		errno = -1;
		return 0;
	}

	for (i = 0; i < test_size; i++) {
        for (j = 0; j < test_size; j++) {
            a[j][i] = -i*5 + j*6;
        }
    }

	for (i = 0; i < test_size; i++) {
		for (j = 0; j < test_size; j++) {
			b[j][i] = -i*7 + j*14;
		}
	}

	for (i = 0; i < test_size; i++) {
		for (j = 0; j < test_size; j++) {
			c[i][j] = 0;
			for (k = 0; k < test_size; k++) {
				c[i][j] += a[i][k] * b[k][j];
			}
		}
	}

	for (i = 0; i < test_size; i++) {
        for (j = 0; j < test_size; j++) {
            a[j][i] = 0;
        }
    }

	for (i = 0; i < test_size; i++) {
		for (j = 0; j < test_size; j++) {
			b[j][i] = 0;
		}
	}


	return a[0][0] + b[0][0] + c[test_size - 1][test_size - 1];

}

typedef struct {
		int size;
		int result;
	} Mult_Args;

void
fast_C_mult_matrix(Mult_Args *args)
{
	args->result = mult_matrix(args->size);
}
*/
import "C"
import "unsafe"

func MultMatrix(size int) int {
	return int(C.mult_matrix(C.size_t(size)))
}

//go:linkname asmcgocall runtime.asmcgocall
//go:noescape
func asmcgocall(unsafe.Pointer, uintptr) int32

//go:nosplit
func FastCMultMatrix(size int) int {
	args := C.Mult_Args{C.int(size), 0}
	asmcgocall(C.fast_C_mult_matrix, uintptr(unsafe.Pointer(&args)))
	if _Cgo_always_false {
		_Cgo_use(args)
	}
	return int(args.result)
}
