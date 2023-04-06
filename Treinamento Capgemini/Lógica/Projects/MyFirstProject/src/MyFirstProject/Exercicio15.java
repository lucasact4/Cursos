// Faça um algoritmo que receba um número e diga se este número está no intervalo entre 100 e 200.

package MyFirstProject;

import java.util.Scanner;

public class Exercicio15 {
	public static void main(String[] args) {
		int numero;
		Scanner leitor = new Scanner(System.in);
		System.out.print("Digite um número: ");
		numero = leitor.nextInt();
		if(numero >= 100 && numero <= 200) {
			System.out.println("Está no intervalo entre 100 e 200");
		} else {
			System.out.println("Não está no intervalo entre 100 e 200");
		}
	}
}
