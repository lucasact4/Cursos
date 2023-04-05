class RecipesController < ApplicationController
  before_action :set_recipe, only: [:show, :update]
  before_action :set_error, only: [:new, :edit]

  def index
    @recipes = Recipe.paginate(page: params[:page], per_page: 5)
  end

  def show
    
  end

  def new
  end

  def create
    @recipe = Recipe.new(recipe_params)
    @recipe.chef = current_chef
    if @recipe.save
      flash[:success] = "Recipe was created successfully!"
      redirect_to recipe_path(@recipe)
    else
      if @recipe.errors.any?
        @errors = true
        @count = @recipe.errors.count
        @error = @recipe.errors.full_messages
      end
      redirect_to new_recipe_path(recipe: @recipe, errors: @errors, count: @count, error: @error)
    end
  end

  def edit
    @recipe = Recipe.find(params[:id]) if params[:id]
  end

  def update
    if @recipe.update(recipe_params)
      flash[:success] = "Recipe was updated successfully!"
      redirect_to recipe_path(@recipe)
    else
      if @recipe.errors.any?
        @errors = true
        @count = @recipe.errors.count
        @error = @recipe.errors.full_messages
      end
      redirect_to edit_recipe_path(recipe: @recipe, errors: @errors, count: @count, error: @error)
    end
  end

  def destroy
    Recipe.find(params[:id]).destroy
    flash[:success] = "Recipe deleted successfully"
    redirect_to recipes_path
  end

  private

    def set_recipe
      @recipe = Recipe.find(params[:id])
    end

    def set_error
      @error = params[:error]
      @count = params[:count]
      @errors = params[:errors] == 'true'
      @recipe = params[:recipe] || Recipe.new
    end
  
    def recipe_params
      params.require(:recipe).permit(:name, :description)
    end

end