iniciar-programa

define-nueva-instruccion gira como inicio
    mientras frente-bloqueado hacer inicio
        gira-izquierda;
    fin;
fin;


define-nueva-instruccion ajuste como inicio
    si derecha-libre entonces inicio
        repetir 3 veces  inicio
          gira-izquierda;
        fin;
        avanza;
        si derecha-libre entonces inicio
            repetir 3 veces inicio
              gira-izquierda;
            fin;
            avanza;
        fin;
    fin;
fin;


    inicia-ejecucion
       mientras no-junto-a-zumbador hacer inicio
            gira;
            avanza;
            ajuste;
       fin;
        apagate;
    termina-ejecucion
finalizar-programa