package main

import "C"
import (
	"github.com/gin-gonic/gin"
	"net/http"
	"strconv"
)

func main() {

	router := gin.Default()

	router.GET("/cgo/:size/:loop", cgo)
	router.GET("/fastcgo/:size/:loop", fastcgo)

	router.Run(":8081")

}

func cgo(c *gin.Context) {
	str_size := c.Param("size")
	str_loop := c.Param("loop")
	size, _ := strconv.Atoi(str_size)
	loop, _ := strconv.Atoi(str_loop)
	sum := 0
	for i := 0; i < loop; i++ {
		sum += MultMatrix(size)
	}
	c.IndentedJSON(http.StatusOK, sum)

}

func fastcgo(c *gin.Context) {
	str_size := c.Param("size")
	str_loop := c.Param("loop")
	size, _ := strconv.Atoi(str_size)
	loop, _ := strconv.Atoi(str_loop)
	sum := 0
	for i := 0; i < loop; i++ {
		sum += FastCMultMatrix(size)
	}
	c.IndentedJSON(http.StatusOK, sum)
}
