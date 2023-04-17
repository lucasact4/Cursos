package Classes;

import java.util.Scanner;

public class Estruturado {
	public static void main(String[] args) {
		
		float peso;
		float altura;
		float imc;
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.println("Digite o peso da pessoa");
		peso = leitor.nextFloat();
		System.out.println("Digite a altura da pessoa");
		altura = leitor.nextFloat();
		
		imc = peso / (altura * altura);
		
		System.out.println("IMC = " + imc);
	}
}
