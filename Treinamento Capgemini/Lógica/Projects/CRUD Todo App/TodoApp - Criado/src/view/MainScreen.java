package view;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.GroupLayout;
import javax.swing.GroupLayout.Alignment;
import java.awt.Color;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.LayoutStyle.ComponentPlacement;
import javax.swing.ImageIcon;
import javax.swing.border.EtchedBorder;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.SwingConstants;
import javax.swing.UIManager;

import java.awt.Dimension;
import javax.swing.ListSelectionModel;
import javax.swing.JScrollPane;
import javax.swing.AbstractListModel;
import javax.swing.DefaultListModel;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

import controller.ProjectController;
import controller.TaskController;
import model.Project;
import model.Task;
import util.ButtonColumnCellRenderer;
import util.DeadlineColumnCellRenderer;
import util.TaskTableModel;

import javax.swing.UIManager.LookAndFeelInfo;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.List;
import javax.swing.JLayeredPane;
import java.awt.FlowLayout;
import java.awt.BorderLayout;

public class MainScreen extends JFrame {
	private JPanel panel_5;
	private JList ListProjects;
	private JTable TableTasks;
	private JScrollPane ScrollPaneTasks;
	private JPanel PanelEmptyList;

	/**
	 * Launch the application.
	 */
	
	ProjectController projectController;
	TaskController taskController;
	
	DefaultListModel projectsModel;
	TaskTableModel taskModel;
	
