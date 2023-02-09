// Faça um algoritmo que receba "N" números e mostre positivo, negativo ou zero para cada número.

package MyFirstProject;

import java.util.Scanner;

public class Exercicio24 {
	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);
		String desejaContinuar = "S";
		while(desejaContinuar.equalsIgnoreCase("S")) {
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
				desejaContinuar = leitor.next();
				if(!desejaContinuar.equalsIgnoreCase("S") && !desejaContinuar.equalsIgnoreCase("N")) {
					System.out.println("Opção não reconhecida, tente novamente!");
					continue;
				} else {
					break;
				}
			}
			if(desejaContinuar.equalsIgnoreCase("S")) {
				System.out.println("Continuando...");
				continue;
			} else {
				System.out.println("Parando...");
				break;
			}
		}
	}
}
