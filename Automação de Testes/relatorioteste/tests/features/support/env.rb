require 'capybara/cucumber'
require 'selenium-webdriver'
require 'site_prism'
require_relative 'page_helper.rb'
require_relative 'helper.rb'

BROWSER = ENV['BROWSER']
AMBIENTE = ENV['AMBIENTE']

CONFIG = YAML.load_file(File.dirname(__FILE__) + "/ambientes/#{AMBIENTE}.yml")

Capybara.register_driver :selenium do |app|

  if BROWSER.eql?('chrome_headless')
    CAPYBARA::SELENIUM::DRIVER.NEW(APP, :BROWSER => :CHROME, desired_capabilities: Selenium::WebDriver::Remote::Capabilities.chrome(
      'chromeOptions' => {'args' =>['--headless', 'disable-gpu']}
    ))
  elsif BROWSER.eql?('chrome')
    CAPYBARA::SELENIUM::DRIVER.NEW(APP, :BROWSER => :CHROME)
  elsif BROWSER.eql?('firefox')
    CAPYBARA::SELENIUM::DRIVER.NEW(APP, :BROWSER => :FIREFOX, :MARIONETTE =>TRUE)
  elsif BROWSER.eql?('ie')
    CAPYBARA::SELENIUM::DRIVER.NEW(APP, :BROWSER => :INTERNET_EXPLORER)
  elsif BROWSER.eql?('safari')
    CAPYBARA::SELENIUM::DRIVER.NEW(APP, :BROWSER => :SAFARI)
  elsif BROWSER.eql?('poltergeist')
    OPTIONS = { JS_ERRORS: FALSE }
    CAPYBARA::POLTERGEIST::DRIVER.NEW(APP, OPTIONS)
  elsif BROWSER.eql?('brave')
    CAPYBARA::SELENIUM::DRIVER.NEW(APP, :BROWSER => :BRAVE)
  end
end

World(Pages)
World(Helper)

Capybara.configure do |config|

  config.default_driver = :selenium
  config.app_host = CONFIG['url_padrao']
  CONFIG['user']
  config.default_max_wait_time = 5

end
