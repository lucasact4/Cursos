class IngredientsController < ApplicationController
  before_action :set_ingredient, only: [:edit, :update, :show]
  before_action :set_error, only: [:new, :edit]
  before_action :require_admin, except: [:show, :index]
  
  def new
    @ingredient = Ingredient.new
  end

  def create
    @ingredient = Ingredient.new(ingredient_params)
    if @ingredient.save
      flash[:success] = "Ingredient was successfully created"
      redirect_to ingredient_path(@ingredient)
    else
      if @ingredient.errors.any?
        @errors = true
        @count = @ingredient.errors.count
        @error = @ingredient.errors.full_messages
      end
      redirect_to new_ingredient_path(ingredient: @ingredient, errors: @errors, count: @count, error: @error)
    end
  end

  def edit
    @ingredient = Ingredient.find(params[:id]) if params[:id]
  end

  def update
    if @ingredient.update(ingredient_params)
      flash[:success] = "Ingredient name was updated successfully"
      redirect_to @ingredient
    else
      redirect_to edit_ingredient_path(ingredient: @ingredient, errors: @errors, count: @count, error: @error)
    end
  end

  def show
    @ingredient_recipes = @ingredient.recipes.paginate(page: params[:page], per_page: 5)
  end

  def index
    @ingredients = Ingredient.paginate(page: params[:page], per_page: 5)
  end

  private

  def ingredient_params
    params.require(:ingredient).permit(:name)
  end

  def set_error
    @error = params[:error]
    @count = params[:count]
    @errors = params[:errors] == 'true'
    @ingredient = params[:ingredient] || Ingredient.new
  end

  def set_ingredient
    @ingredient = Ingredient.find(params[:id])
  end

  def require_admin
    if !logged_in? || (logged_in? and !current_chef.admin?)
      flash[:danger] = "Only admin users can perform that action"
      redirect_to ingredients_path
    end
  end

end