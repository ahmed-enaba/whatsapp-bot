from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from tkinter import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def send_byNumber(the_num):
    options=Options()
    options.add_experimental_option("detach",True)
    service=Service(ChromeDriverManager().install())
    options.add_argument("user-data-dir=C:/chrome_profile")
    driver = webdriver.Chrome(options=options)
    link=f"https://web.whatsapp.com/send?phone=2{the_num}"
    msg=entry.get()

    driver.get(link)
    time.sleep(5)
    try:
        msg_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//footer//div[@contenteditable="true"]'))).send_keys(msg)
        msg_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Send"]'))).click()
        time.sleep(2)
        driver.close()
    except:
        print("we have a error on selectors")
        driver.quit()

    



def send_setion2():
    button2=Button(window,text="for one number",command=only_one)
    button2.place(x=150,y=170)


def clear_widgets():
            for widget in window.winfo_children():
                if widget not in [label, entry, send_button, send_byname, close_button]:
                    widget.destroy()

def only_one():
    the_num=Entry(window,width=20)
    the_num.place(x=140,y=205)

    num_label=Label(window,text="Enter the number here:",font='bold',background=window["background"])
    num_label.place(x=130,y=225)

    number=the_num.get()
    if not number.startswith("01"):
        print("the number you have entered was wrong")
    Go_button=Button(window,text="GO",font='bold',activebackground='aqua',command=lambda:send_byNumber(the_num.get()))
    Go_button.place(x=170,y=255)





def get_theName():
    name=Entry(window,width=20)
    name.place(x=240,y=180)

    label2=Label(window,text="input the name",font='bold',background=window["background"])
    label2.place(x=240,y=200)

    go_button=Button(window,text="GO",font='bold',activebackground='aqua',command=lambda:send_section3(name.get()))
    go_button.place(x=280,y=230)



def send_section3(receiver):
    link="https://web.whatsapp.com/"
    options=Options()
    options.add_experimental_option("detach",True)
    service=Service(ChromeDriverManager().install())
    options.add_argument("user-data-dir=C:/chrome_profile")
    driver = webdriver.Chrome(options=options)
    driver.get(link)

    try:
        search_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Search input textbox"]')))
        search_box.send_keys(receiver)
        search_box.send_keys(Keys.ARROW_DOWN,Keys.ENTER)

        msg_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//footer//div[@contenteditable="true"]'))
        )
        msg=entry.get()
        msg_box.send_keys(msg)
        send=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Send"][@data-tab="11"]'))).click()
        time.sleep(2)
        driver.close()
    except:
        print("we have a error in selectors")





def close():
    window.destroy()





window=Tk()
window.title("Whatsapp Bot")
window.geometry("600x450")
window.configure(background="gray")

label=Label(window,text=("Input your massage here:"),font='bold',background=window['background'])
label.place(x=180,y=100)

entry=Entry(window,width=60)
entry.place(x=120,y=80)


send_button=Button(window,text="Send",font="bold",activebackground="aqua",command=send_setion2)
send_button.place(x=170,y=130)

send_byname=Button(window,text="Send By Name",font='bold',activebackground="aqua",command=get_theName)
send_byname.place(x=240,y=130)

close_button=Button(window,text="Close",font='bold',activebackground="aqua",command=close)
close_button.place(x=380,y=130)

copyright_label=Label(window,text="@All Copy Right Are Reseved By Ahmed Elsayed",font=("arial",9),background=window['background'])
copyright_label.pack(side="bottom",pady=4)


window.mainloop()

