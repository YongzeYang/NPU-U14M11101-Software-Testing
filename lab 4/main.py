from appium import webdriver
from time import sleep

'''
测试需求1：
编写脚本启动应用，将介绍页面滑动至最右端（提示：可使用 driver.swipe
函数进行滑动操作），点击屏幕任意一处进入城市选择页面 ，在搜索框中输
入南京，点击南京进入应用主页面
'''

# 加载属性
desired_caps = {'platformName': 'Android', 'platformVersion': '7.1.2', 'deviceName': '127.0.0.1:62001',
                'appPackage': 'com.anjuke.android.app',
                'appActivity': 'com.anjuke.android.app.mainmodule.WelcomeActivity'}
# 启动驱动，进入安卓虚拟机
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# 定义一个点击操作并休眠两秒
def click_id(s):
    driver.find_element_by_id(s).click()
    sleep(2)


# 点击s1的第i个元素，并休眠2s
def click_ith_id(s, i):
    driver.find_elements_by_id(s)[i].click()
    sleep(2)


# 向s1发送s2并休眠两秒
def input(s1, s2):
    driver.find_element_by_id(s1).send_keys(s2)
    sleep(2)


# 向s1的第i个元素发送s2并休眠两秒
def input_ith(s1, s2, i):
    driver.find_elements_by_id(s1)[i].send_keys(s2)
    sleep(2)


# 根据xpath获取元素单击并休眠两秒
def click_xpath(s):
    driver.find_element_by_xpath(s).click()
    sleep(2)


# 向上滑动
def up():
    driver.swipe(width / 2, height * 5 / 6, width / 2, height / 6, 1000)


# 向右滑动
def right():
    driver.swipe(width * 5 / 6, height / 2, width / 6, height / 2, 1000)


# 向左滑动
def left():
    driver.swipe(width / 6, height / 2, width * 5 / 6, height / 2, 1000)


# 获取当前窗口的分辨率
height = driver.get_window_size()['height']
width = driver.get_window_size()['width']

# 点击同意并继续按钮
click_id("com.anjuke.android.app:id/ok_btn")
# 退出欢迎界面和选择界面
sleep(3)
driver.back()
driver.back()
# 点击“我知道了”
click_id("com.anjuke.android.app:id/tvRight")
# 程序的定位
sleep(2)
click_id("com.android.packageinstaller:id/permission_deny_button")
# 输入南京
# driver.tap([(width/2 , int(height/4))])
input("com.anjuke.android.app:id/edittext", "南京")
# 选择南京
click_id("com.anjuke.android.app:id/select_city_tv_item")

'''
测试需求2：
点击主页面的房价一栏的南京房价，进入房价选择页面，点击+关注，并查
看新房的房价情况，在新房的房价情况页面分别选择近 1 年或近 3 年进行查看
'''

#
click_id("com.anjuke.android.app:id/price_address_text_view")
click_id("com.anjuke.android.app:id/title_text_view")
click_id("com.anjuke.android.app:id/title_bar_back_button")
up()
click_id("com.anjuke.android.app:id/new_house_tv")
click_id("com.anjuke.android.app:id/housePriceTrendThreeYearTitle")
click_id("com.anjuke.android.app:id/communityReportBackBtn")

'''
测试需求3：
返回主页面，点击新房，点击房贷计算，点击按房屋总价，填写房屋总价 500，
点击开始计算，点击查看历史按钮查看计算历史

'''
click_id("com.anjuke.android.app:id/item_biz_icon")
click_xpath(".//*[@text='房贷计算']")
click_xpath(".//*[@text='按房屋总价']")
input_ith("android.widget.EditText", "500", 0)
sleep(2)
click_xpath(".//*[@text='开始计算']")
click_xpath(".//*[@text='查看历史']")
driver.back()
driver.back()
driver.back()

'''
测试需求4：
返回新房信息所在页面，点击第一条房源信息,点击变价通知，开盘通知以及
关注按钮，并点击右上角对比按钮，然后点击左上角的比价按钮进行比价房源选
择如图所示，选择猜你喜欢的前两套房源，然后点击开始对比
'''
click_id("com.anjuke.android.app:id/item_biz_icon")
up()
click_id("com.anjuke.android.app:id/title")
up()
click_id("com.anjuke.android.app:id/kaiPanTextView")
driver.back()
click_id("com.anjuke.android.app:id/bianJiaTextView")
driver.back()
click_id("com.anjuke.android.app:id/compareImageView")
up()
click_ith_id("android.widget.RadioButton", 1)
click_ith_id("android.widget.RadioButton", 2)
click_id("com.anjuke.android.app:id/new_house_building_compare_list_begin_compare")
driver.back()
driver.back()
driver.back()

'''
测试需求5：
退回主页面，点击消息，进入消息模块，对于热门群聊和优秀置业顾问，分别对
第一 条进行测试，点击后的所有子页面仅需到达
'''
click_ith_id("com.anjuke.android.app:id/view_maintab_model_icon", 1)
click_id("com.anjuke.android.app:id/start_group_button")
driver.back()
up()
click_id("com.anjuke.android.app:id/consultant_start_chat_button")
click_id("com.anjuke.android.app:id/title_bar_back_button")
driver.back()

'''
测试需求6：
点击有料，进入有料模块，对于推荐一栏的所有模块进行遍历
'''
click_ith_id("com.anjuke.android.app:id/view_maintab_model_icon", 2)
# 滑动13次进行遍历
for i in range(13):
    right()
    sleep(2)

'''
测试需求7：
对于问答模块，点击我要提问，在输入框内输入“南大和园多少钱一平方”，
点击提交。
'''
# 右滑11次
for i in range(11):
    left()
    sleep(1)

click_id("com.anjuke.android.app:id/iv_tiwen")
input("com.anjuke.android.app:id/qa_submit_question_et", "南大和园多少钱一平方")
click_id("com.anjuke.android.app:id/btnright")
driver.back()
driver.back()

'''
测试需求8：
点击推荐，进入推荐模块，对于图示模块进行遍历，仅要求到达，不要求进
一步测试
'''

click_ith_id("com.anjuke.android.app:id/view_maintab_model_icon", 3)
# 左滑4次
for i in range(4):
    left()
    sleep(2)
# 右滑6次
for i in range(6):
    right()
    sleep(2)
