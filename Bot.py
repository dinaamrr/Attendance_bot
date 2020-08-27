from Rivescript import RiveScript
import re
import xlwt
import os.path
file = os.path.dirname(__file__)
book = xlwt.Workbook()
sheet = book.add_sheet("attendance sheet")
Brain = os.path.join(file, 'Brain')
row = 0
col = 0
while True:
 Bot = RiveScript()
 Bot.load_directory(Brain)
 Bot.sort_replies()
 trigger= str(input('you> '))
 while True :
    if Bot.reply('localuser', trigger) == 'impressive and what is your name?':
        print ('Bot>'+Bot.reply('localuser', trigger))
        name = str(input('you> '))
        trigger = name
        name = name.replace('my name is','')
    elif Bot.reply('localuser', trigger) == 'that is all thank you':
        sheet.write(row,col,name)
        sheet.write(row,col+1,trigger)
        book.save("attendance.xls")
        row=row+1
        print ('Bot>'+Bot.reply('localuser', trigger))
        break
    else:
        print ('Bot>'+Bot.reply('localuser', trigger))
        trigger= str(input('you> '))
