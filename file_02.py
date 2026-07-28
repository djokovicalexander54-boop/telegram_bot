from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telebot
from telebot import apihelper
import time
import os
import sqlite3
from openai import OpenAI
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
data_program = sqlite3.connect(r"C:\Users\karino\Desktop\PROJECTS\file_1\data_id.db")
connecting = data_program.cursor()
connecting.execute('''
        CREATE TABLE IF NOT EXISTS yoya (
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        name_id TEXT,
        number_id TEXT
        )
    ''')
data_program.commit()
admin_id = ***
MIN_list = []
H_list = []
W_list = []
M_list = []
price_list = []
price_table = []
sel = sqlite3.connect(r"C:\Users\karino\Desktop\PROJECTS\file_1\data_base.db")
conn = sel.cursor()
TOKEN = "توکن خود را وارد کنید"
proxy_url = 'پروکسی خود را وارد کنید در صورت فیلترینگ تلگرام'
apihelper.proxy = {'https': proxy_url,'http': proxy_url}
bot = telebot.TeleBot(TOKEN)
kk_list = []
gg_list = []
async def deflection(context: ContextTypes.DEFAULT_TYPE):
    conn.execute("SELECT gold_name, price, time FROM ta LIMIT 116")
    UYT = conn.fetchall()
    list01 = ['طلا ۱۸','طلای 24 عیار','سکه','نیم سکه','ربع سکه','دلار','یورو','درهم امارات','پوند انگلیس','لیر ترکیه','فرانک سوئیس','یوان چین','ین ژاپن',
        'وون کره جنوبی','دلار کانادا','دلار استرالیا','دلار نیوزیلند','دلار سنگاپور','روپیه هند','روپیه پاکستان','دینار عراق','لیر سوریه','افغانی','کرون دانمارک',
        'کرون سوئد','کرون نروژ','ریال عربستان','ریال قطر','ریال عمان','دینار کویت','دینار بحرین','رینگیت مالزی','بات تایلند','دلار هنگ کنگ','روبل روسیه',
        'منات آذربایجان','درام ارمنستان','لاری گرجستان','سوم قرقیزستان','سامانی تاجیکستان','منات ترکمنستان','بیت کوین', 'اتریوم', 'لایت کوین',
        'بیت کوین کش', 'تتر', 'ترون', 'بایننس کوین', 'استلار', 'ریپل', 'دوج کوین', 'دش','کاردانو', 'پولکادات', 'سولانا', 'آوالانچ', 'شیبا اینو', 'تون\u200cکوین']
    save_data = context.job.data
    kk_list.append(save_data)
    if len(kk_list)==1:
        kk_list.remove(save_data)
        print(save_data)
        number = list01.index(save_data)
        name_one = UYT[number]
        name_two = UYT[number-58]
        print('--------------')
        print(name_one[0])
        print(name_two[0])
        print('--------------')
        if name_one[1]>name_two[1]:
            await context.bot.send_message(chat_id=context.job.chat_id, text=f"{save_data} افزایش یافت در تاریخ {name_one[2]}")
        elif name_one[1]<name_two[1]:
            await context.bot.send_message(chat_id=context.job.chat_id, text=f"{save_data} کاهش یافت در تاریخ {name_one[2]}")
