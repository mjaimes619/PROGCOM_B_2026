/******************************************************************************

edad=int(input("Ingresa tu edad: "))

if edad>=18:
  print("Eres mayor de edad")
else:
  print("NO eres mayor de edad")

*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		System.out.println("Ingresa tu edad: "); //Impresion
		Scanner edad = new Scanner(System.in); //Creacion de input
		//Nextline sirve para leer string
		//nextInt lee enteros
		//nextFloat lee flotantes
		//nextBoolean lee boleanos
		int age = edad.nextInt();
		
		if (age>=18){
		    System.out.println("Eres mayor de edad");
		}else{
		    System.out.println("NO eres mayor de edad");
		}
		
		
		
        if (age<10){
	             System.out.println("Eres un niño");
	         }else{
	          if (age >= 10 && age < 14){   
	                System.out.println("Eres un preadolescente");
	          }else{
	          if (age >= 14 && age < 18){
	                System.out.println("Eres un adolesecente");
             }else{
             if (age >= 18 && age < 30){
                 System.out.println("Eres un adulto joven");
              }else{
                  System.out.println("Eres un adulto");
                  
                  
        if (age<10){
	             System.out.println("Eres un niño");
	         }else if (age >= 10 && age < 14){   
	                System.out.println("Eres un preadolescente");
	          }else if (age >= 14 && age < 18){
	                System.out.println("Eres un adolesecente");
             }else if (age >= 18 && age < 30){
                 System.out.println("Eres un adulto joven");
              }else{
                  System.out.println("Eres un adulto");
              }
            }
	      }
	    }
	  }
   }
}