	public static void main(String[] args) {
		try {
			
			//Criando o LookAndFeel para poder modificar o template da aplicação
			//Templates disponiveis:
			//Metal, Nimbus, CDE/Motifi, Windows, Windows Classic, Java Swing
			for(LookAndFeelInfo info:UIManager.getInstalledLookAndFeels()) {
				if("Java Swing".equals(info.getName())) {
					UIManager.setLookAndFeel(info.getClassName());
					break;
				}
			}
		} catch (Exception e) {
			throw new RuntimeException("Erro ao salvar a tarefa "
					+ e.getMessage(), e);
		}
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MainScreen frame = new MainScreen();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MainScreen() {
		setMinimumSize(new Dimension(600, 700));
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(250, 250, 1125, 750);
		
		JPanel App = new JPanel();
		GroupLayout groupLayout = new GroupLayout(getContentPane());
		groupLayout.setHorizontalGroup(
			groupLayout.createParallelGroup(Alignment.LEADING)
				.addComponent(App, GroupLayout.DEFAULT_SIZE, 1109, Short.MAX_VALUE)
		);
		groupLayout.setVerticalGroup(
			groupLayout.createParallelGroup(Alignment.LEADING)
				.addComponent(App, GroupLayout.DEFAULT_SIZE, 711, Short.MAX_VALUE)
		);
		
		JPanel PanelToolBar = new JPanel();
		PanelToolBar.setBackground(new Color(0, 153, 102));
		
		JLabel LabelToolBarSubTitle = new JLabel("Anote tudo, não esqueça de nada");
		LabelToolBarSubTitle.setForeground(Color.WHITE);
		LabelToolBarSubTitle.setFont(new Font("Segoe UI", Font.PLAIN, 14));
		
		JLabel LabelToolBarTitle = new JLabel("Todo App");
		LabelToolBarTitle.setIcon(new ImageIcon("C:\\Users\\funcr\\eclipse-workspace\\TodoApp\\resources\\tick.png"));
		LabelToolBarTitle.setForeground(Color.WHITE);
		LabelToolBarTitle.setFont(new Font("Segoe UI", Font.BOLD, 36));
		GroupLayout gl_PanelToolBar = new GroupLayout(PanelToolBar);
		gl_PanelToolBar.setHorizontalGroup(
			gl_PanelToolBar.createParallelGroup(Alignment.LEADING)
				.addGap(0, 1109, Short.MAX_VALUE)
				.addGroup(gl_PanelToolBar.createSequentialGroup()
					.addGap(21)
					.addGroup(gl_PanelToolBar.createParallelGroup(Alignment.LEADING)
						.addComponent(LabelToolBarSubTitle, GroupLayout.PREFERRED_SIZE, 281, GroupLayout.PREFERRED_SIZE)
						.addComponent(LabelToolBarTitle, GroupLayout.PREFERRED_SIZE, 318, GroupLayout.PREFERRED_SIZE))
					.addContainerGap(770, Short.MAX_VALUE))
		);
		gl_PanelToolBar.setVerticalGroup(
			gl_PanelToolBar.createParallelGroup(Alignment.LEADING)
				.addGap(0, 175, Short.MAX_VALUE)
				.addGroup(gl_PanelToolBar.createSequentialGroup()
					.addGap(40)
					.addComponent(LabelToolBarTitle, GroupLayout.PREFERRED_SIZE, 75, GroupLayout.PREFERRED_SIZE)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(LabelToolBarSubTitle, GroupLayout.PREFERRED_SIZE, 30, GroupLayout.PREFERRED_SIZE)
					.addContainerGap(24, Short.MAX_VALUE))
		);
		PanelToolBar.setLayout(gl_PanelToolBar);
		
		JPanel PanelProjects = new JPanel();
		PanelProjects.setBorder(new EtchedBorder(EtchedBorder.LOWERED, null, null));
		PanelProjects.setBackground(new Color(255, 255, 255));
		
		JPanel PanelTasks = new JPanel();
		PanelTasks.setBorder(new EtchedBorder(EtchedBorder.LOWERED, null, null));
		PanelTasks.setBackground(new Color(255, 255, 255));
		
		JPanel PanelProjectList = new JPanel();
		PanelProjectList.setBorder(new EtchedBorder(EtchedBorder.LOWERED, null, null));
		PanelProjectList.setBackground(new Color(255, 255, 255));
		
		panel_5 = new JPanel();
		panel_5.setBackground(new Color(255, 255, 255));
		GroupLayout gl_App = new GroupLayout(App);
		gl_App.setHorizontalGroup(
			gl_App.createParallelGroup(Alignment.LEADING)
				.addComponent(PanelToolBar, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
				.addGroup(gl_App.createSequentialGroup()
					.addContainerGap()
					.addGroup(gl_App.createParallelGroup(Alignment.LEADING, false)
						.addComponent(PanelProjects, 0, 0, Short.MAX_VALUE)
						.addComponent(PanelProjectList, GroupLayout.DEFAULT_SIZE, 228, Short.MAX_VALUE))
					.addPreferredGap(ComponentPlacement.RELATED)
					.addGroup(gl_App.createParallelGroup(Alignment.TRAILING)
						.addComponent(panel_5, GroupLayout.DEFAULT_SIZE, 855, Short.MAX_VALUE)
						.addComponent(PanelTasks, GroupLayout.DEFAULT_SIZE, 855, Short.MAX_VALUE))
					.addContainerGap())
		);
		gl_App.setVerticalGroup(
			gl_App.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_App.createSequentialGroup()
					.addComponent(PanelToolBar, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addGroup(gl_App.createParallelGroup(Alignment.LEADING)
						.addComponent(PanelTasks, GroupLayout.DEFAULT_SIZE, 100, Short.MAX_VALUE)
						.addComponent(PanelProjects, GroupLayout.DEFAULT_SIZE, 100, Short.MAX_VALUE))
					.addPreferredGap(ComponentPlacement.RELATED)
					.addGroup(gl_App.createParallelGroup(Alignment.LEADING)
						.addComponent(panel_5, GroupLayout.DEFAULT_SIZE, 413, Short.MAX_VALUE)
						.addComponent(PanelProjectList, GroupLayout.PREFERRED_SIZE, 413, GroupLayout.PREFERRED_SIZE))
					.addContainerGap())
		);
		
		PanelEmptyList = new JPanel();
		PanelEmptyList.setBorder(new EtchedBorder(EtchedBorder.LOWERED, new Color(228, 228, 228), null));
		PanelEmptyList.setBackground(Color.WHITE);
		
		JLabel LabelEmptyListSubTitle = new JLabel("Clique no botão \"+\" para adicionar uma nova tarefa!");
		LabelEmptyListSubTitle.setHorizontalAlignment(SwingConstants.CENTER);
		LabelEmptyListSubTitle.setForeground(new Color(153, 153, 153));
		LabelEmptyListSubTitle.setFont(new Font("Segoe UI", Font.BOLD, 12));
		
		JLabel LabelEmptyListTitle = new JLabel("Nenhuma Tarefa por aqui! :D");
		LabelEmptyListTitle.setHorizontalAlignment(SwingConstants.CENTER);
		LabelEmptyListTitle.setForeground(new Color(0, 153, 102));
		LabelEmptyListTitle.setFont(new Font("Segoe UI", Font.BOLD, 14));
		
		JLabel LabelEmptyListTitle_1 = new JLabel("");
		LabelEmptyListTitle_1.setIcon(new ImageIcon("C:\\Users\\funcr\\eclipse-workspace\\TodoApp\\resources\\lists.png"));
		LabelEmptyListTitle_1.setHorizontalAlignment(SwingConstants.CENTER);
		LabelEmptyListTitle_1.setForeground(new Color(0, 153, 102));
		LabelEmptyListTitle_1.setFont(new Font("Segoe UI", Font.BOLD, 14));
		
		ScrollPaneTasks = new JScrollPane();
		ScrollPaneTasks.setBorder(new EtchedBorder(EtchedBorder.LOWERED, null, null));
		
		TableTasks = new JTable();
		TableTasks.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int rowIndex = TableTasks.rowAtPoint(e.getPoint());
				int columnIndex = TableTasks.columnAtPoint(e.getPoint());
				Task task = taskModel.getTasks().get(rowIndex);
				
				switch(columnIndex) {
					case 3:
						taskController.update(task);
						break;
					case 5:
						taskController.removeById(task.getId());
						taskModel.getTasks().remove(task);
						int projectIndex = ListProjects.getSelectedIndex();
						Project project = (Project) projectsModel.get(projectIndex);
						loadTasks(project.getId());
						break;
				}
			}
		});
		TableTasks.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		TableTasks.setGridColor(new Color(255, 255, 255));
		TableTasks.setRowHeight(50);
		TableTasks.setShowVerticalLines(false);
		TableTasks.setSelectionBackground(new Color(204, 255, 204));
		ScrollPaneTasks.setViewportView(TableTasks);
		panel_5.setLayout(new BorderLayout(0, 0));
		GroupLayout gl_PanelEmptyList = new GroupLayout(PanelEmptyList);
		gl_PanelEmptyList.setHorizontalGroup(
			gl_PanelEmptyList.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_PanelEmptyList.createSequentialGroup()
					.addGap(10)
					.addGroup(gl_PanelEmptyList.createParallelGroup(Alignment.LEADING)
						.addComponent(LabelEmptyListTitle, GroupLayout.DEFAULT_SIZE, 811, Short.MAX_VALUE)
						.addComponent(LabelEmptyListTitle_1, GroupLayout.DEFAULT_SIZE, 811, Short.MAX_VALUE)
						.addComponent(LabelEmptyListSubTitle, GroupLayout.DEFAULT_SIZE, 811, Short.MAX_VALUE))
					.addGap(30))
		);
		gl_PanelEmptyList.setVerticalGroup(
			gl_PanelEmptyList.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_PanelEmptyList.createSequentialGroup()
					.addGap(76)
					.addGroup(gl_PanelEmptyList.createParallelGroup(Alignment.LEADING)
						.addGroup(gl_PanelEmptyList.createSequentialGroup()
							.addGap(139)
							.addComponent(LabelEmptyListTitle, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
						.addGroup(gl_PanelEmptyList.createSequentialGroup()
							.addComponent(LabelEmptyListTitle_1, GroupLayout.DEFAULT_SIZE, 140, Short.MAX_VALUE)
							.addGap(19)))
					.addGap(6)
					.addComponent(LabelEmptyListSubTitle, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
					.addGap(152))
		);
		PanelEmptyList.setLayout(gl_PanelEmptyList);
		panel_5.add(PanelEmptyList);
		panel_5.add(ScrollPaneTasks);
		
		JLabel LabelTasksTitle = new JLabel("Tarefas");
		LabelTasksTitle.setForeground(new Color(0, 153, 102));
		LabelTasksTitle.setFont(new Font("Segoe UI", Font.BOLD, 18));
		
		JLabel LabelTasksAdd = new JLabel("");
		LabelTasksAdd.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				TaskDialogScreen taskDialogScreen = new TaskDialogScreen();
				int projectIndex = ListProjects.getSelectedIndex();
				Project project = (Project) projectsModel.get(projectIndex);
				taskDialogScreen.setProject(project);
				taskDialogScreen.setVisible(true);
				taskDialogScreen.addWindowListener(new WindowAdapter() {
					public void windowClosed(WindowEvent ex) {
						int projectIndex = ListProjects.getSelectedIndex();
						Project project = (Project) projectsModel.get(projectIndex);
						loadTasks(project.getId());
					}
				});
			}
		});
		LabelTasksAdd.setIcon(new ImageIcon("C:\\Users\\funcr\\eclipse-workspace\\TodoApp\\resources\\add.png"));
		GroupLayout gl_PanelTasks = new GroupLayout(PanelTasks);
		gl_PanelTasks.setHorizontalGroup(
			gl_PanelTasks.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_PanelTasks.createSequentialGroup()
					.addGap(36)
					.addComponent(LabelTasksTitle, GroupLayout.PREFERRED_SIZE, 164, GroupLayout.PREFERRED_SIZE)
					.addPreferredGap(ComponentPlacement.RELATED, 593, Short.MAX_VALUE)
					.addComponent(LabelTasksAdd)
					.addGap(26))
		);
		gl_PanelTasks.setVerticalGroup(
			gl_PanelTasks.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_PanelTasks.createSequentialGroup()
					.addContainerGap()
					.addGroup(gl_PanelTasks.createParallelGroup(Alignment.LEADING)
						.addGroup(gl_PanelTasks.createSequentialGroup()
							.addComponent(LabelTasksTitle, GroupLayout.DEFAULT_SIZE, 74, Short.MAX_VALUE)
							.addContainerGap())
						.addGroup(Alignment.TRAILING, gl_PanelTasks.createSequentialGroup()
							.addComponent(LabelTasksAdd)
							.addGap(31))))
		);
		PanelTasks.setLayout(gl_PanelTasks);
		
		JScrollPane ScrollPaneProjects = new JScrollPane();
		ScrollPaneProjects.setBorder(new EtchedBorder(EtchedBorder.LOWERED, new Color(228, 228, 228), null));
		GroupLayout gl_PanelProjectList = new GroupLayout(PanelProjectList);
		gl_PanelProjectList.setHorizontalGroup(
			gl_PanelProjectList.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_PanelProjectList.createSequentialGroup()
					.addContainerGap()
					.addComponent(ScrollPaneProjects, GroupLayout.DEFAULT_SIZE, 204, Short.MAX_VALUE)
					.addContainerGap())
		);
		gl_PanelProjectList.setVerticalGroup(
			gl_PanelProjectList.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_PanelProjectList.createSequentialGroup()
					.addGap(13)
					.addComponent(ScrollPaneProjects, GroupLayout.DEFAULT_SIZE, 385, Short.MAX_VALUE)
					.addContainerGap())
		);
		
		ListProjects = new JList();
		ListProjects.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int projectIndex = ListProjects.getSelectedIndex();
				Project project = (Project) projectsModel.get(projectIndex);
				loadTasks(project.getId());
			}
		});
		ListProjects.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		ListProjects.setSelectionBackground(new Color(0, 153, 102));
		ListProjects.setFont(new Font("Segoe UI", Font.BOLD, 16));
		ListProjects.setFixedCellHeight(50);
		ScrollPaneProjects.setColumnHeaderView(ListProjects);
		PanelProjectList.setLayout(gl_PanelProjectList);
		
		JLabel LabelProjectsTitle = new JLabel("Projetos");
		LabelProjectsTitle.setForeground(new Color(0, 153, 102));
		LabelProjectsTitle.setFont(new Font("Segoe UI", Font.BOLD, 18));
		
		JLabel LabelProjectsAdd = new JLabel("");
		LabelProjectsAdd.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ProjectDialogScreen projectDialogScreen = new ProjectDialogScreen();
				projectDialogScreen.setVisible(true);
				
				projectDialogScreen.addWindowListener(new WindowAdapter() {
					public void windowClosed(WindowEvent e) {
						loadProject();
					}
				});
			}
		});
		LabelProjectsAdd.setIcon(new ImageIcon("C:\\Users\\funcr\\eclipse-workspace\\TodoApp\\resources\\add.png"));
		GroupLayout gl_PanelProjects = new GroupLayout(PanelProjects);
		gl_PanelProjects.setHorizontalGroup(
			gl_PanelProjects.createParallelGroup(Alignment.LEADING)
				.addGroup(Alignment.TRAILING, gl_PanelProjects.createSequentialGroup()
					.addContainerGap(34, Short.MAX_VALUE)
					.addComponent(LabelProjectsTitle, GroupLayout.PREFERRED_SIZE, 106, GroupLayout.PREFERRED_SIZE)
					.addGap(18)
					.addComponent(LabelProjectsAdd)
					.addGap(34))
		);
		gl_PanelProjects.setVerticalGroup(
			gl_PanelProjects.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_PanelProjects.createSequentialGroup()
					.addContainerGap()
					.addGroup(gl_PanelProjects.createParallelGroup(Alignment.LEADING)
						.addGroup(gl_PanelProjects.createSequentialGroup()
							.addComponent(LabelProjectsTitle, GroupLayout.DEFAULT_SIZE, 74, Short.MAX_VALUE)
							.addContainerGap())
						.addGroup(Alignment.TRAILING, gl_PanelProjects.createSequentialGroup()
							.addComponent(LabelProjectsAdd)
							.addGap(29))))
		);
		PanelProjects.setLayout(gl_PanelProjects);
		App.setLayout(gl_App);
		getContentPane().setLayout(groupLayout);
		initDataController();
		initComponentsModel();
		decorateTableTask();
	}
	
	public void decorateTableTask() {
		
		//Customizando o header da table de tarefas
		TableTasks.getTableHeader().setFont(new Font("Segoe UI", Font.BOLD, 14));
        TableTasks.getTableHeader().setOpaque(false);
		TableTasks.getTableHeader().setBackground(new Color(0, 153, 102));
		TableTasks.getTableHeader().setForeground(new Color(255, 255, 255));
		
		//Criando um sort automático para as colunas da table
		//TableTasks.setAutoCreateRowSorter(true);
		TableTasks.getColumnModel().getColumn(2).setCellRenderer(new DeadlineColumnCellRenderer());
		TableTasks.getColumnModel().getColumn(4).setCellRenderer(new ButtonColumnCellRenderer("edit"));
		TableTasks.getColumnModel().getColumn(5).setCellRenderer(new ButtonColumnCellRenderer("delete"));
	
	}
	
	public void initDataController() {
		projectController = new ProjectController();
		taskController = new TaskController();
	}
	
	public void initComponentsModel() {
		projectsModel = new DefaultListModel();
		loadProject();
		
		taskModel = new TaskTableModel();
		TableTasks.setModel(taskModel);
		
		if (!projectsModel.isEmpty()) {
            ListProjects.setSelectedIndex(0);
            int projectIndex = ListProjects.getSelectedIndex();
            Project project = (Project) projectsModel.get(projectIndex);
            loadTasks(project.getId());
        }
	}
	
	public void loadTasks(int idProject) {
		List<Task> tasks = taskController.getAll(idProject);
		taskModel.setTasks(tasks);
		showJTableTasks(!tasks.isEmpty());
	}
	private void showJTableTasks(boolean hasTasks) {
		if (hasTasks) {
			//Existem tarefas
			
			if (PanelEmptyList.isVisible()) {
				PanelEmptyList.setVisible(false);
				panel_5.remove(PanelEmptyList);
			}
			
			panel_5.add(ScrollPaneTasks);
			ScrollPaneTasks.setVisible(true);
			ScrollPaneTasks.setSize(panel_5.getWidth(), panel_5.getHeight());
		} else {
			if (ScrollPaneTasks.isVisible()) {
				ScrollPaneTasks.setVisible(false);
				panel_5.remove(ScrollPaneTasks);
			}
			
			panel_5.add(PanelEmptyList);
			PanelEmptyList.setVisible(true);
			PanelEmptyList.setSize(panel_5.getWidth(), panel_5.getHeight());
		}
	}
	public void loadProject() {
		List<Project> projects = projectController.getAll();
		projectsModel.clear();
		for (int i = 0; i < projects.size(); i++) {
			Project project = projects.get(i);
			projectsModel.addElement(project);
		}
		ListProjects.setModel(projectsModel);
	}
}
