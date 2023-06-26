# require 'capybara/cucumber'
require 'capybara'
require 'capybara/dsl'
require 'capybara/rspec/matchers'
require 'selenium-webdriver'

World(Capybara::DSL)
World(Capybara::RSpecMatchers)

Capybara.configure do |config|
  # Selenium
  # Selenium_Chrome
  # Selenium_Chrome_Healess

  config.default_driver = :selenium_chrome
  config.app_host = 'https://test.fap.softexrecife.org.br'
  config.default_max_wait_time = 5

end
