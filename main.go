package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	router := gin.Default()

	router.GET("/test/:id", getAlbumByID)

	router.Run("localhost:8080")
}

func getAlbumByID(c *gin.Context) {
	id := c.Param("id")

	if true {
		c.IndentedJSON(http.StatusOK, "-----------------------------------------"+id)
		return
	}

	c.IndentedJSON(http.StatusNotFound, gin.H{"message": "album not found"})
}
