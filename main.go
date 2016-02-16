package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Inside handler")
	fmt.Fprintf(w, "Hello world")
}

func main() {
	http.HandleFunc("/", handler)

	http.ListenAndServe("localhost:9999", nil)
}
