// A concessionária de veículos "Carango Velho" está vendendo os seus veículos com desconto.
// Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros.
// O desconto deverá ser calculado de acordo com o ano do veículo.
// Até 2000 -12% e acima de 2000 -7%.
// O sistema deverá perguntar se deseja continuar calculando o desconto até que a resposta seja:
// "(N) Não". Informar total de carros com ano até 2000 e o total geral;

package MyFirstProject;

import java.util.Scanner;

public class Exercicio20 {
	public static void main(String[] args) {
		
		int anoFabricacao, totalCarros = 0, totalCarrosSemiNovos = 0;
		float valorVeiculo, porcentagemDesconto, valorDesconto, valorPagar = 0.0f;
		boolean desejaRepetir = true;
		char escolha;
		Scanner leitor = new Scanner(System.in);
		
		while (desejaRepetir == true) {
			
			System.out.print("Digite o ano de fabricação do veículo: ");
			anoFabricacao = leitor.nextInt();
			
			System.out.print("Digite o valor do do veículo: ");
			valorVeiculo = leitor.nextFloat();
			
			if(anoFabricacao <= 2000) {
				porcentagemDesconto = 0.12f;
			} else {
				porcentagemDesconto = 0.07f;
				totalCarrosSemiNovos++;
			}
			totalCarros++;
			
			valorDesconto = valorVeiculo * porcentagemDesconto;
			valorPagar = valorVeiculo - valorDesconto;

			System.out.println("O valor do desconto foi de: " + valorDesconto);
			System.out.println("O valor que deve ser pago é: " + valorPagar);
			
			System.out.print("Deseja fazer mais cadastros? S - [Sim / N - Não]");
			escolha = leitor.next().toUpperCase().charAt(0);
			while (escolha != 'S' && escolha != 'N') {
				System.out.println("Escolha não reconhecida...");
				System.out.print("Deseja fazer mais cadastros? S - [Sim / N - Não]");
				escolha = leitor.next().toUpperCase().charAt(0);
			}
			if (escolha == 'S') {
				System.out.println("Continuando...");
				continue;
			} else {
				System.out.println("Parando...");
				desejaRepetir = false;
			}
			
		}

		System.out.println("Total de carros semi novos: " + totalCarrosSemiNovos);
		System.out.println("Total de carros: " + totalCarros);
		
	}
}
