package main

import "C"
import (
	"fmt"
	"runtime"
	"sort"
	"sync"
	"time"
)

func median(data []int) int {
	dataCopy := make([]int, len(data))
	copy(dataCopy, data)

	sort.Ints(dataCopy)

	var median int
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

	timeArray := make([]int, count)
	var wg sync.WaitGroup
	var avg int
	t1 := time.Now().UnixMicro()

	for i := 0; i < count; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			t := time.Now().UnixMicro()
			if fast {
				for i := 0; i < loop; i++ {
					_ = FastCMultMatrix(C.size_t(size))
				}
			} else {
				for i := 0; i < loop; i++ {
					_ = MultMatrix(size)
				}
			}
			timeArray[i] = int(time.Now().UnixMicro() - t)
			avg += timeArray[i]
		}()
	}
	wg.Wait()

	fmt.Println(timeArray)
	fmt.Println("median \t=", median(timeArray))
	fmt.Println("sum \t=", time.Now().UnixMicro()-t1)
}

func main() {
	var count = runtime.GOMAXPROCS(0)
	const size = 222
	const loop = 44
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

	fmt.Println("===== Fast C ======", count)
	Cloop(count, loop, size, true)

	count = count * more
	fmt.Println("===== Fast C ======", count)
	Cloop(count, loop, size, true)

}
