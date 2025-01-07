import styles from "../styles/Home.module.css"; // Importa os estilos CSS
import { useState , useEffect} from "react"; // Importa o hook useState

function ContadorComMensagem() {
  const [contador, setContador] = useState(0); // Inicializa o estado contador com o valor 0

  useEffect(() => {
    console.log(`O contador mudou para: ${contador}`);
  },[contador]);


  const incrementar = () => {
    setContador(contador + 1); // Função que incrementa o contador
    console.log(contador);
  };
  
  return (
  <main className={styles.main}>
    <p className={styles.aula}>Você clicou {contador}</p>
    <button onClick={incrementar} className={styles.button}>
      Clique aqui</button>
  </main>);
}

export default ContadorComMensagem;
