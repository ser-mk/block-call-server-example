go test -gcflags="fastc-example-server=-std" -bench=.  -run Bench -timeout 2000m

#bash bench.sh
#goos: linux
#goarch: amd64
#pkg: fastc-example-server
#cpu: Westmere E56xx/L56xx/X56xx (Nehalem-C)
#BenchmarkCGO-2             	17306889	        59.97 ns/op
#BenchmarkFastCGO-2         	78309889	        15.78 ns/op
#BenchmarkGO-2              	800541379	         1.354 ns/op
#BenchmarkCGO_timer-2       	 4326824	       278.9 ns/op
#BenchmarkFastCGO_timer-2   	 7351843	       162.4 ns/op
#BenchmarkGO_timer-2        	13134422	        93.35 ns/op
#BenchmarkCGO_clear-2       	   21888	     52595 ns/op
#BenchmarkFastCGO_clear-2   	   23187	     51655 ns/op
#BenchmarkGO_clear-2        	   20985	     56261 ns/op
#PASS
#ok  	fastc-example-server	758.607s

