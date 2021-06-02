from selenium.webdriver.common.by import By


"""以下数据为自媒体、后台管理url"""
# 自媒体url
url_mp = "http://ttmp.research.itcast.cn/#/login"
# 后台管理url
url_mis = "http://ttmis.research.itcast.cn/#/"

"""以下数据为自媒体 登录模块 配置数据-->page_mp_login.py"""

# 用户名 13812345679
mp_username = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
# 验证码 246811
mp_code = (By.CSS_SELECTOR, "[placeholder='验证码']")
# 登录按钮
mp_login_btn = (By.XPATH, "/html/body/div[1]/div/div/form/div[4]/div/button/span")
# 昵称
mp_nickname = (By.CSS_SELECTOR, ".company-container")


"""以下数据为 发布文章 模块配置数据 -->page_mp_article.py"""

# 内容 管理
mp_content_manage = (By.XPATH, "//span[text()='内容管理']/..")

# 发布 文章
mp_publish_article = (By.XPATH, "//*[contains(text(),'发布文章')]")

# 文章 标题
mp_title = (By.CSS_SELECTOR, "[placeholder='文章名称']")

# iframe
mp_iframe = (By.CSS_SELECTOR, "#publishTinymce_ifr")

# 文章 内容 ：定位到body,勿定位<p>标签
mp_content = (By.CSS_SELECTOR, "#tinymce")

# 封面
mp_cover = (By.XPATH, "//*[contains(text(),'自动')]")

# 发 表
mp_submit = (By.XPATH, "//span[contains(text(),'发表')]")

# 结果
mp_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"


""" 以下数据为 后台登录 模块配置数据 --> page_mis_login"""

# 用户名  testid
mis_login = By.CSS_SELECTOR, "[placeholder='用户名']"

# 密码
mis_pwd = By.CSS_SELECTOR, "[placeholder='密码']"

# 登录 按钮
mis_login_btn = By.CSS_SELECTOR, "#inp1"

# 昵称  欢迎 test-管理员
mis_nickname = By.CSS_SELECTOR, ".user_info"


"""以下数据为 后台内容审核 模块配置数据 -->page_mis_audit"""

# 信息管理
mis_info_manage = By.XPATH, "//*[text()='信息管理']/."

# 内容审核
mis_content_audit = By.XPATH, "//*[text()='内容审核']/."

# 文章标题
mis_title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"

# 文章频道
mis_channel = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"

# 点击查询
mis_find = By.CSS_SELECTOR, ".find"

# 文章标题
mis_article_id = By.CSS_SELECTOR, ".cell>span"

# 通过
mis_pass = By.XPATH, "//*[text()='通过']/.."

# 确认通过
mis_confirm_pass = By.CSS_SELECTOR, ".el-button--primary"


"""以下为 app应用元素配置信息"""
# 设备名
advice = "79d70e23"
# 包名
appPackage = "com.myzaker.ZAKER_Phone"
# 启动名
appActivity = "com.myzaker.ZAKER_Phone.view.LogoActivity"


# 手机号
app_phone = By.XPATH, "//*[@index='1' and @class='android.widget.EditText']"
# 验证码
app_code = By.XPATH, "//*[@index='2' and @class='android.widget.EditText']"
# 登录 按钮
app_login_btn = By.XPATH, "//*[@text='登录' and @class='android.widget.Button']"
# 我的菜单
app_me = By.XPATH, "//*[@index='3' and contains(@text,'我的')]"
# 频道区域
app_channel_area = By.XPATH, "//*[@class='android.widget.HorizontalScrollview']"
# 文章区域
app_article = By.XPATH, "//*[@index='2' and @bounds='[0,520][1440,2288]']"
