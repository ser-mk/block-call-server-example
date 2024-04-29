package main

/*

int trivial_fun(int a) {
  return a;
}

extern char* _cgo_topofstack(void);

void
_cgo_wrapper_trivial_fun(void *v)
{
	struct {
		int p0;
		char __pad4[4];
		int r;
		char __pad12[4];
	} __attribute__((__packed__, __gcc_struct__)) *_cgo_a = v;
	char *_cgo_stktop = _cgo_topofstack();
	__typeof__(_cgo_a->r) _cgo_r;
	_cgo_r = trivial_fun(_cgo_a->p0);
	_cgo_a = (void*)((char*)_cgo_a + (_cgo_topofstack() - _cgo_stktop));
	_cgo_a->r = _cgo_r;
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
//go:cgo_unsafe_args
func fast_Cfunc_trivial_fun(p0 C.int) (r1 C.int) {
	asmcgocall(C._cgo_wrapper_trivial_fun, uintptr(unsafe.Pointer(&p0)))
	if _Cgo_always_false {
		_Cgo_use(p0)
	}
	return
}

//go:noinline
func fast_cgo_trivial(a int) int {
	return int(fast_Cfunc_trivial_fun(C.int(a)))
}
