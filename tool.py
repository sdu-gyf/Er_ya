#encoding=gbk
import sys
import time
from selenium import webdriver

# 尝试登陆尔雅

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
login = "http://passport2.chaoxing.com/wunitlogin?refer=http%3A%2F%2Ferya.mooc.chaoxing.com%2F"
driver.get(login)

try:
    driver.find_element_by_id('FidName').send_keys("山东大学")
    time.sleep(0.2)
    driver.find_element_by_id('2093').click()
    username = input('请输入用户名')
    driver.find_element_by_id('idNumber').send_keys(username)
    password = input('请输入密码')
    driver.find_element_by_id('pwd').send_keys(password)
    numcode = input("请输入验证码:")
    driver.find_element_by_id('numcode').send_keys(numcode)
    driver.find_element_by_class_name('loginBtn').click()
    print('正在尝试登陆尔雅')
    try: # 进入刷课界面
        print('登陆成功，正在尝试进入个人空间')
        time.sleep(1)
        study="http://i.mooc.chaoxing.com"
        driver.get(study)
        print('进入个人空间成功，正在尝试跳转到课程界面')
        target = driver.find_element_by_id('zne_kc_icon')
        driver.execute_script("arguments[0].scrollIntoView();", target)
        driver.find_element_by_id('zne_kc_icon').click()
        print('跳转到课程界面成功，正在尝试选择视频')
        time.sleep(1)
        driver.switch_to_frame('frame_content')
        name=input('请输入课程名（你看到什么就输入什么，包括省略号）')
        driver.find_element_by_link_text(name).click()
        print('进入视频列表成功')
        try:#遍历课表
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(0.2)
            print('正在尝试进入视频播放界面')
            driver.find_element_by_xpath("//span[@class='icon']/em[@class='orange']/../following-sibling::span[1]/a").click()
            print('进入视频播放页面成功。')
            try:
                for _ in range(sys.maxsize):
                    try:
                        print('正在尝试播放视频')
                        time.sleep(1)
                        print('正在尝试播放现在未完成视频')
                        time.sleep(1)
                        target = driver.find_element_by_xpath("//span[@class='roundpointStudent  orange01 a002 jobCount'][text()='2']")
                        driver.execute_script("arguments[0].scrollIntoView();", target)
                        driver.find_element_by_xpath("//span[@class='roundpointStudent  orange01 a002 jobCount'][text()='2']/../a").click()
                        time.sleep(1)
                        print('正在尝试注入js')
                        time.sleep(1)
                        fp = open('.\\js.txt', 'r')
                        try:
                            js = fp.read()
                            time.sleep(0.02)
                            driver.execute_script(js)
                        finally:
                            fp.close()
                        time.sleep(0.05)
                        driver.find_element_by_id('lfsenior').click()
                        print('注入js成功')
                        driver.switch_to.frame("iframe")
                        time.sleep(1)
                        iframe = driver.find_element_by_xpath("//div[@class='ans-attach-ct']/iframe")
                        time.sleep(1)
                        driver.switch_to.frame(iframe)
                        time.sleep(1)
                        print('视频正在播放')
                        time.sleep(5)
                        vedio=driver.find_element_by_id("video_html5_api")
                        duration = driver.execute_script("return arguments[0].duration", vedio)
                        print('视频时间',duration,'秒')
                        time.sleep(duration)
                        time.sleep(0.05)
                        print('本视频播放完成，即将自动切换到下一个视频')
                        driver.switch_to_default_content()
                        time.sleep(0.1)
                        driver.find_element_by_xpath('//html/body/div[3]/div/div[1]/a').click()
                        driver.find_element_by_xpath("//span[@class='icon']/em[@class='orange']/../following-sibling::span[1]/a").click()
                    except:
                        print('刷课失败或者可已经刷完，请自行确认')
                        break
            except:
                print("进入视频播放页面失败,请关闭程序重试")
        except:
            print('进入视频列表界面失败，请关闭程序重试')
    except:
        print('进入课程页面失败请关闭程序重试')
except:
    print('登陆失败，请关闭程序重试')
time.sleep(1)

