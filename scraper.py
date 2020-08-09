from selenium import webdriver

DRIVER_PATH = 'C:\Program Files\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get('example.com')

websiteTitle = driver.title
firstPost = driver.find_element_by_xpath('//*[@id="post-7"]/div/header/h2/a')

if websiteTitle:
    print(websiteTitle)
else: 
    print("Couldn't get title")


if firstPost.text:
    print(firstPost.text)
    firstPost.click()
    excerpt = driver.find_element_by_xpath('//*[@id="post-7"]/div/div/p[1]')

    if(excerpt.text):
        print(excerpt.text)

        commentTextField = driver.find_element_by_xpath('//*[@id="comment"]')
        commentNameField = driver.find_element_by_xpath('//*[@id="author"]')
        commentEmailField = driver.find_element_by_xpath('//*[@id="email"]')
        commentSubmitButton = driver.find_element_by_xpath('//*[@id="submit"]')

        commentTextField.send_keys("Some content here")
        commentNameField.send_keys("John Doe")
        commentEmailField.send_keys("john.doe@example.com")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        commentSubmitButton.click()

    else:
        print('Couldn\'t find excerpt for post.')
else:
    print('Couldn\'t find first post')

driver.quit()
