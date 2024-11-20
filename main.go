package main

import "C"
import (
	"github.com/gin-gonic/gin"
	"net/http"
	"strconv"
)

func main() {

	router := gin.Default()

	router.GET("/cgo/:size/:loop", func(c *gin.Context) { mult(c, true) })
	router.GET("/blockcall/:size/:loop", func(c *gin.Context) { mult(c, false) })

	router.Run(":8081")
}

func mult(c *gin.Context, use_cgo bool) {
	str_size := c.Param("size")
	str_loop := c.Param("loop")
	size, _ := strconv.Atoi(str_size)
	loop, _ := strconv.Atoi(str_loop)
	sum := 0
	if use_cgo {
		for i := 0; i < loop; i++ {
			sum += CGOMultMatrix(size)
		}
	} else {
		for i := 0; i < loop; i++ {
			sum += WithoutCGOMultMatrix(size)
		}
	}
	c.IndentedJSON(http.StatusOK, sum)
}
