package main 

import (
	"fmt"
	"time"
)

func trabalho (nome string ){

	fmt.Printf("Trabalho %s começou\n", nome)
	time.Sleep(2 * time.Second)
	fmt.Printf("Trabalho %s terminou\n", nome)
}

func main() {
	go trabalho("Go Routine1") 
	go trabalho("Go Routine2")
	go trabalho("Go Routine3")
	go trabalho("Go Routine4")
	go trabalho("Go Routine5")
	time.Sleep(3 * time.Second)
	fmt.Println("Fim")
}