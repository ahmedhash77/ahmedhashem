class log_in():
 re = 0
 dic={"ahmed hashem":336369225258,"hassan":123456,"kh":123456789}
 @staticmethod
 def passwo(username):
    re=log_in.re
    password = int(input("input password"))
    if password == log_in.dic[username]:
        print("you are accessed")
    else:
        print("password is wrong inter in again")
        re=re+1
        log_in.re=re
        print("you have 4 retration this is retration number",log_in.re)
        if re == 4:
          print("you are not the person")
          quit()
        else:
          log_in.passwo(username)
 @staticmethod
 def usen():
  dic=log_in.dic
  username=""
  username+= input("input user name")
  if username in dic.keys():
    log_in.passwo(username)
  else:
      print("your user name is incorrect")
facebook=log_in()
facebook.usen()
