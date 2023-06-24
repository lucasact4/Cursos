require 'capybara/cucumber'
require 'selenium-webdriver'

Capybara.configure do |config|
  # Selenium
  # Selenium_Chrome
  # Selenium_Chrome_Healess

  config.default_driver = :selenium_chrome
  config.app_host = 'https://test.fap.softexrecife.org.br'
  config.default_max_wait_time = 5

end

World(Capybara::DSL)