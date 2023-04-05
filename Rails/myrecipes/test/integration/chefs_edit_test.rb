require "test_helper"

class ChefsEditTest < ActionDispatch::IntegrationTest

  def setup
    @chef = Chef.create!(chefname: "mashrur", email: "mashrur@example.com",
      password: "password", password_confirmation: "password")
    @chef2 = Chef.create!(chefname: "John", email: "john@example.com",
      password: "password", password_confirmation: "password")
    @admin_user = Chef.create!(chefname: "John1", email: "john1@example.com",
      password: "password", password_confirmation: "password", admin: true)
  end

  test "reject on invalid edit" do
    sign_in_as(@chef, "password")
    get edit_chef_path(@chef)
    assert_template 'chefs/edit'
    patch chef_path(@chef), params: { chef: {chefname: " ", email: "mashrur@example.com" } }
    assert_redirected_to edit_chef_path(chef: assigns(:chef), errors: assigns(:errors), count: assigns(:count), error: assigns(:error))
    follow_redirect!
    assert_select 'h2.panel-title'
    assert_select 'div.panel-body'
  end

  test "accept valid edit" do
    sign_in_as(@chef, "password")
    get edit_chef_path(@chef)
    assert_template 'chefs/edit'
    patch chef_path(@chef), params: { chef: {chefname: "mashrur1", email: "mashrur1@example.com" } }
    assert_redirected_to @chef
    assert_not flash.empty?
    @chef.reload
    assert_match "mashrur1", @chef.chefname
    assert_match "mashrur1@example.com", @chef.email
  end

  test "accept edit attemp by admin user" do
    sign_in_as(@admin_user, "password")
    get edit_chef_path(@chef)
    assert_response :success
    assert_template 'chefs/edit'
    patch chef_path(@chef), params: { chef: {chefname: "mashrur3", email: "mashrur3@example.com" } }
    assert_redirected_to @chef
    follow_redirect!
    assert_not flash.empty?
    @chef.reload
    assert_match "mashrur3", @chef.chefname
    assert_match "mashrur3@example.com", @chef.email
  end

  test "redirect edit attemp by another non-admin user" do
    sign_in_as(@chef2, "password")
    updated_name = "joe"
    updated_email = "joe@example.com"
    patch chef_path(@chef), params: { chef: {chefname: updated_name, email: updated_email } }
    assert_redirected_to chefs_path
    assert_not flash.empty?
    @chef.reload
    assert_match "mashrur", @chef.chefname
    assert_match "mashrur@example.com", @chef.email
  end

end
