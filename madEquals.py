import os
import urllib
import re
import datetime

currencies=["eur","usd","gbp","aud","cad","chf"]
currenciesLongName={currencies[0]:"Euro",
                    currencies[1]:"US Dollar",
                    currencies[2]:"British Pound",
                    currencies[3]:"Australian Dollar",
                    currencies[4]:"Canadian Dollar",
                    currencies[5]:"Swiss Franc"}

regex='<b>(.+?)</b>'
pattern=re.compile(regex)

now = datetime.datetime.now()
now = now.strftime('%d/%m/%Y  %H:%M:%S')

memo = open("memo.txt","a")
memo.write("Date : "+now+"\n")

i=0
while i<len(currencies):
    siteurl="http://themoneyconverter.com/"+ currencies[i] +"/MAD.aspx"
    htmlfile=urllib.urlopen(siteurl)
    htmltext=htmlfile.read()

    madvalue=re.findall(pattern, htmltext)
    if madvalue :
        result = currencies[i] + " = "+madvalue[-1]+"Dirham(s). "+"("+currenciesLongName[currencies[i]]+")"
    else:
        result = "Pas d'infos pour"+currenciesLongName.value[i]

    print result
    memo.write(result+"\n")

    i+=1

memo.write("\n---\n\n")
memo.close()

os.system("pause")
