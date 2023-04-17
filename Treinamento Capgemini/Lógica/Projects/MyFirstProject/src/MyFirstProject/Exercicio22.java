// Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos.
// Mostre como resultado se houver lucro, prejuízo ou empate para cada produto.
// Informe o valor de custo de cada produto, o valor de venda de cada produto,
// a média de preço de custo e do preço de venda.

package MyFirstProject;

import java.util.Scanner;

public class Exercicio22 {
	public static void main(String[] args) {
		String nomeProduto;
		float precoCusto = 0.0f;
		float precoVenda = 0.0f;
		float totalCusto = 0.0f;
		float totalVenda = 0.0f;
		int i = 0;
		
		Scanner leitor = new Scanner(System.in);

		for(; i < 40; i++) {
			System.out.print("Digite o nome do produto: ");
			nomeProduto = leitor.next();
			System.out.print("Digite o preço de custo do produto: ");
			precoCusto = leitor.nextFloat();
			System.out.print("Digite o preço de venda do produto: ");
			precoVenda = leitor.nextFloat();
			
			totalCusto += precoCusto;
			totalVenda += precoVenda;
			
			if(precoCusto == precoVenda) {
				System.out.println("Houve um EMPATE!\nO preço entre custo e venda são iguais!");
			} else {
				if(precoCusto > precoVenda) {
					System.out.println("Houve um Prejuízo!\nOpreço de custo foi maior do que o de venda!");
				} else {
					System.out.println("Houve um Lucro!\nO preço de venda foi maior do que o de custo!");
				}
			}
			System.out.println(nomeProduto + ", preço de custo = " + precoCusto + ", preço de venda = " + precoVenda);
		}
		System.out.println("A média do preço de custo é de: " + (totalCusto/i));
		System.out.println("A média do preço de venda é de: " + (totalVenda/i));
	}
}
