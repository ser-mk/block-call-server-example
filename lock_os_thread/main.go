package main

import (
	"fmt"
	"runtime"
	"sync"
	"time"
)

/*
#include <stdio.h>
#include <unistd.h>

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
*/
import "C"

func Cloop(count int, loop int, size int) {

	timeArray := make([]int64, count)
	var wg sync.WaitGroup
	var avg int64
	t1 := time.Now().UnixMicro()

	for i := 0; i < count; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			t := time.Now().UnixMicro()
			for i := 0; i < loop; i++ {
				_ = C.mult_matrix(C.size_t(size))
			}
			timeArray[i] = time.Now().UnixMicro() - t
			avg += timeArray[i]
		}()
	}
	wg.Wait()

	fmt.Println(timeArray)
	fmt.Println("avg =", avg/int64(count))
	fmt.Println("sum =", time.Now().UnixMicro()-t1)
}

func CloopFast(count int, loop int, size int) {
	timeArray := make([]int64, count)
	var wg sync.WaitGroup
	var avg int64
	t1 := time.Now().UnixMicro()

	for i := 0; i < count; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			t := time.Now().UnixMicro()
			FastCMultMatrix(C.size_t(size))
			timeArray[i] = time.Now().UnixMicro() - t
			avg += timeArray[i]
		}()
	}
	wg.Wait()

	fmt.Println(timeArray)
	fmt.Println("avg time :", avg/int64(count))
	fmt.Println("sum time :", time.Now().UnixMicro()-t1)
}

func main() {
	var count = runtime.GOMAXPROCS(0)
	const size = 190
	const loop = 20
	fmt.Println("===== GORUTINE EQUAL PROCS ======", count)
	Cloop(count, loop, size)

	fmt.Println("===== GORUTINE MORE MORE PROCS ======", count)
	count = count * 5
	Cloop(count, loop, size)

	// https://github.com/golang/go/issues/21827
	runtime.LockOSThread()
	fmt.Println("===== GORUTINE MORE MORE PROCS AND LockOSThread ======", count)
	Cloop(count, loop, size)

	fmt.Println("===== GORUTINE EQUAL PROCS AND LockOSThread ======", count)
	count = runtime.GOMAXPROCS(0)
	Cloop(count, loop, size)

	runtime.UnlockOSThread()

	fmt.Println("===== Fast C ======", count)
	CloopFast(count, loop, size)

	count = count * 5
	fmt.Println("===== Fast C ======", count)
	CloopFast(count, loop, size)

}
