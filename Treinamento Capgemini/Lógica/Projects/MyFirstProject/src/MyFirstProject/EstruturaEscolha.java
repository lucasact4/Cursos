package MyFirstProject;

public class EstruturaEscolha {
	public static void main(String[] args) {
		int codigoProduto = 2;
		
		switch(codigoProduto) {
		case 1:
			System.out.println("Bolo!");
			break;
		case 2:
			System.out.println("Açucar!");
			break;
		default:
			System.out.println("Sem Produtos!");
			break;
		}
		
	}
}