async def analyzes_def(context: ContextTypes.DEFAULT_TYPE):
    save_data = context.job.data
    gg_list.append(save_data)
    if len(gg_list)==1:
        gg_list.remove(save_data)
        await context.bot.send_message(chat_id=context.job.chat_id, text=f"{save_data}")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    print(user_id)
    f_name = update.effective_user.first_name
    print(f_name)
    connecting.execute(
        "INSERT INTO yoya (name_id, number_id) VALUES (?,?)",
        (f_name,user_id)
    )
    if user_id==admin_id:
        keyboard_133=[[InlineKeyboardButton(text="دسترسی به پنل مدیریت", callback_data=f"99")]]
        reply = InlineKeyboardMarkup(keyboard_133)
        await context.bot.send_message(chat_id=update.effective_chat.id,text="شما ادمین هستید. میتوانید به پنل مدیریت دسترسی داشته باشید", reply_markup=reply)
    conn.execute("SELECT gold_name, price, time FROM ta LIMIT 43300")
    sdf = conn.fetchall()
    list01 = ['طلا ۱۸','طلای 24 عیار','سکه','نیم سکه','ربع سکه','دلار','یورو','درهم امارات','پوند انگلیس','لیر ترکیه','فرانک سوئیس','یوان چین','ین ژاپن',
        'وون کره جنوبی','دلار کانادا','دلار استرالیا','دلار نیوزیلند','دلار سنگاپور','روپیه هند','روپیه پاکستان','دینار عراق','لیر سوریه','افغانی','کرون دانمارک',
        'کرون سوئد','کرون نروژ','ریال عربستان','ریال قطر','ریال عمان','دینار کویت','دینار بحرین','رینگیت مالزی','بات تایلند','دلار هنگ کنگ','روبل روسیه',
        'منات آذربایجان','درام ارمنستان','لاری گرجستان','سوم قرقیزستان','سامانی تاجیکستان','منات ترکمنستان','بیت کوین', 'اتریوم', 'لایت کوین',
        'بیت کوین کش', 'تتر', 'ترون', 'بایننس کوین', 'استلار', 'ریپل', 'دوج کوین', 'دش','کاردانو', 'پولکادات', 'سولانا', 'آوالانچ', 'شیبا اینو', 'تون\u200cکوین']
    for item in list01:
        price_list = []
        MIN_list = []
        H_list = []
        W_list = []
        M_list = []
        for data in sdf:
            if data[0]==item:
                price_list.append(int(data[1].replace(',','')))
                timing = datetime.strptime(data[2], "%Y-%m-%d %H:%M:%S")
                MIN_list.append(timing.strftime("%H:%M"))
                H_list.append(timing.strftime("%H:%M"))
                W_list.append(timing.strftime("%d %H:%M"))
                M_list.append(timing.strftime("%d %H:%M"))
        ss = fr"C:\Users\karino\Desktop\PROJECTS\file_1\diagram"
        gg = os.path.join(ss,item)
        if not os.path.exists(gg):
            os.makedirs(gg)
        # نمودار یک ساعت اخیر
        fig, ax = plt.subplots()
        x_data1 = MIN_list[-60:]
        y_data1 = price_list[-60:]
        plt.title(item)
        ax.plot(x_data1,y_data1, 'b-')
        ss1 = x_data1[::6]
        ax.set_xticks(ss1) 
        ax.set_xticklabels(ss1, fontsize=7)
        plt.savefig(fr"C:\Users\karino\Desktop\PROJECTS\file_1\diagram\{item}\axis_MIN_{item}.jpg")
        plt.close()
        # نمودار یک روز اخیر
        fig, ax = plt.subplots()
        x_data2 = H_list[-1440:]
        y_data2 = price_list[-1440:]
        plt.title(item)
        ax.plot(x_data2,y_data2, 'b-')
        ss2 = x_data2[::144]
        ax.set_xticks(ss2)
        ax.set_xticklabels(ss2, fontsize=7)
        plt.savefig(fr"C:\Users\karino\Desktop\PROJECTS\file_1\diagram\{item}\axis_H_{item}.jpg")
        plt.close()
        #نمودار یک هفته اخیر
        fig, ax = plt.subplots()
        x_data3 = W_list[-10080:]
        y_data3 = price_list[-10080:]
        plt.title(item)
        ax.plot(x_data3,y_data3, 'b-')
        ss3 = x_data3[::1008]
        ax.set_xticks(ss3)
        ax.set_xticklabels(ss3, fontsize=7)
        plt.savefig(fr"C:\Users\karino\Desktop\PROJECTS\file_1\diagram\{item}\axis_W_{item}.jpg")
        plt.close()
        #نمودار یک ماه اخیر
        fig, ax = plt.subplots()
        x_data4 = M_list[-43200:]
        y_data4 = price_list[-43200:]
        plt.title(item)
        ax.plot(x_data4,y_data4, 'b-')
        ss4 = x_data4[::4320]
        ax.set_xticks(ss4)
        ax.set_xticklabels(ss4, fontsize=7)
        plt.savefig(fr"C:\Users\karino\Desktop\PROJECTS\file_1\diagram\{item}\axis_M_{item}.jpg")
        plt.close()
    keyboard = [[InlineKeyboardButton(text=f"داده های مالی", callback_data=f"77")]]
    reply = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id,text="سلام. خوش آمدید. قیمت، نمودار و تحلیل لحظه ای داده های مالی روز دنیا را تنها با چند کلیک میتوانید مشاهده کنید. لطفا روی گزینه موردنظر کلیک کنید", reply_markup=reply)
