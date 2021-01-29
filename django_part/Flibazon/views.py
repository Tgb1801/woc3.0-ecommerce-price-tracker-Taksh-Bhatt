from django.shortcuts import render
import Flibazon.Amaze_scrap as Amaze
import Flibazon.eba_scrap as eba
import Flibazon.Flip_scrap as Flip
from .models import User_Details

# Create your views here.


def home(request):
    return render(request, 'home.html')


def get_info(request):

    # Here, to get the data from the website we use POST method
    # And to send the data to the website we use GET method.

    # Also using POST method no information is seen on the address bar of the website, so that nobody can see it.

    website = int(request.POST['website'])
    url = request.POST['url']
    desired_price = float(request.POST['price'])
    email = request.POST['email_Id']

    product_name = ""
    product_price = ""

    if website == 1:    # Amazon
        product_name += Amaze.get_product_name_from_amaze(url)
        product_price += Amaze.get_product_price_from_amaze(url)
    elif website == 2:  # Flipkart
        product_name += Flip.get_product_name_from_flip(url)
        product_price += Flip.get_product_price_from_flip(url)
    elif website == 3:  # ebay
        product_name += eba.get_product_name_from_eba(url)
        product_price += eba.get_product_price_from_eba(url)

    User_Details.objects.create(website=website, url=url, product_name=product_name, Email_Id=email, desired_price=desired_price)

    return render(request, 'result.html', {'name': product_name, 'price': product_price})
