class Locator(object):

    # Demo page
    admin_backend_link = '//*[@id="Main"]/section[1]/div/div/div[4]/div/div/div[2]/div/div/div[1]/div/a/small'

    # Admin login page
    login_email = '/html/body/div[1]/form[1]/div[1]/label[1]/input'
    login_password = '/html/body/div[1]/form[1]/div[1]/label[2]/input'
    login_button = '/html/body/div[1]/form[1]/button/span[1]'

    # Admin page
    dashboard_title = '//*[@id="content"]/div[2]/div[2]/p'
    accounts_tab = '//*[@id="bs-navbar-collapse-1"]/ul[1]/li[3]/a'
    admin_page_link = '//*[@id="bs-navbar-collapse-1"]/ul[1]/li[3]/ul/li[1]/a'
    add_new_admin_user = '//*[@id="content"]/div[2]/form/button'

    # Add admin form
    first_name = '//*[@id="content"]/form/div[1]/div/div[2]/div/div[1]/div/input'
    last_name = '//*[@id="content"]/form/div[1]/div/div[2]/div/div[2]/div/input'
    email = '//*[@id="content"]/form/div[1]/div/div[2]/div/div[3]/div/input'
    password = '//*[@id="content"]/form/div[1]/div/div[2]/div/div[3]/div/input'
    phone = '//*[@id="content"]/form/div[1]/div/div[2]/div/div[5]/div/input'
    country = '//*[@id="select2-drop-mask"]'
    address1 = '//*[@id="content"]/form/div[1]/div/div[2]/div/div[8]/div/input'
    address2 = '//*[@id="content"]/form/div[1]/div/div[2]/div/div[9]/div/input'
    submit = '//*[@id="content"]/form/div[1]/div/div[3]/button'
