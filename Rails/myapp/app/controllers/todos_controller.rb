class TodosController < ApplicationController
  def new
    @todo = Todo.new
  end

  def create
    @todo = Todo.new(todo_params)
    if @todo.save
      flash[:notice] = "Todo was created successfully!"
      redirect_to todo_path(@todo)
    else
      if @todo.errors.any?
        flash[:error] = "The following errors prevented the todo from being saved"
        @teste = true
      end
      redirect_to new_todo_path
    end
  end

  def show
    @todo = Todo.find(params[:id])
  end

  private

    def todo_params
      params.require(:todo).permit(:nome, :description)
    end
end
