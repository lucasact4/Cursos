package MyFirstProject;

public class EstruturaCondicionalSe {
	public static void main(String[] args) {
		int media = 7;
		
		/*
			= Recebe
			> Maior
			>= Maior ou Igual
			< Menor
			<= Menor ou Igual
			== Igual
			/! Diferente
		*/
		
		/*
			&& Operador E | AND
			|| Operador OU | OR
			! Operador NÃO | NO
		*/
		
		if (media >= 7) {
			System.out.println("Aprovado!");
			if (media == 10) {
				System.out.println("Parabéns com nota MÁXIMA!");
			} else {
				System.out.println("Parabéns!");
			}
		} else {
			System.out.println("Reprovado!");
		}
	}
}
