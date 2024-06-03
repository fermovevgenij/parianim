def new_metamask(driver, account):
    """
    Create a new MetaMask account.

    Args:
        driver (selenium.webdriver.remote.webdriver.WebDriver): The Selenium WebDriver object.
        account (str): The name of the account to create.

    Returns:
        str: The address of the new account.
    """

    # Click the "Create a new wallet" button.
    driver.find_element_by_xpath("//button[contains(text(), 'Create a new wallet')]").click()

    # Click the "I agree" button.
    driver.find_element_by_xpath("//button[contains(text(), 'I Agree')]").click()

    # Click the "Create" button.
    driver.find_element_by_xpath("//button[contains(text(), 'Create')]").click()

    # Enter the account name.
    driver.find_element_by_xpath("//input[@placeholder='Account Name']").send_keys(account)

    # Enter the account password.
    driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(account)

    # Confirm the account password.
    driver.find_element_by_xpath("//input[@placeholder='Confirm Password']").send_keys(account)

    # Click the "Create" button.
    driver.find_element_by_xpath("//button[contains(text(), 'Create')]").click()

    # Get the address of the new account.
    address = driver.find_element_by_xpath("//span[@class='address']").text

    return address
