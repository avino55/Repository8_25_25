import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(2)
#driver.fullscreen_window()
action = ActionChains(driver)
expl_wait = WebDriverWait(driver,5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#expl_wait.until(expected_conditions.url_to_be(""))

driver.find_element(By.PARTIAL_LINK_TEXT,"Free Access").click()
# /*
# 		 * 1. What is XPath?
# 		 *
# 		 * 	  A query language which is used to find a node or set of nodes in XML/HTML document
# 		 *
# 		 * 2. Relative XPath Using Node Attributes
# 		 *
# 		 *    Syntax: //TagName[@Attribute Name="Attribute Value"]
# 		 *
# 		 */

driver.back()

# /*
# 		 * Relative XPath Using Text
# 		 *
# 		 * Syntax: //TagName[text()="Text"]
# 		 */


driver.find_element(By.XPATH,"//a[contains(text(),'Free Access ')]").click()
time.sleep(1)
driver.back()
driver.find_element(By.XPATH,"//input[contains(@name,'Option1')]").click()

element_to_hover = driver.find_element(By.XPATH,"//button[@id='mousehover']")
action.move_to_element(element_to_hover).perform()
time.sleep(3)
driver.find_element(By.LINK_TEXT,'Top').click()
# /*
# 		 * Dynamic Elements: Elements with dynamic property-values and/or text
# 		 *
# 		 * 1. Using 'and' Operator
# 		 *    Syntax:
# 		 *    //TagName[@Att1='Value1' and @Att2='Value2']
# 		 *    //TagName[@Att='Value' and Text()='Value']
# 		 *
# 		 * 2. Using 'or' Operator
# 		 * 	  Syntax:
# 		 *    //TagName[@Att1='Value1' or @Att2='Value2']
# 		 *    //TagName[@Att='Value' or Text()='Value']
# 		 *
# 		 * 3. Using 'contains'
# 		 *    Syntax:
# 		 *    //TagName[contains(@Att,'Partial Value')]
# 		 *    //TagName[contains(text(),'Partial Value')]
# 		 *
# 		 * 4. Using 'starts-with'
# 		 * 	  Syntax:
# 		 *    //TagName[starts-with(@Att,'Starting Value')]
# 		 *    //TagName[starts-with(text(),'Starting Value')]
# 		 *
# 		 * 5. Hybrid
# 		 * 	  Syntax:
# 		 * 	  //TagName[contains(@Att1,'Partial Value') and starts-with(text(),'Starting Value')]
# 		 * 	  //TagName[@Att1='Value' or starts-with(@Att2,'Starting Value')]
# 		 *    //*[@Att='Value']
# 		 *
# 		 */
name_to_print= driver.find_element(By.XPATH,'(//td[contains(text(),"Write")])')
print(name_to_print.text)

selected_field = Select(driver.find_element(By.XPATH,"(//select[@id='dropdown-class-example'])[1]"))

selected_field.select_by_visible_text('Option1')
# /*
# 		 * XPath Axes: Parent and Child Relation
# 		 *
# 		 * Syntax:
# 		 *
# 		 * //Node1/child::*
# 		 *
# 		 * //Node1/parent::*
# 		 *
# 		 */

driver.find_element(By.XPATH,"//fieldset/child::input[@value='Hide']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//fieldset/child::input[@value='Show']").click()

driver.find_element(By.XPATH,"(//input[@id='autocomplete'])[1]").send_keys("USA")
         #
		 # * XPath Axes: Ancestor and Descendant Relationship
		 # *
		 # * Syntax:
		 # *
		 # * //Node1/ancestor::*
		 # *
		 # * //Node1/descendant::*
		 # *
		 # */

driver.find_element(By.XPATH,"//div[@class = 'block large-row-spacer'][2]/descendant::input[@id='name']").send_keys("Checking Dependent")
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class = 'block large-row-spacer'][2]/descendant::input[@id='confirmbtn']").click()
alert = Alert(driver)
# alert.accept()
alert.dismiss()
info_AXV = driver.find_element(By.XPATH,"//legend[normalize-space()='Switch Window Example']")

print(info_AXV.text)


#  * XPath Axes: Preceding and Following
#  *
#  * Syntax:
#  *
#  * //Node1/preceding::*
#  *
#  * //Node1/preceding-sibling::*
#  *
#  * //Node1/following::*
#  *
#  * //Node1/following-sibling::*
#  *

legend = driver.find_element(By.XPATH,"//label[@for='radio2']/preceding::legend").text

print(f"This is the legend -->{legend}")

legend2 = driver.find_element(By.XPATH,"//label[@for='radio3']/preceding::label[1]/input").text
#legend2 = driver.find_element(By.XPATH,"label[for='radio3'] preceding::label[1] input").text
legend3 = driver.find_element(By.XPATH,"//label[@for='radio3']/preceding::label[1]/child::input")
attrib_legend2 = legend3.get_attribute("name")

print(f"This is attribute of {attrib_legend2}")


# #CSS /*
# 		 * What is CSS and CSS Selector?
# 		 *
# 		 * CSS (Cascading Style Sheets): Describes presentation of elements mentioned in HTML
# 		 *
# 		 * CSS Selector: Pointer for applying the styling mentioned in CSS
# 		 *
# 		 **** Creating CSS Selector Using Attributes ****
# 		 * 	Syntax: TagName[Att1=Value]
# 		 * 	In case Att1 is 'id' or 'class' then we can use following symbols:
# 		 * 		id => # (hash)
# 		 * 		class => . (dot)
# 		 * 	Examples: 1. div#u123   2. span.layerParent

driver.find_element(By.CSS_SELECTOR,"#openwindow").click()

all_window_handles = driver.window_handles

# Switch to the new window (the last one in the list)
new_window_handle = all_window_handles[-1]
driver.switch_to.window(new_window_handle)

# Navigate to a URL in the new window (if needed)
#driver.get("https://www.google.com")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#app_carts = driver.find_elements(By.CSS_SELECTOR,"ADD TO CART")
# Get and print the title of the new window
new_window_title = driver.title
print(f"Title of the new window: {new_window_title}")

#driver.get("https://google.com")

# Switch back to the original window (if needed)
original_window_handle = all_window_handles[0]
driver.switch_to.window(original_window_handle)
time.sleep(1)

print(driver.title)

driver.find_element(By.CSS_SELECTOR,"a.btn-style").click()

for i in all_window_handles:

        print(i)

print("*" * 25)
driver.close()


