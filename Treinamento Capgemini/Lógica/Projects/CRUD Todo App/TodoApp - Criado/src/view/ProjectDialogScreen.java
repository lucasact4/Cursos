package view;

import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.GroupLayout;
import javax.swing.GroupLayout.Alignment;
import java.awt.Color;
import javax.swing.LayoutStyle.ComponentPlacement;
import javax.swing.UIManager.LookAndFeelInfo;
import javax.swing.border.EtchedBorder;

import controller.ProjectController;
import model.Project;

import javax.swing.JLabel;
import javax.swing.JOptionPane;

import java.awt.Font;
import java.awt.event.MouseAdapter;

import javax.swing.ImageIcon;
import javax.swing.SwingConstants;
import javax.swing.UIManager;
import javax.swing.JTextField;
import javax.swing.JTextArea;
import java.awt.Dimension;
import java.awt.event.MouseEvent;
import javax.swing.JScrollPane;

public class ProjectDialogScreen extends JDialog {
	private JTextField TextFieldName;
	
	ProjectController controller;

	/**
	 * Launch the application.
	 */
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
			throw new RuntimeException("Erro ao salvar modelo de terminal "
					+ e.getMessage(), e);
		}
		try {
			ProjectDialogScreen dialog = new ProjectDialogScreen();
			dialog.setDefaultCloseOperation(
					JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Create the dialog.
	 * @param rootPaneCheckingEnabled 
	 * @param mouseAdapter 
	 */
	public ProjectDialogScreen() {
		setMinimumSize(new Dimension(250, 400));
		setBounds(125, 125, 375, 425);
		JPanel PanelToolBar = new JPanel();
		PanelToolBar.setBackground(new Color(0, 153, 102));
		
		JPanel PanelProject = new JPanel();
		PanelProject.setBorder(new EtchedBorder(EtchedBorder.LOWERED, null, null));
		PanelProject.setBackground(new Color(255, 255, 255));
		GroupLayout groupLayout = new GroupLayout(getContentPane());
		groupLayout.setHorizontalGroup(
			groupLayout.createParallelGroup(Alignment.LEADING)
				.addComponent(PanelToolBar, GroupLayout.DEFAULT_SIZE, 359, Short.MAX_VALUE)
				.addGroup(groupLayout.createSequentialGroup()
					.addGap(10)
					.addComponent(PanelProject, GroupLayout.DEFAULT_SIZE, 339, Short.MAX_VALUE)
					.addGap(10))
		);
		groupLayout.setVerticalGroup(
			groupLayout.createParallelGroup(Alignment.LEADING)
				.addGroup(groupLayout.createSequentialGroup()
					.addComponent(PanelToolBar, GroupLayout.PREFERRED_SIZE, 66, GroupLayout.PREFERRED_SIZE)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(PanelProject, GroupLayout.DEFAULT_SIZE, 303, Short.MAX_VALUE)
					.addContainerGap())
		);
		
		JLabel LabelName = new JLabel("Nome");
		LabelName.setFont(new Font("Segoe UI", Font.PLAIN, 14));
		
		TextFieldName = new JTextField();
		TextFieldName.setFont(new Font("Segoe UI", Font.PLAIN, 14));
		TextFieldName.setBorder(new EtchedBorder(EtchedBorder.LOWERED, null, null));
		TextFieldName.setColumns(10);
		
		JLabel LabelDescription = new JLabel("Descrição");
		LabelDescription.setFont(new Font("Segoe UI", Font.PLAIN, 14));
		
		JScrollPane ScrollPane = new JScrollPane();
		ScrollPane.setBorder(new EtchedBorder(EtchedBorder.LOWERED, null, null));
		GroupLayout gl_PanelProject = new GroupLayout(PanelProject);
		gl_PanelProject.setHorizontalGroup(
			gl_PanelProject.createParallelGroup(Alignment.TRAILING)
				.addGroup(gl_PanelProject.createSequentialGroup()
					.addContainerGap()
					.addGroup(gl_PanelProject.createParallelGroup(Alignment.TRAILING)
						.addComponent(ScrollPane, Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 315, Short.MAX_VALUE)
						.addComponent(TextFieldName, Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 315, Short.MAX_VALUE)
						.addComponent(LabelName, Alignment.LEADING)
						.addComponent(LabelDescription, Alignment.LEADING))
					.addContainerGap())
		);
		gl_PanelProject.setVerticalGroup(
			gl_PanelProject.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_PanelProject.createSequentialGroup()
					.addContainerGap()
					.addComponent(LabelName)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(TextFieldName, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
					.addGap(18)
					.addComponent(LabelDescription)
					.addGap(8)
					.addComponent(ScrollPane, GroupLayout.DEFAULT_SIZE, 181, Short.MAX_VALUE)
					.addContainerGap())
		);
		
		JTextArea TextAreaDescription = new JTextArea();
		TextAreaDescription.setFont(new Font("Segoe UI", Font.PLAIN, 14));
		ScrollPane.setViewportView(TextAreaDescription);
		PanelProject.setLayout(gl_PanelProject);
		
		JLabel LabelToolTitle = new JLabel("Projeto");
		LabelToolTitle.setForeground(new Color(255, 255, 255));
		LabelToolTitle.setFont(new Font("Segoe UI", Font.BOLD, 18));
		
		JLabel LabelToolBarSave = new JLabel("");
		LabelToolBarSave.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				try {
					if(!TextFieldName.getText().equals("")) {
						Project project = new Project();
						project.setName(TextFieldName.getText());
						project.setDescription(TextAreaDescription.getText());
						controller.save(project);
						JOptionPane.showMessageDialog(rootPane, "Projeto salvo com sucesso!");
						try {
							dispose();
						} catch (Exception e3) {
							JOptionPane.showMessageDialog(rootPane, "Erro ao fechar a janela! " + e3.getMessage());
						}
					} else {
						JOptionPane.showMessageDialog(rootPane, "O Projeto não foi salvo, pois o campo nome não foi preenchido!");
					}
				} catch (Exception e2) {
					JOptionPane.showMessageDialog(rootPane, e2.getMessage());
				}
			}
		});
		LabelToolBarSave.setHorizontalAlignment(SwingConstants.CENTER);
		LabelToolBarSave.setIcon(new ImageIcon("C:\\Users\\funcr\\eclipse-workspace\\TodoApp\\resources\\check.png"));
		GroupLayout gl_PanelToolBar = new GroupLayout(PanelToolBar);
		gl_PanelToolBar.setHorizontalGroup(
			gl_PanelToolBar.createParallelGroup(Alignment.TRAILING)
				.addGroup(Alignment.LEADING, gl_PanelToolBar.createSequentialGroup()
					.addGap(19)
					.addComponent(LabelToolTitle, GroupLayout.PREFERRED_SIZE, 111, GroupLayout.PREFERRED_SIZE)
					.addPreferredGap(ComponentPlacement.RELATED, 172, Short.MAX_VALUE)
					.addComponent(LabelToolBarSave, GroupLayout.PREFERRED_SIZE, 47, GroupLayout.PREFERRED_SIZE)
					.addContainerGap())
		);
		gl_PanelToolBar.setVerticalGroup(
			gl_PanelToolBar.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_PanelToolBar.createSequentialGroup()
					.addContainerGap()
					.addGroup(gl_PanelToolBar.createParallelGroup(Alignment.LEADING)
						.addComponent(LabelToolBarSave, GroupLayout.PREFERRED_SIZE, 46, GroupLayout.PREFERRED_SIZE)
						.addComponent(LabelToolTitle, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
					.addContainerGap())
		);
		PanelToolBar.setLayout(gl_PanelToolBar);
		getContentPane().setLayout(groupLayout);
		controller = new ProjectController();
	}
}
