package MyFirstProject;

import java.util.Scanner;

public class ComandosLeituraGravacao {
	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);
		System.out.print("Idade: ");
		int idade = leitor.nextInt();
		System.out.print("CotaçãoDollar: ");
		float cotacaoDolar = leitor.nextFloat();
		System.out.print("CotaçãoEuro: ");
		double cotacaoEuro = leitor.nextDouble();
		System.out.print("CEP: ");
		String codigoRua = leitor.next();
		System.out.print("Nome: ");
		String nome = leitor.next();

		System.out.println("Texto que será exibido no console");
		System.out.print("Texto que será exibido no console");
	}
}
