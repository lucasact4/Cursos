Quando("eu uso um script") do
  visit ''
  page.execute_script("window.scrollBy(0,1500)")
  @result = page.evaluate_script('4 + 4');
  puts @result
  sleep(2)
end