class ChefsController < ApplicationController

  def index
    @chefs = Chef.paginate(page: params[:page], per_page: 5)
  end

  def new
    @error = params[:error]
    @count = params[:count]
    @errors = params[:errors] == 'true'
    @chef = params[:chef] || Chef.new
  end

  def create
    @chef = Chef.new(chef_params)
    if @chef.save
      flash[:success] = "Welcome #{@chef.chefname} to MyRecipes App!"
      redirect_to chef_path(@chef)
    else
      if @chef.errors.any?
        @errors = true
        @count = @chef.errors.count
        @error = @chef.errors.full_messages
      end
      redirect_to signup_path(chef: @chef, errors: @errors, count: @count, error: @error)
    end
  end

  def show
    @chef = Chef.find(params[:id])
    @chef_recipes = @chef.recipes.paginate(page: params[:page], per_page: 5)
  end

  def edit
    @error = params[:error]
    @count = params[:count]
    @errors = params[:errors] == 'true'
    @chef = params[:chef] || Chef.new
    @chef = Chef.find(params[:id]) if params[:id]
  end

  def update
    @chef = Chef.find(params[:id])
    if @chef.update(chef_params)
      flash[:success] = "Your account was updated successfully"
      redirect_to @chef
    else
      if @chef.errors.any?
        @errors = true
        @count = @chef.errors.count
        @error = @chef.errors.full_messages
      end
      redirect_to edit_chef_path(chef: @chef, errors: @errors, count: @count, error: @error)
    end
  end

  def destroy
    @chef = Chef.find(params[:id])
    @chef.destroy
    flash[:danger] = "Chef and all associated recipes have been deleted!"
    redirect_to chefs_path
  end

  private

    def chef_params
      params.require(:chef).permit(:chefname, :email, :password, :password_confirmation)
    end

end