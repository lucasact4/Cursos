class ChefsController < ApplicationController

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
  end

  private

    def chef_params
      params.require(:chef).permit(:chefname, :email, :password, :password_confirmation)
    end

end