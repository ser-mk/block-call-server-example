package main

import (
	"fmt"
	"testing"
)

func ExampleMult() {
	r := CGOMultMatrix(11)
	fmt.Println(r)
	// Output: -7700
}

func ExampleFastMult() {
	r := WithoutCGOMultMatrix(11)
	fmt.Println(r)
	// Output: -7700
}

func TestBoth(t *testing.T) {
	a := CGOMultMatrix(11)
	b := WithoutCGOMultMatrix(11)
	println(a, b)
	if int(a) != int(b) {
		t.Error("no equal")
	}
}
