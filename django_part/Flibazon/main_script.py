
import datetime
import time
from Flibazon import Amaze_scrap
from Flibazon import Flip_scrap
from Flibazon import eba_scrap
import os
import smtplib
from .models import User_Details
from .models import next_run_time


def run_main_script():
    sender_email = "___Your email Id goes here___"

    email_pass = "___The password goes here___"

    # print("TIME:", next_run_time.objects.get(id=1).time)

    run_script = True

    date_time_obj = next_run_time.objects.get(id=1)

    now_time = str(datetime.datetime.now())
    next_time = str(date_time_obj.time)

    if now_time < next_time:
        run_script = False

    while 1:
        if run_script:
            print("\nRUNNING THE SCRIPT..\n")
            try:

                details = User_Details.objects.all()

                # Run the loop here
                for detail in details:

                    url = detail.url
                    website = detail.website

                    price = ""

                    if website == 1:  # Amazon
                        price += Amaze_scrap.get_product_price_from_amaze(url)
                    elif website == 2:  # Flipkart
                        price += Flip_scrap.get_product_price_from_flip(url)
                    elif website == 3:  # ebay
                        price += eba_scrap.get_product_price_from_eba(url)

                    num_str = ""

                    for j in range(len(price)):
                        if (price[j] >= '0' and price[j] <= '9') or price[j] == '.':
                            num_str += price[j]

                    p_price = float(num_str)
                    # print(p_price)

                    # Send email here
                    if p_price <= detail.desired_price:

                        site_name = ''
                        if website == 1:
                            site_name = 'Amazon'
                        elif website == 2:
                            site_name = 'Flipkart'
                        else:
                            site_name = 'ebay'

                        pro_name = detail.product_name

                        receiver_email = detail.Email_Id

                        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                            print("\nSENDING MAIL...\n")
                            smtp.ehlo()
                            smtp.starttls()
                            smtp.ehlo()

                            smtp.login(sender_email, email_pass)

                            subject = 'Product available within your desired price.'

                            body = f'Dear user,\n\nWe found that {site_name} is providing the following product that you desired ' \
                                   f'within your desired price range. The information of the product is given below:\n\n' \
                                   f'Product Name: {pro_name}\nProduct Price: {price}\nURL: {url}\n\n' \
                                   f'Regards,\nFlibazon Price Tracker.'

                            msg = f'Subject: {subject}\n\n{body}'

                            # Format of sending email ---> smtp.sendmail(SENDER, RECEIVER, message)
                            smtp.sendmail(sender_email, receiver_email, msg.encode('utf8'))

                        detail.delete()

                # The iteration through data structure ends here
                # Stores the next running time i.e. after 10 seconds.
                new_run_time = datetime.datetime.now() + datetime.timedelta(seconds=10)

                date_time_obj.time = new_run_time

                # Saves new time in the database
                date_time_obj.save()

                # Waits till 10 seconds
                time.sleep(10)

            except Exception as e:
                print("EXCEPTION OCCURRED: ", e)
                quit()

        else:
            run_script = True
            date_time_str = str(date_time_obj.time)
            date_time_str = date_time_str[:-6]
            date_time_obj2 = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

            diff = date_time_obj2 - datetime.datetime.now()
            total_secs = diff.total_seconds()
            time.sleep(total_secs)
