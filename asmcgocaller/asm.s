#include "go_asm.h"

#include "funcdata.h"
#include "textflag.h"

//#include "go_tls.h"
#ifdef GOARCH_arm
#define LR R14
#endif

#ifdef GOARCH_amd64
#define	get_tls(r)	MOVQ TLS, r
#define	g(r)	0(r)(TLS*1)
#endif

#ifdef GOARCH_386
#define	get_tls(r)	MOVL TLS, r
#define	g(r)	0(r)(TLS*1)
#endif



#ifdef GOOS_windows
#define RARG0 CX
#define RARG1 DX
#define RARG2 R8
#define RARG3 R9
#else
#define RARG0 DI
#define RARG1 SI
#define RARG2 DX
#define RARG3 CX
#endif


// func Asmcgocall(fn, arg unsafe.Pointer) int32
TEXT	·Asmcgocall(SB), NOSPLIT, $0-32
	JMP	runtime·asmcgocall(SB)

