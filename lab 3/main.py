from time import sleep

from selenium import webdriver

# 使用Chrome驱动
driver = webdriver.Chrome()

# 0.进入网页
driver.get('https://nj.zu.anjuke.com')

# 1.点击租房
'''
元素的xpath路径根据该元素html结构定位。
简单获取xpath路径的方法：
浏览器打开网页，进入开发者模式，查看源码，选中要点击的内容后，右键copy->copy Xpath即可。
'''
driver.find_element_by_xpath("html/body/div[2]/div/ul/li[4]/a").click()
sleep(2)

# 2.地址选择南京
driver.find_element_by_xpath("//*[@id='switch_apf_id_5']/i").click()
sleep(2)

# 3. 点击"地铁找房"
driver.find_element_by_xpath("/html/body/div[4]/ul/li[2]/a").click()
sleep(2)

# 4. 选择"2号线"
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/span[2]/div/a[3]").click()
sleep(2)

# 5. 选择"马群"
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/span[2]/div/div/a[20]").click()
sleep(2)

# 6. 设置租金5000-8000元并点击确定
driver.find_element_by_xpath("//*[@id='from-price']").send_keys("5000")
sleep(2)
driver.find_element_by_xpath("//*[@id='to-price']").send_keys("8000")
sleep(2)
driver.find_element_by_xpath("//*[@id='pricerange_search']").click()
sleep(2)

# 7. 选择"整租"
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[4]/span[2]/a[2]").click()
sleep(2)

# 8. 选择"普通住宅"
driver.find_element_by_xpath("//*[@id='condmenu']/ul/li[2]/a").click()
sleep(2)
driver.find_element_by_xpath("//*[@id='condmenu']/ul/li[2]/ul/li[2]/a").click()
sleep(2)

# 9. 搜索"经天路"
driver.find_element_by_xpath("//*[@id='search-rent']").send_keys("经天路")
sleep(2)
driver.find_element_by_xpath("//*[@id='search-button']").click()
sleep(2)

# 10. 选择"视频看房"
driver.find_element_by_xpath("//*[@id='list-content']/div[1]/a[2]").click()
sleep(2)

# 11. 依次点击"租金"、"最新"排序查看
driver.find_element_by_xpath("//*[@id='list-content']/div[2]/div/a[2]").click()
sleep(2)

driver.find_element_by_xpath("//*[@id='list-content']/div[2]/div/a[3]").click()
sleep(2)

# 12. 点击第一个搜索出来的房源进行查看
driver.find_element_by_xpath("//*[@id='list-content']/div[3]").click()
sleep(2)
