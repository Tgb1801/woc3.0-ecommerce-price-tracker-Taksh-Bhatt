import json
import datetime
import time
import Amazon_scrap
import Flipkart_scrap
import ebay_scrap
import os
import smtplib

Sender_email = "___Your email Id goes here___"    

Email_Pass = "___The password goes here___"

# Stored_Time.json file will store the time when to run the script next
with open('Stored_Time.json', 'r') as json_file:
    data = json.load(json_file)

date_time_obj = datetime.datetime.strptime(data['time'], '%Y-%m-%d %H:%M:%S.%f')

run = True

if datetime.datetime.now() < date_time_obj:
    run = False

choice = int(input("Enter 1 to run the script or 2 to enter the data: "))

if choice == 2:

    run = True
    ch = int(input("Enter your choice [1] Amazon [2] Flipkart [3] ebay: "))
    url = input("Enter the product url: ")
    price_req = float(input("Enter the desired price: "))
    email_id = input("Enter your E-mail Id: ")

    if ch == 1:
        product_name = Amaze_scrap.get_product_name_from_amaze(url)
    elif ch == 2:
        product_name = Flip_scrap.get_product_name_from_flip(url)
    else:
        product_name = eba_scrap.get_product_name_from_eba(url)

    # Read from the file
    try:
        # with open('Details.json', 'r') as json_file:
        #    data = json.load(json_file)
        data = []
        dict1 = {'website': ch, 'url': url, 'product_name': product_name, 'Email_Id': email_id, 'desired_price': price_req}

        data.append(dict1)

        # Write to the file
        with open('Details.json', 'w') as json_file:
            json.dump(data, json_file)

    except Exception:
        data = []
        dict1 = {'website': ch, 'url': url, 'product_name': product_name, 'Email_Id': email_id, 'desired_price': price_req}
        data.append(dict1)

        # Write to the file
        with open('Details.json', 'w') as json_file:
            json.dump(data, json_file)

while 1:
    if run:

        try:
            # Read from the file
            with open('Details.json', 'r') as json_file:
                data = json.load(json_file)

            f = 0

            # Run the loop here
            for i in range(len(data)):
                f = 1
                url = data[i]['url']
                website = data[i]['website']

                if website == 1:  # Amazon
                    price = Amaze_scrap.get_product_price_from_amaze(url)
                elif website == 2:  # Flipkart
                    price = Flip_scrap.get_product_price_from_flip(url)
                else:  # ebay
                    price = eba_scrap.get_product_price_from_eba(url)

                num_str = ""

                for j in range(len(price)):
                    if (price[j] >= '0' and price[j] <= '9') or price[j] == '.':
                        num_str += price[j]

                p_price = float(num_str)
                # print(p_price)

                # Send email here
                if p_price <= data[i]['desired_price']:

                    site_name = ''
                    if website == 1:
                        site_name = 'Amazon'
                    elif website == 2:
                        site_name = 'Flipkart'
                    else:
                        site_name = 'ebay'

                    pro_name = data[i]['product_name']

                    receiver_email = data[i]['Email_Id']

                    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()

                        smtp.login(Sender_email, Email_Pass)

                        subject = 'Product available within your desired price.'

                        body = f'Dear user,\n\nWe found that {site_name} is providing the following product that you desired ' \
                               f'within your desired price range. The information of the product is given below:\n\n' \
                               f'Product Name: {pro_name}\nProduct Price: {price}\nURL: {url}\n\n' \
                               f'Regards,\nFlibazon Price Tracker.'

                        msg = f'Subject: {subject}\n\n{body}'

                        # Format of sending email ---> smtp.sendmail(SENDER, RECEIVER, message)
                        smtp.sendmail(Sender_email, receiver_email, msg.encode('utf8'))

                    data.pop(i)
                    i -= 1
                    with open('Details.json', 'w') as file:
                        json.dump(data, file)

            # The iteration through data structure ends here
            new_run_time = datetime.datetime.now() + datetime.timedelta(hours=12)

            dict1 = {'time': str(new_run_time)}

            with open('Stored_Time.json', 'w') as file:
                json.dump(dict1, file)

            if f == 0:
                quit()

            # Waits till 12 hours
            time.sleep(12*3600)

        except Exception as e:
            print(e)
            quit()

    else:
        run = True
        diff = 3600*abs(date_time_obj.hour - datetime.datetime.now().hour)
        if date_time_obj.minute > datetime.datetime.now().minute:
            diff += 60*(date_time_obj.minute - datetime.datetime.now().minute)
        else:
            diff -= 60*(datetime.datetime.now().minute - date_time_obj.minute)

        time.sleep(diff)
