package main;

import java.sql.SQLException;
import java.util.List;
import controller.ProjectController;
import model.Project;

public class Main {
	public static void main(String[] args) {
		
//		ProjectController projectController = new ProjectController();
//		
//		Project project = new Project();
//		project.setName("Projeto teste");
//		project.setDescription("descricao");
//		projectController.save(project);
		
		ProjectController projectController = new ProjectController();
		
		Project project = new Project();
		project.setId(10);
		project.setName("Novo nome do projeto");
		project.setDescription("descricao");
		
		projectController.update(project);
		
		List<Project> projects = projectController.getAll();
		System.out.print("Total de projetos = " + projects.size());
		
		projectController.removeById(10);
		
	}
}
