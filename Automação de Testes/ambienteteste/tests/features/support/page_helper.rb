Dir[File.join(File.dirname(__FILE__), '../pages/*_page.rb')].each { |file| require file }

class Pages
  def home
    @home ||= TagPage.new
  end
end