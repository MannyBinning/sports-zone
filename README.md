# Table of Contents

- [Description](#description)
- [UX](#ux)
- [User Stories](#user-stories)
- [Database](#database)
- [Wireframes](#wireframes)
- [Deployment](#deployment)
- [Views and Features](#views-and-features)
- [Technologies and Tools Used](#technologies-and-tools-used)
- [Testing](#testing)
- [Acknowledgements](#acknowledgements)


# Description
[Sports Zone](https://sports-zone-manny.herokuapp.com/) has been created to be a fictional e-commerce website. The main purpose of the website is to sell various sports products to individuals of all ages and sexualities. ‘Sports Zone’ specialises in two particular sports, football and cricket. The range of products is extremely diverse as the website sells items such as clothing to specialised equipment. 

# UX
The ‘Welcome page’ has been designed to make users easily aware of what type of products ‘Sports Zone’ distribute. To achieve this objective, a relevant background has been included to make it clear to all individuals what this website entails. Additionally, a ‘shop now’ button has been placed in the middle of the screen to establish an easily accessible way for the user to browse all products.

Brand awareness is a key feature for ‘Sports Zone’. To obtain this aspiration, the company logo has been placed in the same position throughout the website. This encourages the user to recognise the brand if ever seen elsewhere. 
 
A navigation bar and search bar has been placed on every page of the website. This has been created to provide a simple way for users to browse the website without any complications. Likewise, a shopping bag link and profile link has also been added to every page, to make it apparent to all users.

The ‘shop now’ button displayed on the ‘welcome page’ is designed to convey users to the ‘All Products’ page. This page has all the products listed from both the cricket and football range. All users also have access to this specific page via the navigation bar displayed at the top of each page.
 
Consistency is a key feature throughout the website. To achieve this feature, the navigation bar and logo on the ‘All Products’ page is displayed in the same position as the ‘Welcome Page’. To help give users a visual representation of each product, an image has been advertised alongside the name of the product, price, category and rating. Once selecting the image of each product, the page will be redirected to the selected products detail page. This page will give users a detailed description of the product and an option to select the quantity or (if required) the size of the product they wish to buy. After choosing their required options, the user has an opportunity to add the product to their shopping bag by selecting ‘add to bag’. As the product has been added to the bag, it will be included in the shopping bag aspect that is displayed on the top right of the screen. A pop-up feature will also be displayed to the users indicating the product has been added successfully or if unable to add or any reason, an appropriate message will be dispayed. 
 
The shopping bag link has been established to ensure users can view the products that they are intending to buy alongside the total price and quantity/size of each product. If the user wishes to update the quantity or remove the product from the shopping bag, then there are link options available to do so. To accommodate all individuals buying from ‘sports zone’, there is a total feature within the shopping bag that includes delivery cost.

To complete the purchase, a link at the bottom of the ‘shopping bag’ page is provided named ‘secure checkout’. Once selected, the page will lead the user to a designed check out page where the user will need to add their details, delivery address and payment details. If the user fails to complete a necessary field, the user will not be able to complete the order and will be requested to add the necessary information. 
 
All users are granted access to register and create their account with ‘Sports Zone’. To register or login into an account, the user will need to select the ‘my account’ feature which is displayed on every page on the website. Once an account is created, the user is provided with a profile page that will display personal details and all previous and current purchases with ‘Sports Zone’.
 
If the user is also an admin and logged in as an admin then they will have access to conduct any works that are needed for the website. Those works could be adding new products to the website or changing specific pricing for products.

<div align="right"><p style="text-align: right"><a href="#table-of-contents">Back to top</a></p></div>

# User Stories
- ### As a Site User/Customer, I would like to:
    - Understand the range of products available for purchase.
    - Efficiently navigate through the site for browsing purposes.
    - Be able to have different categories to ease my way through the site
    - Be able to specifically search products I am interested in. 
    - View the products listed. 
    - Learn more about the product's specification in detail. 
    - Rearrange the products to have the ones I am interested in towards the top. 
    - View the items and the in shopping bag.
    - Update my basket without having to leave the shopping bag. 
    - View the individual and total cost of all products in the bag, including delivery cost. 
    - Securely checkout to purchase the items required. 
    - Have my details stored for future orders.
    - View the history of the products, I have purchased previously. 
    - Be able to log in and out of the site. 

- ### As an admin, I would like to:
    - Have access to add products with full details.
    - Have access to updated products where needed. 
    - Update images if required. 
    - Have access to remove products or users if needed. 

- ### To achieve the above targets, I have added:
    - A Landing Page and Logo determining the meaning and purpose of the site. 
    - A Navigation bar using bootstrap to guide the user through the site. 
    - Various categories so the user can be lead in the right direction efficiently.
    - A search bar for the user to explore a specific product in mind.
    - Products page, where the user can view all the project in a selected category.
    - Product detail page, where the user can find the product information. 
    - Select Menu for the user to select the order they would like to arrange the list in. 
    - Shopping bag, where the user can add products ready to be purchased. 
    - Cost section, where the user can view the total cost, sub-total for a specific product and delivery cost if required. 
    - Secure Checkout page, where the user can add their details securely to checkout and purchase the products. 
    - Profile page, where the details are saved for the user for future purchases.
    - Profile page, where the user can check their order history. 
    - Dropdown menu with options to log in if not already and log out once logged in. 
    - Added product management in the dropdown menu for admin to add new products. 
    - Added edit and remove buttons for the admin to update details or remove the product. 
    - Added an upload images function in the update and add products section. 

<div align="right"><p style="text-align: right"><a href="#table-of-contents">Back to top</a></p></div>

# Database
Data Structure was pre-planned for this project, so the categories can be stored including the products linked to individual categories and all the product details. Besides this the user profile details will be stored including the orders they have made: 

<p align="center">Database</p>
<p align="center">
  <img src="static/images/database4.jpg" alt="Database" width="600"/>
</p>

This website has been created to sell products for Men, Women, Kids and Accessories for all, therefore, I have created categories that will contain the products for each gender and age. These four categories have been separated into two styles such as clothing categories and equipment categories. These categories consist of storage for the id, name and friendly name. 

Given the categories, I had to work on the products that will be allocated to these categories. As mentioned above there are two types of products, clothing and equipment. These products consist of storage for the id, SKU, name, description, the category they are allocated to, has_sizes if they are in clothing categories, price, image_url, image.

Once the user adds a product to the shopping bag there is an order line, where the product details are brought in from the storage. The details brought in are the Order, Product, Product Size if chosen, Quantity and Total.

This website has given the user to create their profile where they can save the details attracting user to visit back to make further orders with ease. To achieve this the user id, user, full name, the full address is stored. These details are requested when the user visits the profile page and also can be amended there if needed. 

Another this visible on the profile page is the order history where all the order details are brought in. These details are also brought in when the purchase is completed to show the user full details of the order. Items stored in this scenario are order number, order date, order items, full name, phone number, full address, order total, delivery cost and the total. 

<div align="right"><p style="text-align: right"><a href="#table-of-contents">Back to top</a></p></div>

# Wireframes

- Wireframes were made at the start of the project to create a specific framework for this website. 
### **Wireframe Screenshots:**
<p align="center">Home Page Wireframe</p>
<p align="center">
  <img src="static/images/Home.png" alt="Home-Page wireframe" width="600"/>
</p>
<p align="center">Prodcuts Page Wireframe</p>
<p align="center">
  <img src="static/images/Products.png" alt="Prodcuts-Page wireframe" width="600"/>
</p>
<p align="center">Product Details Page Wireframe</p>
<p align="center">
  <img src="static/images/ProductDetails.png" alt="Product Details wireframe" width="600"/>
</p>
<p align="center">Product Management Wireframe</p>
<p align="center">
  <img src="static/images/ProductManagement.png" alt="Product Management wireframe" width="600"/>
</p>
<p align="center">Profile Page Wireframe</p>
<p align="center">
  <img src="static/images/Profile.png" alt="Profile Page wireframe" width="600"/>
</p>
<p align="center">Shopping Bag Page Wireframe</p>
<p align="center">
  <img src="static/images/ShoppingBag.png" alt="Shopping Bag Page wireframe" width="600"/>
</p>
<p align="center">Checkout Page Wireframe</p>
<p align="center">
  <img src="static/images/Checkout.png" alt="Checkout Page wireframe" width="600"/>
</p>
<p align="center">Order Confirmation Page Wireframe</p>
<p align="center">
  <img src="static/images/Confirmation.png" alt="Order Confirmation Page wireframe" width="600"/>
</p>
<p align="center">Register Page Wireframe</p>
<p align="center">
  <img src="static/images/Register.png" alt="Sign Up Page wireframe" width="600"/>
</p>
<p align="center">Sign In Page Wireframe</p>
<p align="center">
  <img src="static/images/Signin.png" alt="Sign In Page wireframe" width="600"/>
</p>

<div align="right"><p style="text-align: right"><a href="#table-of-contents">Back to top</a></p></div>

# Views and Features

# Deployment
### Github Deployment
To deploy the project on Github, I created a repository called "sports-zone" and included the Code Institute template.
As I was using gitpod, throughout the project journey, I updated the variables in Gitpod Settings such as:
  - SECRET_KEY = "YOUR_DJANGO_SECRET_KEY"
  - STRIPE_PUBLIC_KEY = "YOUR_STRIPE_PUBLIC_KEY"
  - STRIPE_SECRET_KEY = "YOUR_STRIPE_SECRET_KEY"
  - STRIPE_WH_SECRET = "YOUR_STRIPE_WEBHOOK_SECRET"
  - DEVELOPMENT = "True"

To help acheive the target of this website there were various packages installed through out the project:
  - Django 
  - Django AllAuth 
  - Pillow 
  - Django Crispy Forms
  - Stripe
  - Django Countries
  - DJ Database URL
  - Psycopg2
  - Gunicorn
  - Boto3
  - Django Storages
Every time an installation was done, it was stored into requirements.txt file. 

To start the project with django, django-admin startproject was used which created many useful apps for this project. 

When the changes were made for updating purpose in the project, the migrations were done using following steps:
  - python3 manage.py makemigrations --dry-run
  - python3 manage.py makemigrations
  - python3 manage.py migrate --plan
  - python3 manage.py migrate

To load the data created in json files following commads were used: 
  - python3 manage.py loaddata products
  - python3 manage.py loaddata categoriess

Django has a built-in admin feature to aurthorise superusers to log in ammend the products by updating, adding or removing them and to acheive this I used:
  - python3 manage.py createsuperuser

In this project I also used a system known as Amazon S3 Bucket, where I created a bucked named 'sports-zone'. Once the bucket was created I enabled it for public access and enable the website to host static files. Following the steps from Boutique Ado Mini Project, I also added CORD config. To create the bucket I selected a S3 policy which then provided me with an ARN number. 
Once Bucket was set up I created a user in IAM. To run this successfully I attached a pre-built policy named amazonS3FullAccess. Once created, I attached this policy to the group created. 
Once the group was created I added User to hold the static files granting it progromatic access. Once all done, I was provided with the Access Key ID and Secret Access Key. Which were then added to Heroku Variables. 

Once the S3 bucket was created, I connected Django to the bucket and to acheieve that boto3 and django storages were installed. After this the variables were added tho the settings file so they can only be called when the value is True in the Heroku Environment. 
AWS_STORAGE_BUCKET_NAME
AWS_S3_REGION_NAME
AWS_S3_CUSTOM_DOMAIN

### Deploying to Heroku 
To deploy this project to heroku procedure explained below was followed: 
  - To begin with an app called 'sports-zone-manny' was created on Heroku.
  - Via "heroku login -i" in the command line I logged in to Heroku.  
  - To use Postgres I installed "dj_database_url" and "psycopg2-binary" ensuring Heroku will install all the app requirements when deployed.
  - In settings file I added the database URL from Heroku, which can be found in config variables in app settings tab.  
  - Once this wasd achieved I ran migrations and loaded the categories and products. 
  - Then I took out the database url to stop it from getting added in the version control.
  - Back in the Gitpod workspace I installed gunicorn using pip3 install method.
  - Then a Procfile was creating a web dyno allowing to run unicorn and serve the django app. 
  - Once acheived, the static file collection was disabled so that Heroku didnt collect the static files when deploying. 
  - Within the settings file, I added 'sports-zone-manny.herokuapp.com' to the list of ALLOWED_HOSTS.
  - Once all these changes were commited, I then pushed them to both GitHun and Heroku master branch.
  - On the deploy screen, select GitHub in the deployment section and select your app from the options of your GitHub repositories.
  - Within settings sections create config vars, these are the same as environment variables Gitpod environment. These are used here as they cant be found on the GitHub page so will need to be set up on Heroku to get the application working.
  - Automatic Deployment will need to be enabled on the settings page so that Heroku runs the most recent update

<div align="right"><p style="text-align: right"><a href="#table-of-contents">Back to top</a></p></div>

# Technologies and Tools Used

# Testing

# Acknowledgements
I would like to thank code institute for an amazing opportunity to learn and devlop my skills in web development field. I appreciate all the help and support provided through the modules, tutor assistance and many other ways of assistance. Felipe, my mentor, has once again been a great help for guiding me to the correct path, supporting me at every step of this journey and for rescuing me from any unwanted situation. Additional help provided by my mentor through mentor sessions on weekly bases really built my confidence, morale and knowledge up to achieve this goal. I would like to thank all the tutors from tutor support, who helped me resolve the issues I had by guiding me towards the solution. Also, technologies I have used, such as Boutique Ado Project and Slack to help me achieve the final version of this site.

<div align="right"><p style="text-align: right"><a href="#table-of-contents">Back to top</a></p></div>