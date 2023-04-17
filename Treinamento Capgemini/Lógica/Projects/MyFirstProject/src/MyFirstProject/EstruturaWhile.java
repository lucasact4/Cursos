package MyFirstProject;

import java.util.Scanner;

public class EstruturaWhile {
	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);
		int totalAlunos = 1;
		while (totalAlunos <= 10) {
			System.out.println("Cadastro N " + totalAlunos + "º");
			System.out.print("Nome: ");
			String nomeAluno = leitor.next();
			System.out.print("Idade: ");
			int idadeAluno = leitor.nextInt();
			System.out.println("O nome do aluno é " + nomeAluno + " e sua idade é " + idadeAluno);
			totalAlunos++;
		}
	}
}
