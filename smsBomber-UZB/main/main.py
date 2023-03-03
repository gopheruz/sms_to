from send_script import startBomb

def sendSms():


    counter = 500
    phone = "+998330036668"
    if(len(phone) != 13 or phone.startswith("+")is not True): 
        print("Incorrect number!")
        return
    startBomb(phone, int(counter))
    
def main():
    sendSms()

if __name__ == "__main__":
    main()

