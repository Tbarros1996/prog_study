/*  

Programa que imprime o resto de uma divisão no C++

Programador: Thiago Barros

*/

#include <iostream> //Importando a bibloteca padrão para Input Output

int main(){ //Definindo a função para a operação

using namespace std;

//Declarando as Variaveis

int valor_1,valor_2,resto;
valor_1 = 10;
valor_2 = 20;
resto = valor_1%valor_2; // Operador de Resto de Divisão
cout << resto;
return 0;


}