async def button0(update: Update, context: ContextTypes.DEFAULT_TYPE):
    list01 = ['قیمت طلا','قیمت ارز','قیمت رمز ارز']
    cv = OpenAI(
            base_url = "هوش مصنوعی خود را وارد کنید",
            api_key = "کلید هوش مصنوعی را وارد کنید"
        )
    mm = update.callback_query
    await mm.answer()
    data = mm.data
    keyboard11 = []
    if data.startswith("77"):
        for item in list01:
            kll = list01.index(item)
            button = [InlineKeyboardButton(text=f"{item}", callback_data=f"dee_{kll}"),InlineKeyboardButton(text=f"فعال سازی تحلیل روزانه AI", callback_data=f"xxi_{kll}")]
            keyboard11.append(button)
        reply = InlineKeyboardMarkup(keyboard11)
        await context.bot.send_message(chat_id=update.effective_chat.id,text="روی داده موردنظر کلیک کنید", reply_markup=reply)
    list02 = ['طلا ۱۸','طلای 24 عیار','سکه','نیم سکه','ربع سکه']
    list03 = ['دلار','یورو','درهم امارات','پوند انگلیس','لیر ترکیه','فرانک سوئیس','یوان چین','ین ژاپن','وون کره جنوبی','دلار کانادا',
              'دلار استرالیا','دلار نیوزیلند','دلار سنگاپور','روپیه هند','روپیه پاکستان','دینار عراق','لیر سوریه','افغانی','کرون دانمارک'
                ,'کرون سوئد','کرون نروژ','ریال عربستان','ریال قطر','ریال عمان','دینار کویت','دینار بحرین','رینگیت مالزی','بات تایلند',
                'دلار هنگ کنگ','روبل روسیه','منات آذربایجان','درام ارمنستان','لاری گرجستان','سوم قرقیزستان','سامانی تاجیکستان','منات ترکمنستان']
    list04 = ['بیت کوین', 'اتریوم', 'لایت کوین', 'بیت کوین کش', 'تتر', 'ترون', 'بایننس کوین', 'استلار', 'ریپل', 'دوج کوین', 'دش',
            'کاردانو', 'پولکادات', 'سولانا', 'آوالانچ', 'شیبا اینو', 'تون\u200cکوین']
    box = ["یک ساعت گذشته","یک روز گذشته","یک هفته گذشته","یک ماه گذشته"]
    lim_list = ["MIN","H","W","M"]
    keyboard12 = []
    if data.startswith("dee_"):
        cb = int(data.split("_")[1])
        if cb==0:
            for data_ll in list02: 
                kll = list02.index(data_ll)
                button = [InlineKeyboardButton(text=f"{data_ll}", callback_data=f"ree_{kll}")]
                keyboard12.append(button)
            reply = InlineKeyboardMarkup(keyboard12)
            await context.bot.send_message(chat_id=update.effective_chat.id,text="یکی از داده های مربوط به قیمت طلا را انتخاب کنید", reply_markup=reply)
        elif cb==1:
            for data_ll in list03:
                kll = list03.index(data_ll)
                button = [InlineKeyboardButton(text=f"{data_ll}", callback_data=f"show_{kll}")]
                keyboard12.append(button)
            reply = InlineKeyboardMarkup(keyboard12)
            await context.bot.send_message(chat_id=update.effective_chat.id,text="یکی از داده های مربوط به قیمت ارز را انتخاب کنید", reply_markup=reply)
        else:
            if cb==2:
                for data_ll in list04:
                    kll = list04.index(data_ll) 
                    button = [InlineKeyboardButton(text=f"{data_ll}", callback_data=f"mee_{kll}")]
                    keyboard12.append(button)
                reply = InlineKeyboardMarkup(keyboard12)
                await context.bot.send_message(chat_id=update.effective_chat.id,text="یکی از داده های مربوط به قیمت رمز ارز را انتخاب کنید", reply_markup=reply) 
    if data.startswith("ree_"):
        cb = int(data.split("_")[1])
        data_lll = list02[cb]
        kll = list02.index(data_lll)
        keyboard12.append([InlineKeyboardButton(text=f"فعال سازی نوتفیکیشن هشدار {data_lll}", callback_data=f"aaee_{kll}")])
        for h in box:
            cm = int(box.index(h))
            button = [InlineKeyboardButton(text=f"نمودار {h}", callback_data=f"gee_{kll}_{cm}"),InlineKeyboardButton(text=f"تحلیل {h}", callback_data=f"kee_{kll}_{cm}")]
            keyboard12.append(button)
        reply = InlineKeyboardMarkup(keyboard12)
        conn.execute("SELECT gold_name, price, time FROM ta LIMIT 58")
        sdf = conn.fetchall()
        for ft in sdf:
            if ft[0]==data_lll:
                await context.bot.send_message(chat_id=update.effective_chat.id,text=f"قیمت {data_lll} {ft[1]} ریال است. یکی از گزینه های زیر را برای {data_lll} انتخاب کنید", reply_markup=reply)
    if data.startswith("show_"):
        cb = int(data.split("_")[1])
        data_lll = list03[cb]
        kll = list03.index(data_lll)
        keyboard12.append([InlineKeyboardButton(text=f"فعال سازی نوتفیکیشن هشدار {data_lll}", callback_data=f"ssee_{kll}")])
        for h in box:
            cm = int(box.index(h))
            button = [InlineKeyboardButton(text=f"نمودار {h}", callback_data=f"nee_{kll}_{cm}"),InlineKeyboardButton(text=f"تحلیل {h}", callback_data=f"uee_{kll}_{cm}")]
            keyboard12.append(button)
        reply = InlineKeyboardMarkup(keyboard12)
        conn.execute("SELECT gold_name, price, time FROM ta LIMIT 58")
        sdf = conn.fetchall()
        for ft in sdf:
            if ft[0]==data_lll:
                await context.bot.send_message(chat_id=update.effective_chat.id,text=f"قیمت {data_lll} {ft[1]} ریال است. یکی از گزینه های زیر را برای {data_lll} انتخاب کنید", reply_markup=reply)
    if data.startswith("mee_"):
        cb = int(data.split("_")[1])
        data_lll = list04[cb]
        kll = list04.index(data_lll)
        keyboard12.append([InlineKeyboardButton(text=f"فعال سازی نوتفیکیشن هشدار {data_lll}", callback_data=f"hhee_{kll}")])
        for h in box:
            cm = int(box.index(h))
            button = [InlineKeyboardButton(text=f"نمودار {h}", callback_data=f"vee_{kll}_{cm}"),InlineKeyboardButton(text=f"تحلیل {h}", callback_data=f"cee_{kll}_{cm}")]
            keyboard12.append(button)
        reply = InlineKeyboardMarkup(keyboard12)
        conn.execute("SELECT gold_name, price, time FROM ta LIMIT 58")
        sdf = conn.fetchall()
        for ft in sdf:
            if ft[0]==data_lll:
                await context.bot.send_message(chat_id=update.effective_chat.id,text=f"قیمت {data_lll} {ft[1]} ریال است. یکی از گزینه های زیر را برای {data_lll} انتخاب کنید", reply_markup=reply)
    if data.startswith("gee_"):
        cb = int(data.split("_")[1])
        cd = int(data.split("_")[2])
        data_lll = list02[cb]
        select00 = lim_list[cd]
        select000 = box[cd]
        if select000 in box:
            with open(fr"C:\Users\karino\Desktop\PROJECTS\file_1\diagram\{data_lll}\axis_{select00}_{data_lll}.jpg", 'rb') as photo_file:
                await mm.message.reply_photo(
                    photo=photo_file,caption=f"نمودار {data_lll} در {select000}"
                )
    elif data.startswith("kee_"):
        cb = int(data.split("_")[1])
        cd = int(data.split("_")[2])
        data_lll = list02[cb]
        select = lim_list[cd]
        time = box[cd]
        with open(fr"C:\Users\karino\Desktop\PROJECTS\file_1\diagram\{data_lll}\axis_{select}_{data_lll}.jpg", 'rb') as photo_file:
            sentence = f"{photo_file} این تصویر، نمودار قیمت {data_lll} را در {time} نمایش میدهد. لطفا این نمودار را باتوجه به شرایط تجاری و سیاسی موجود تحلیل کن . در حد چهار خط"
            responce = cv.chat.completions.create( 
                model = "مدل هوش مصنوعی خود را وارد کنید", 
                messages=[{"role":"user", "content":sentence}] 
            )
            ai_answer = responce.choices[0].message.content
            await context.bot.send_message(chat_id=update.effective_chat.id, text=ai_answer)
    if data.startswith("nee_"):
        cb = int(data.split("_")[1])
        cd = int(data.split("_")[2])
        data_lll = list03[cb]
        select00 = lim_list[cd]
        select000 = box[cd]
        if select000 in box:
            with open(fr"C:\Users\karino\Desktop\PROJECTS\file_1\diagram\{data_lll}\axis_{select00}_{data_lll}.jpg", 'rb') as photo_file:
                await mm.message.reply_photo(
                    photo=photo_file,caption=f"نمودار {data_lll} در {select000}"
                )
    elif data.startswith("uee_"):
        cb = int(data.split("_")[1])
        cd = int(data.split("_")[2])
        data_lll = list03[cb]
        select = lim_list[cd]
        time = box[cd]
        with open(fr"C:\Users\karino\Desktop\PROJECTS\file_1\diagram\{data_lll}\axis_{select}_{data_lll}.jpg", 'rb') as photo_file:
            sentence = f"{photo_file} این تصویر، نمودار قیمت {data_lll} را در {time} نمایش میدهد. لطفا این نمودار را باتوجه به شرایط تجاری و سیاسی موجود تحلیل کن. در حد چهار خط"
            responce = cv.chat.completions.create( 
                model = "مدل هوش مصنوعی خود را وارد کنید", 
                messages=[{"role":"user", "content":sentence}] 
            )
            ai_answer = responce.choices[0].message.content
            await context.bot.send_message(chat_id=update.effective_chat.id, text=ai_answer)
    if data.startswith("vee_"):
        cb = int(data.split("_")[1])
        cd = int(data.split("_")[2])
        data_lll = list04[cb]
        select00 = lim_list[cd]
        select000 = box[cd]
        if select000 in box:
            with open(fr"C:\Users\karino\Desktop\PROJECTS\file_1\diagram\{data_lll}\axis_{select00}_{data_lll}.jpg", 'rb') as photo_file:
                await mm.message.reply_photo(
                    photo=photo_file,caption=f"نمودار {data_lll} در {select000}"
                )
    elif data.startswith("cee_"):
        cb = int(data.split("_")[1])
        cd = int(data.split("_")[2])
        data_lll = list04[cb]
        select = lim_list[cd]
        time = box[cd]
        with open(fr"C:\Users\karino\Desktop\PROJECTS\file_1\diagram\{data_lll}\axis_{select}_{data_lll}.jpg", 'rb') as photo_file:
            sentence = f"{photo_file} این تصویر، نمودار قیمت {data_lll} را در {time} نمایش میدهد. لطفا این نمودار را باتوجه به شرایط تجاری و سیاسی موجود تحلیل کن. در حد چهار خط"
            responce = cv.chat.completions.create( 
                model = "مدل هوش مصنوعی خود را وارد کنید", 
                messages=[{"role":"user", "content":sentence}] 
            )
            ai_answer = responce.choices[0].message.content
            await context.bot.send_message(chat_id=update.effective_chat.id, text=ai_answer)
    if data.startswith("aaee_"):
        cb = int(data.split("_")[1])
        name_data = list02[cb]
        context.job_queue.run_repeating(
            callback=deflection,
            interval = 60,
            first = 2,
            chat_id = update.effective_chat.id,
            data = name_data,
        )
    elif data.startswith("ssee_"):
        cb = int(data.split("_")[1])
        name_data = list03[cb]
        context.job_queue.run_repeating(
            callback=deflection,
            interval = 60,
            first = 2,
            chat_id = update.effective_chat.id,
            data = name_data,
        )
    else:
        if data.startswith("hhee_"):
            cb = int(data.split("_")[1])
            name_data = list04[cb]
            context.job_queue.run_repeating(
                callback=deflection,
                interval = 60,
                first = 2,
                chat_id = update.effective_chat.id,
                data = name_data,
            )
    if data.startswith("xxi_"):
        cb = int(data.split("_")[1])
        data_lll = list01[cb]
        sentense = f"لطفا بازار {data_lll} در 24 ساعت گذشته در ایران رو باتوجه به شرایط اقتصادی و سیاسی تحلیل کن"
        responce = cv.chat.completions.create(
            model="مدل هوش مصنوعی خود را وارد کنید",
            messages=[{"role":"user", "content":sentense}] 
        )
        ai_answer = responce.choices[0].message.content
        context.job_queue.run_repeating(
            callback=analyzes_def,
            interval = 86400,
            first = 2,
            chat_id = update.effective_chat.id,
            data = ai_answer,
        )
    if data.startswith("99"):
        keyboard_133 = []
        keyboard_133.append([InlineKeyboardButton(text="ارسال پیام به تمام اعضا", callback_data=f"111")])
        keyboard_133.append([InlineKeyboardButton(text="بن کردن اعضا", callback_data=f"222")])
        keyboard_133.append([InlineKeyboardButton(text="مشاهده تعداد اعضا و آیدی اعضا", callback_data=f"333")])
        reply = InlineKeyboardMarkup(keyboard_133)
        await context.bot.send_message(chat_id=update.effective_chat.id,text="لطفا گزینه موردنظر را جهت اقدام کلیک کنید", reply_markup=reply)
    if data.startswith("111"):
        await context.bot.send_message(chat_id=admin_id, text="لطفا پیام، عکس یا فایلی که میخواهید برای همه اعضا فرستاده شود را بنویسید")
