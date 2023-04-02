class RecipesController < ApplicationController

  def index
    @recipes = Recipe.all
  end

  def show
    @recipe = Recipe.find(params[:id])
  end

  def new
    @error = params[:error]
    @count = params[:count]
    @errors = params[:errors] == 'true'
    @recipe = params[:recipe] || Recipe.new
  end

  def create
    @recipe = Recipe.new(recipe_params)
    @recipe.chef = Chef.first
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
    @error = params[:error]
    @count = params[:count]
    @errors = params[:errors] == 'true'
    @recipe = params[:recipe] || Recipe.new
    @recipe = Recipe.find(params[:id]) if params[:id]
  end

  def update
    @recipe = Recipe.find(params[:id])
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
  
    def recipe_params
      params.require(:recipe).permit(:name, :description)
    end

end