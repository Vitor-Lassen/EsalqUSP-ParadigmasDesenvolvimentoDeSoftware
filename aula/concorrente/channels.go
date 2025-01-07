package main 

import (
	"fmt"
	"time"
)

func enviarMensagem (canal chan string, mensagem string, delay time.Duration){
	time.Sleep(delay)
	canal <- mensagem
}

func main(){
	canal1 := make(chan string)
	canal2 := make(chan string)

	go enviarMensagem(canal1, "Mensagem canal 1 ", 2 * time.Second)
	go enviarMensagem(canal2, "Mensagem canal 2 ", 1 * time.Second)

	for i :=0; i<2;i++{
		select {
			case mensagemCanal1 := <- canal1:
				fmt.Println(mensagemCanal1)
			case mensagemCanal2 := <- canal2:
				fmt.Println(mensagemCanal2)
		}
	}
}