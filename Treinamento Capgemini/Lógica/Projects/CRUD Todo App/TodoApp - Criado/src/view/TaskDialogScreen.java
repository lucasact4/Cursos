package view;

import java.awt.Color;
import java.awt.Font;
import javax.swing.GroupLayout;
import javax.swing.ImageIcon;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.GroupLayout.Alignment;
import javax.swing.LayoutStyle.ComponentPlacement;
import javax.swing.border.EtchedBorder;
import javax.swing.text.DateFormatter;
import javax.swing.text.DefaultFormatterFactory;

import controller.TaskController;
import model.Project;
import model.Task;

import java.awt.Dimension;
import javax.swing.JScrollPane;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.swing.JFormattedTextField;

public class TaskDialogScreen extends JDialog {
	
	private JTextField TextFieldName;
	TaskController controller;
	Project project;
	private final JPanel contentPanel = new JPanel();

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try {
			TaskDialogScreen dialog = new TaskDialogScreen();
			dialog.setDefaultCloseOperation(
					JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Create the dialog.
	 */
	public TaskDialogScreen() {
		setMinimumSize(new Dimension(250, 400));
		setBounds(125, 125, 375, 625);
		JPanel PanelToolBar = new JPanel();
		PanelToolBar.setBackground(new Color(0, 153, 102));
		
		JPanel PanelTask = new JPanel();
		PanelTask.setBorder(new EtchedBorder(EtchedBorder.LOWERED, null, null));
		PanelTask.setBackground(new Color(255, 255, 255));
		GroupLayout groupLayout = new GroupLayout(getContentPane());
		groupLayout.setHorizontalGroup(
			groupLayout.createParallelGroup(Alignment.LEADING)
				.addComponent(PanelToolBar, GroupLayout.DEFAULT_SIZE, 359, Short.MAX_VALUE)
				.addGroup(groupLayout.createSequentialGroup()
					.addGap(10)
					.addComponent(PanelTask, GroupLayout.DEFAULT_SIZE, 339, Short.MAX_VALUE)
					.addGap(10))
		);
		groupLayout.setVerticalGroup(
			groupLayout.createParallelGroup(Alignment.LEADING)
				.addGroup(groupLayout.createSequentialGroup()
					.addComponent(PanelToolBar, GroupLayout.PREFERRED_SIZE, 66, GroupLayout.PREFERRED_SIZE)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(PanelTask, GroupLayout.DEFAULT_SIZE, 303, Short.MAX_VALUE)
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
		
		JLabel LabelDeadline = new JLabel("Prazo");
		LabelDeadline.setFont(new Font("Segoe UI", Font.PLAIN, 14));
		
		JLabel LabelNotes = new JLabel("Notas");
		LabelNotes.setFont(new Font("Segoe UI", Font.PLAIN, 14));
		
		JScrollPane ScrollPaneDescription = new JScrollPane();
		ScrollPaneDescription.setBorder(new EtchedBorder(EtchedBorder.LOWERED, null, null));
		
		JScrollPane ScrollPaneNotes = new JScrollPane();
		ScrollPaneNotes.setBorder(new EtchedBorder(EtchedBorder.LOWERED, null, null));
		
		DateFormatter dateFormatter = new DateFormatter();
		JFormattedTextField FormattedTextFieldDeadline = new JFormattedTextField();
		FormattedTextFieldDeadline.setFormatterFactory(new DefaultFormatterFactory(dateFormatter));
		FormattedTextFieldDeadline.setFocusLostBehavior(JFormattedTextField.PERSIST);
		GroupLayout gl_PanelTask = new GroupLayout(PanelTask);
		gl_PanelTask.setHorizontalGroup(
			gl_PanelTask.createParallelGroup(Alignment.TRAILING)
				.addGroup(gl_PanelTask.createSequentialGroup()
					.addContainerGap()
					.addGroup(gl_PanelTask.createParallelGroup(Alignment.LEADING)
						.addComponent(ScrollPaneNotes, GroupLayout.DEFAULT_SIZE, 315, Short.MAX_VALUE)
						.addComponent(ScrollPaneDescription, GroupLayout.DEFAULT_SIZE, 315, Short.MAX_VALUE)
						.addComponent(TextFieldName, GroupLayout.DEFAULT_SIZE, 315, Short.MAX_VALUE)
						.addComponent(LabelName)
						.addComponent(LabelDescription)
						.addComponent(LabelNotes, GroupLayout.PREFERRED_SIZE, 58, GroupLayout.PREFERRED_SIZE)
						.addComponent(LabelDeadline, GroupLayout.PREFERRED_SIZE, 37, GroupLayout.PREFERRED_SIZE)
						.addComponent(FormattedTextFieldDeadline, GroupLayout.DEFAULT_SIZE, 315, Short.MAX_VALUE))
					.addContainerGap())
		);
		gl_PanelTask.setVerticalGroup(
			gl_PanelTask.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_PanelTask.createSequentialGroup()
					.addContainerGap()
					.addComponent(LabelName)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(TextFieldName, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
					.addGap(18)
					.addComponent(LabelDescription)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(ScrollPaneDescription, GroupLayout.PREFERRED_SIZE, 142, GroupLayout.PREFERRED_SIZE)
					.addGap(18)
					.addComponent(LabelDeadline, GroupLayout.PREFERRED_SIZE, 20, GroupLayout.PREFERRED_SIZE)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(FormattedTextFieldDeadline, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
					.addGap(22)
					.addComponent(LabelNotes, GroupLayout.PREFERRED_SIZE, 20, GroupLayout.PREFERRED_SIZE)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(ScrollPaneNotes, GroupLayout.DEFAULT_SIZE, 129, Short.MAX_VALUE)
					.addContainerGap())
		);
		
		JTextArea TextAreaNotes = new JTextArea();
		TextAreaNotes.setFont(new Font("Segoe UI", Font.PLAIN, 14));
		ScrollPaneNotes.setViewportView(TextAreaNotes);
		
		JTextArea TextAreaDescription = new JTextArea();
		TextAreaDescription.setFont(new Font("Segoe UI", Font.PLAIN, 14));
		ScrollPaneDescription.setViewportView(TextAreaDescription);
		PanelTask.setLayout(gl_PanelTask);
		
		JLabel LabelToolBarTitle = new JLabel("Tarefa");
		LabelToolBarTitle.setForeground(new Color(255, 255, 255));
		LabelToolBarTitle.setFont(new Font("Segoe UI", Font.BOLD, 18));
		
		JLabel LabelToolBarSave = new JLabel("");
		LabelToolBarSave.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				try {
					if(!TextFieldName.getText().isEmpty() && !FormattedTextFieldDeadline.getText().isEmpty()) {
						Task task = new Task();
						task.setProject_id(project.getId());
						task.setName(TextFieldName.getText());
						task.setDescription(TextAreaDescription.getText());
						task.setNotes(TextAreaNotes.getText());
						task.setCompleted(false);
						
						SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
						Date deadline = null;
						deadline = dateFormat.parse(FormattedTextFieldDeadline.getText());
						task.setDeadline(deadline);
						
						controller.save(task);
						JOptionPane.showMessageDialog(rootPane, "Tarefa salva com sucesso!");
						try {
							dispose();
						} catch (Exception e3) {
							JOptionPane.showMessageDialog(rootPane, e3.getMessage());
							JOptionPane.showMessageDialog(rootPane, "Erro ao fechar a janela!");
						}
					} else {
						JOptionPane.showMessageDialog(rootPane,  "A tarefa não foi salva pois existem"
								+ "campos obrigatórios a serem preenchidos!");
					}
				} catch (Exception e2) {
					JOptionPane.showMessageDialog(rootPane, "Erro ao salvar a tarefa: " + e2.getMessage());
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
					.addComponent(LabelToolBarTitle, GroupLayout.PREFERRED_SIZE, 111, GroupLayout.PREFERRED_SIZE)
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
						.addComponent(LabelToolBarTitle, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
					.addContainerGap())
		);
		PanelToolBar.setLayout(gl_PanelToolBar);
		getContentPane().setLayout(groupLayout);
		controller = new TaskController();
	}

	public void setProject(Project project) {
		this.project = project;
	}
	
}
