package trivial_func

import "unsafe"

/*
int fun(int a) {
  return a;
}

typedef struct {
		int arg;
		int result;
	} Args;

void wrapper_fun(Args *args)
{
	args->result = fun(args->arg);
}
*/
import "C"

//go:nosplit
func fast_trivial(a int) int {
	args := C.Args{C.int(a), 0}
	asmcgocall(C.wrapper_fun, uintptr(unsafe.Pointer(&args)))
	return int(args.result)
}

//go:linkname asmcgocall runtime.asmcgocall
//go:noescape
func asmcgocall(unsafe.Pointer, uintptr) int32

//go:noinline
func go_trivial(a int) int {
	return a
}

//go:noinline
func cgo_trivial(a int) int {
	return int(C.fun(C.int(a)))
}
