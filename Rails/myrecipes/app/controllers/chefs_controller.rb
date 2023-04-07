class ChefsController < ApplicationController
  before_action :set_chef, only: [:show, :update, :destroy]
  before_action :set_error, only: [:new, :edit]
  before_action :require_same_user, only: [:edit, :update, :destroy]
  before_action :require_admin, only: [:destroy]

  def index
    @chefs = Chef.paginate(page: params[:page], per_page: 5)
  end

  def new
  end

  def create
    @chef = Chef.new(chef_params)
    if @chef.save
      session[:chef_id] = @chef.id
      cookies.signed[:chef_id] = @chef.id
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
    @chef_recipes = @chef.recipes.paginate(page: params[:page], per_page: 5)
  end

  def edit
    @chef = Chef.find(params[:id]) if params[:id]
  end

  def update
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
    if !@chef.admin?
      @chef.destroy
      flash[:danger] = "Chef and all associated recipes have been deleted!"
      redirect_to chefs_path
    end
  end

  private

  def chef_params
    params.require(:chef).permit(:chefname, :email, :password, :password_confirmation)
  end

  def set_chef
    @chef = Chef.find(params[:id])
  end
  
  def set_error
    @error = params[:error]
    @count = params[:count]
    @errors = params[:errors] == 'true'
    @chef = params[:chef] || Chef.new
  end

  def require_same_user
    if current_chef != @chef and !current_chef.admin?
      flash[:danger] = "You can only edit or delete your own account"
      redirect_to chefs_path
    end
  end

  def require_admin
    if logged_in? && !current_chef.admin?
      flash[:danger] = "Only admin users can perform that action"
      redirect_to root_path
    end
  end

end