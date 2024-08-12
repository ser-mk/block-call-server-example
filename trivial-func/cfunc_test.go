package trivial_func

import (
	"fmt"
	"testing"
	_ "unsafe"
)

func BenchmarkCGO(b *testing.B) {
	for i := 0; i < b.N; i++ {
		cgo_trivial(1)
	}
}

func BenchmarkFastCGO(b *testing.B) {
	for i := 0; i < b.N; i++ {
		fast_cgo_trivial(1)
	}
}

func BenchmarkGO(b *testing.B) {
	for i := 0; i < b.N; i++ {
		go_trivial(1)
	}
}

//--------------------------------------------------

func BenchmarkCGO_timer(b *testing.B) {
	for i := 0; i < b.N; i++ {
		b.StartTimer()
		cgo_trivial(1)
		b.StopTimer()
	}
}

func BenchmarkFastCGO_timer(b *testing.B) {
	for i := 0; i < b.N; i++ {
		b.StartTimer()
		fast_cgo_trivial(1)
		b.StopTimer()
	}
}

func BenchmarkGO_timer(b *testing.B) {
	for i := 0; i < b.N; i++ {
		b.StartTimer()
		go_trivial(1)
		b.StopTimer()
	}
}

// --------------------------------------------------
const sizeA = 1024 * 1024 * 20

var a [sizeA]byte

//go:linkname nanotime runtime.nanotime
func nanotime() int64

func clear() {
	for i := 0; i < sizeA; i += 128 {
		a[i] += 1
	}
}

const N = 1000

func TestBenchCGO_clearCache(t *testing.T) {
	var sum int64
	sum = 0
	for i := 0; i < N; i++ {
		t := nanotime()
		cgo_trivial(1)
		sum += nanotime() - t
		clear()
	}
	fmt.Println("Avarage time for general CGo func:", sum/N, "ns")
}

func TestBenchFastCGO_clearCache(t *testing.T) {
	var sum int64
	sum = 0
	for i := 0; i < N; i++ {
		t := nanotime()
		fast_cgo_trivial(1)
		sum += nanotime() - t
		clear()
	}
	fmt.Println("Avarage time for fast C call func:", sum/N, "ns")
}

func TestBenchGO_clearCache(t *testing.T) {
	var sum int64
	sum = 0
	for i := 0; i < N; i++ {
		t := nanotime()
		go_trivial(1)
		sum += nanotime() - t
		clear()
	}
	fmt.Println("Avarage time for Go call func:", sum/N, "ns")
}
