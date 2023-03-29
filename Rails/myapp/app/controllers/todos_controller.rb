class TodosController < ApplicationController
  before_action :set_todo, only: [:edit, :update, :show, :destroy]
  before_action :set_error, only: [:new, :edit]

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
        @error = @todo.errors.full_messages
        @errors = true
      end
      redirect_to new_todo_path(@todo, errors: @errors, error: @error)
    end
  end

  def show
  end

  def edit
  end

  def update
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

  def destroy
    @todo.destroy
    flash[:notice] = "Todo was deleted successfully"
    redirect_to todos_path
  end

  private

    def set_todo
      @todo = Todo.find(params[:id])
    end

    def set_error
      @errors = params[:errors] == 'true'
      @error = params[:error]
    end

    def todo_params
      params.require(:todo).permit(:nome, :description)
    end
end
