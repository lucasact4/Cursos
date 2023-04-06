// Faça um algoritmo que receba "N" números e mostre positivo, negativo ou zero para cada número.

package MyFirstProject;

import java.util.Scanner;

public class EstruturaRepeticao {
	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);
		char desejaContinuar = 'S';
		while(desejaContinuar == 'S') {
			System.out.print("Digite um número: ");
			int numero = leitor.nextInt();
			if (numero == 0) {
				System.out.println("O número é zero");
			} else {
				if(numero > 0) {
					System.out.println("O número é maior que zero");
				} else {
					System.out.println("O número é menor que zero");
				}
			}
			while(true) {
				System.out.print("Deseja continuar? [S/N]");
				// desejaContinuar = leitor.next().charAt(0);
				// .toUpperCase();
				desejaContinuar = leitor.next().toUpperCase().charAt(0);
				if(desejaContinuar != 'S' && desejaContinuar != 'N') {
					System.out.println("Opção não reconhecida, tente novamente!");
					continue;
				} else {
					break;
				}
			}
			if(desejaContinuar == 'S') {
				System.out.println("Continuando...");
				continue;
			} else {
				System.out.println("Parando...");
				break;
			}
		}
	}
}
