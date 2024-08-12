package trivial_func

/*

int trivial_fun(int a) {
  return a;
}

typedef struct {
		int a;
		int result;
	} Trivial_Args;

void
_cgo_wrapper_trivial_fun(Trivial_Args *args)
{
	args->result = trivial_fun(args->a);
}

*/
import "C"
import (
	"unsafe"
)

//go:noinline
func go_trivial(a int) int {
	return a
}

//go:noinline
func cgo_trivial(a int) int {
	return int(C.trivial_fun(C.int(a)))
}

//go:nosplit
func fast_cgo_trivial(a int) int {
	args := C.Trivial_Args{C.int(a), 0}
	asmcgocall(C._cgo_wrapper_trivial_fun, uintptr(unsafe.Pointer(&args)))
	if _Cgo_always_false {
		_Cgo_use(args)
	}
	return int(args.result)
}
