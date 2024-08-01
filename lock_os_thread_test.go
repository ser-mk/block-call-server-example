package main

import (
	"fmt"
	"runtime"
	"sort"
	"sync"
	"testing"
	"time"
)

func median(data []int64) int64 {
	dataCopy := make([]int64, len(data))
	copy(dataCopy, data)

	sort.Slice(dataCopy, func(i, j int) bool { return dataCopy[i] < dataCopy[j] })

	var median int64
	l := len(dataCopy)
	if l == 0 {
		return 0
	} else if l%2 == 0 {
		median = (dataCopy[l/2-1] + dataCopy[l/2]) / 2
	} else {
		median = dataCopy[l/2]
	}

	return median
}

func Cloop(count int, loop int, size int, fast bool) {

	timeOfWork := make([]int64, count)
	timeWithWait := make([]int64, count)
	var wg sync.WaitGroup
	var avg int64
	tStart := time.Now().UnixMicro()

	for i := 0; i < count; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			t := time.Now().UnixMicro()
			if fast {
				for i := 0; i < loop; i++ {
					_ = WithoutCGOMultMatrix(size)
				}
			} else {
				for i := 0; i < loop; i++ {
					_ = CGOMultMatrix(size)
				}
			}
			timeOfWork[i] = time.Now().UnixMicro() - t
			avg += timeOfWork[i]
			timeWithWait[i] = time.Now().UnixMicro() - tStart
		}()
	}
	wg.Wait()
	tfinish := time.Now().UnixMicro()

	fmt.Println("work time of every gorutine:", timeOfWork)
	fmt.Println("median \t=", median(timeOfWork))
	fmt.Println("sum \t=", tfinish-tStart)
	fmt.Println("time with delay of every gorutine:", timeWithWait)
	sort.Slice(timeWithWait, func(i, j int) bool { return timeWithWait[i] < timeWithWait[j] })
	fmt.Println("sort time with delay of every gorutine:", timeWithWait)
}

func TestLockOSThread(t *testing.T) {

	var count = runtime.GOMAXPROCS(0)
	const size = 222
	const loop = 22
	const more = 5

	count = runtime.GOMAXPROCS(0)
	fmt.Println("===== GORUTINE EQUAL PROCS ======", count)
	Cloop(count, loop, size, false)

	count = count * more
	fmt.Println("===== GORUTINE MORE MORE PROCS ======", count)
	Cloop(count, loop, size, false)

	// https://github.com/golang/go/issues/21827
	runtime.LockOSThread()
	fmt.Println("===== GORUTINE MORE MORE PROCS AND LockOSThread ======", count)
	Cloop(count, loop, size, false)

	count = runtime.GOMAXPROCS(0)
	fmt.Println("===== GORUTINE EQUAL PROCS AND LockOSThread ======", count)
	Cloop(count, loop, size, false)

	runtime.UnlockOSThread()

	fmt.Println("===== Fast C ======", count)
	Cloop(count, loop, size, true)

	count = count * more
	fmt.Println("===== Fast C ======", count)
	Cloop(count, loop, size, true)

}