async def button1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    photo = update.message.photo
    document = update.message.document
    if text:
        connecting.execute("SELECT number_id FROM yoya")
        all_id = connecting.fetchall()
        print(all_id)
        for id in all_id:
            print(int(id[0]))
            if int(id[0])!=admin_id:
                print()
                await context.bot.send_message(chat_id=int(id[0]), text=text)
    elif photo:
        photo = update.message.photo[-1].file_id
        connecting.execute("SELECT number_id FROM yoya")
        all_id = connecting.fetchall()
        print(all_id)
        for id in all_id:
            print(int(id[0]))
            if int(id[0])!=admin_id:
                print()
                await context.bot.send_photo(chat_id=int(id[0]), photo=photo)
    else:
        if document:
            document = update.message.document.file_id
            connecting.execute("SELECT number_id FROM yoya")
            all_id = connecting.fetchall()
            print(all_id)
            for id in all_id:
                print(int(id[0]))
                if int(id[0])!=admin_id:
                    print()
                    await context.bot.send_document(chat_id=int(id[0]), document=document)
    await context.bot.send_message(chat_id=admin_id, text="پیام برای همه اعضا با موفقیت ارسال شد")
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button0))
    app.add_handler(MessageHandler(filters.TEXT | filters.PHOTO | filters.Document.ALL & ~ filters.COMMAND, button1))
    print('yes')
    app.run_polling()
