#include <iostream>
#include <cmath>
using namespace std;

int main(){

             float a, b, c, delta, x1, x2;
             
             cout << "Considere a lei de formação 'ax² + bx + c = 0' para equações do 2° grau\n";

             cout << "Informe o valor do coeficiente a:  ";
             cin >> a;
             cout << "Informe o valor do coeficiente b:  ";
             cin >> b;
             cout << "Informe o valor do coeficiente c:  ";
             cin >> c;

             delta=(b*b)-4*a*c;
             
             cout << "delta = " << delta << "\n";

             if (delta < 0){

                 cout << "Putz, o discriminante (delta) é negativo... a equação não possui raízes reais =/ \n";

             }else if (delta > 0) {
                 
                 x1=((-b)+sqrt(delta))/(2*a);
             
                 x2=((-b)-sqrt(delta))/(2*a);
             
                 cout << "As raizes são: ";
                 cout <<"x1 = " << x1 << " e x2 = " << x2 << "\n";

             }else{ //para o caso delta = 0, raiz será única
              
                 x1 = -b/2;
                 cout << "A raiz única é: ";
                 cout <<"x = " << x1 << "\n";

             }

}
