// Programa de Impressao de Uma Soma entre dois números
// Programa Desenvolvido por Thiago Barros

// Não se equecer do ponto e vírgula no final dos comandos

#include <iostream> // Inclusão da bibloteca iostream para podermos imprimir os valores da soma

int main(){

using namespace std; //Uso da namespace padrão para evidar conflitos de nomes

/* Definição das Variáveis */

// lembrando = comando cout é para IMPRIMIR A INFORMAÇÃO EM TELA
// endl = É PARA PULAR UMA LINHA
// cout(imprima na tela)<<variavel<<endl(pule uma linha)

int numero_1;
int numero_2;
int soma_dos_numeros;
numero_1 = 1;
numero_2 = 2;
cout<<numero_1<<endl;
cout<<numero_2<<endl;
soma_dos_numeros = numero_1 + numero_2;
cout<<soma_dos_numeros<<endl;
return 0;
}