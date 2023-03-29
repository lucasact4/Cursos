class TodosController < ApplicationController

  def new
    @errors = params[:errors] == 'true'
    @error = params[:error]
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
        @error = @todo.errors.full_messages
        @errors = true
      end
      redirect_to new_todo_path(@todo, errors: @errors, error: @error)
    end
  end

  def show
    @todo = Todo.find(params[:id])
  end

  def edit
    @errors = params[:errors] == 'true'
    @error = params[:error]
    @todo = Todo.find(params[:id])
  end

  def update
    @todo = Todo.find(params[:id])
    if @todo.update(todo_params)
      flash[:notice] = "Todo was succesfully updated"
      redirect_to todo_path(@todo)
    else
      if @todo.errors.any?
        flash[:error] = "The following errors prevented the todo from being saved"
        @error = @todo.errors.full_messages
        @errors = true
      end
      redirect_to edit_todo_path(@todo, errors: @errors, error: @error)
    end
  end

  def index
    @todos= Todo.all
  end

  private

    def todo_params
      params.require(:todo).permit(:nome, :description)
    end
end
