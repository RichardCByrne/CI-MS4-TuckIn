# TuckIn - Dublin

<h2 align="center"><img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/media/amiresponsive_mockup.PNG?raw=true"></h2>

This is the repository for TuckIn - Dublin, a food ordering app, akin to JustEat and UberEats. It provides a platform for restaurants and takeaways to display their menus and receive orders through a secure and streamlined process.

[View live project here.](https://tuckin-ms4.herokuapp.com/)

## Project Rationale

The idea of building a food ordering application for the MS4 project came about after brainstorming multiple ideas and refining them with the help of my mentor. TuckIn was eventually chosen as not only would it comfortably fit within the criteria of the project, but it would also challenge me as a developer in creating a project larger than I had ever tackled before.

As a contemporary food ordering platform, TuckIn would have to include everything from cuisines to restaurants, menus to individual foods, user accounts, a secure e-commerce checkout, opening times for each restaurant and much more. It would also require a significant amount of planning of the customer's journey through the application, getting them from the homepage to order confirmation. Below, you will find multiple stages of planning and execution that was required to complete this project. As the project is so large for one novice developer, many features that were deemed unessential were added to the roadmap for development after the course has been completed.

In a commercial scenario, the owner of the site would generate revenue by taking a small commission from each order placed.

## User Experience (UX)

### Project Goals

-   Develop a food delivery web app akin to JustEat, UberEats etc.
-   Create a full-stack site using HTML, CSS, JavaScript, Python+Django.
-   Utilise a secure login system to allow users to create an account.
-   Provide an easy-to-use search platform for users to find restaurants serving Dublin.
-   Use a relational database, hosted on AWS.
-   Integrate Stripe to accept secure payments.

### Developer Goals

-   Create a commercial-grade web app that could be a minimum viable product/proof of concept for a real-world business.

### User Stories

#### Viewing and Navigation

-   As a hungry site user, I want to be able to...
    -   View available restaurants in my area
    -   See which restaurants are open and which are closed
    -   Clearly and easily see other customers' ratings of a restaurant
    -   View food available from a restaurant in easy-to-navigate sections
    -   View a restaurant's opening times
    -   View a restaurant's delivery charge

#### Registration and User Accounts

-   As an enthusiastic and efficient foodie, I want to be able to...
    -   Register for an account
    -   Easily login and logout
    -   View my previous orders
    -   Save an address for use in checkout
    -   Recover my password in case I forget it

#### Sorting and Searching

-   As a site user who is looking for something specific, I want to be able to...
    -   Refine restaurants by cuisine
    -   Sort restaurants by rating and delivery cost
    -   View food from a specific restaurant's menu section
    -   Search for a restaurant either by name, cuisine, food or food description

#### Purchasing and Checkout

-   As a site user who needs food ASAP, I want to be able to...
    -   Add food to my bag with a message for the restaurant
    -   Change the quantity of food being added to my bag
    -   View items in my bag to be ordered
    -   Adjust the quantity of a food item in my bag
    -   Confirm my address details before ordering
    -   Easily choose a delivery time for my order
    -   Simply and quickly enter my card details for payment
    -   Feel my information and payment is secure
    -   Reach out for help if something goes wrong
    -   View an order confirmation upon checking out successfully
    -   Receive an email confirming my order

#### Admin and Store Management

-   As the proud site owner, I want to be able to...
    -   Accept requests from restaurants to join the platform
    -   Receive requests for help from customers

### Design Choices

-   Colour Scheme

    -   The colours used throughout the website are: #E96800 (primary buttons and links), #0073CF (secondary buttons and links), #354555 (opening later banner) and #F1F2F4 (footer background).

    -   The primary colour (#E96800) of the site was chosen because, according to popular colour theory, it is energetic and draw attention. The intention is to give users the impression that their hunger can be satiated quickly by using this site. Orange hues can also represent a refreshing feeling, linked to citrus fruit.

    -   The secondary colour (#0073CF) of the site was chosen as the direct compliment of the primary colour (#E96800) using [colourpicke.me](https://colorpicker.me/).

-   Layout

    -   [This website](https://www.just-eat.ie/) and [this website](https://www.ubereats.com/ie) were used to inform the layout choices made.

    -   The current state of the site includes 3 fake restaurants with a limited amount of food. As this is a proof of concept and not a final product, this was deemed to be enough content to portray the purpose and functionality of the site.

    -   The restaurant phone numbers were purposely excluded from the restaurant menu to encourage the user to order through TuckIn, and not directly from the restaurant itself. The restaurant's phone number is provided on the order confirmation page if a user needs to contact them about an order.

    -   The footer was removed from the bag and checkout pages so as to minimise potential distractions that could prevent the user from completing an order.

    -   In a commercial setting, the logo would just read 'TuckIn' without the '- Dublin' ending. The '- Dublin' ending currently exists as part of a number of measures to ensure users know that the current state of the site only allows ordering from 'restaurants' in Dublin.

-   Typography

    -   One primary font was used throughout the website: 'Inter'. The logo, however, uses 'Baloo 2'. 'Inter' was chosen for its easy readability and simplicity, reducing friction for users allowing them to get their food faster. 'Baloo 2' with its rounded edge and lack of ornamentation was chosen for the logo to display a sense of carefree-ness, light-heartedness and youthfulness. This combines with the 'energy' of the orange colour to provide consistent messaging to the user about the type of business with whom they are interacting.

-   Imagery

    -   Images play a large role throughout the website. The homepage contains a large background image to warm up the taste buds of the user. Each restaurant is [primarily represented by the image](https://www.easel.ly/blog/text-vs-images-which-content-format-effective/) and logo chosen by the restaurant, and secondarily by the restaurant name. The same goes for each food item within restaurants' menus, but to a lesser extent.

### Wireframes

-   Homepage

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Homepage%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Homepage%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Homepage%20-%20Desktop.png?raw=true)

-   Restaurants

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Restaurants%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Restaurants%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Restaurants%20-%20Desktop.png?raw=true)

-   Restaurant Menu

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Restaurant%20Menu%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Restaurant%20Menu%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Restaurant%20Menu%20-%20Desktop.png?raw=true)

-   Bag

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Bag%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Bag%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Bag%20-%20Desktop.png?raw=true)

-   Delivery Address

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Delivery%20Address%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Delivery%20Address%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Delivery%20Address%20-%20Desktop.png?raw=true)

-   Delivery Time

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Delivery%20Time%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Delivery%20Time%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Delivery%20Time%20-%20Desktop.png?raw=true)

-   Checkout Payment

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Checkout%20Payment%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Checkout%20Payment%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Checkout%20Payment%20-%20Desktop.png?raw=true)

-   Order Confirmation

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Order%20Confirmation%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Order%20Confirmation%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Order%20Confirmation%20-%20Desktop.png?raw=true)

-   Profile

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Profile%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Profile%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Profile%20-%20Desktop.png?raw=true)

-   Order History

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Order%20History%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Order%20History%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Order%20History%20-%20Desktop.png?raw=true)

-   List Your Restaurant

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/List%20Your%20Restaurant%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/List%20Your%20Restaurant%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/List%20Your%20Restaurant%20-%20Desktop.png?raw=true)

-   Policies

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Policies%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Policies%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Policies%20-%20Desktop.png?raw=true)

-   Help

    -   [Mobile](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Help%20-%20Mobile.png?raw=true)
    -   [Tablet](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Help%20-%20Tablet.png?raw=true)
    -   [Desktop](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/wireframes/Help%20-%20Desktop.png?raw=true)

## Features

### Current Features

-   Food ordering from local restaurants
-   Allows users to interact with an e-commerce website as expected by modern web users
-   User accounts that can save information for a quicker checkout experience
-   View order history
-   Search functionality
-   Interactive elements
-   Responsive on all common device sizes

### Features Left to Implement

-   Use restaurant names instead of id numbers in the restaurant URL.
-   Allow users to change their email addresses (presents logistical and security issues).
-   Ability to add multiple addresses to one account.
-   Add real-time updates of an order's status ('cooking'/'on it's way' etc.) to order confirmation page.
-   Add the ability to add a note to the overall order for the restaurant.
-   Add the ability to edit notes/additional details.
-   Add flexible minimum order amount.
-   Allow users to choose delivery or collection.
-   Add restaurant accounts so that they can manage their inventory.
-   Allow restaurants delivery and collection times to be separate.
-   Allow restaurant to have delivery intervals other than 15 minutes (done via adding delivery_interval option to model and setting interval to self.delivery_interval in class' functions).
-   Allow restaurant opening times to span over 2 days e.g. 13:00 - 02:00.
-   Implement flexible minimum time before the first available delivery slot as different restaurants prepare food at different speeds, and have different delivery schedules.
-   Allow customers to pre-order with a restaurant if it's not open today.
-   Add a prompt to remove everything from the bag when food from another restaurant is in the bag.
-   Allow the user to store a different bag for each restaurant.
-   Add choices to food modal e.g. select toppings.
-   Add ability for restaurants to issue discount codes.
-   Properly integrate vegan and vegetarian options to allow users to see restaurants that serve these diets.
-   Show previous orders on the homepage for easy re-ordering.
-   Use Google Place's Autocomplete for checkout address forms.
-   Refine checkout by skipping checkout address if the user has an address associated with their account and hasn't submitted a new address on the homepage.
-   Add automated order confirmation text message when a user successfully submits an order.
-   Allow sorting within a specific cuisine
-   Add a minimum delivery threshold
-   Add an optional delivery threshold for free delivery
-   Add ASAP to delivery time options
-   Allow a user to proceed with their order if a restaurant closes while the user is in the process of ordering.
-   Allow users to edit messages for the restaurant within the bag.
-   Allow users to choose to pay with cash at the door if being delivered, or at the restaurant, if collecting.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python 3.9](https://www.python.org/)
-   [JavaScript ES6](https://www.javascript.com/)

### Frameworks, Libraries & Programs Used

1.  [Django 3.1.7](https://www.djangoproject.com/)
    -   Django 3.1.7 was used as the web framework for this project.

2.  [jQuery](https://jquery.com/)
    -   jQuery was used to streamline the process of writing JavaScript code.

3.  [AWS S3](https://aws.amazon.com/s3/)
    -   S3 was used to store the database for the site.

4.  [Git](https://git-scm.com/)
    -   Git was used for version control by utilizing the terminal to commit to Git and Push to GitHub.

5.  [GitHub](https://github.com/)
    -   GitHub was used to store the project's code after being pushed from Git.

6.  [Django Allauth](https://django-allauth.readthedocs.io/en/latest/overview.html)
    -   Allauth was used to create a secure system through which users could safely register for accounts, log in, log out and perform other account-related activities.

7.  [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/#)
    -   Crispy Forms was used to easily control the rendering behaviour of the forms used on the website.

8.  [VSCode](https://code.visualstudio.com/)
    -   VSCode was the text editor used for this project. All installed addons can be found in the 'requirements.txt' file.

9.  [Django Mathfilters](https://pypi.org/project/django-mathfilters/)
    -   Mathfilters was used for the creation and rendering of the rating system for restaurants.

10. [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
    -   Django Debug Toolbar was used to aid in the debugging of errors that occurred throughout development.

11. [Django Storages](https://django-storages.readthedocs.io/en/latest/)
    -   Django Storages was used to allow Django to access the database setup on AWS S3.

12. [Balsamiq](https://balsamiq.com/)
    -   Balsamiq was used to create the wireframes during the design process.

13. [LucidChart](https://www.lucidchart.com/)
    -   LucidChart was used to create the database schema diagram for the README.

14. [Stripe](https://stripe.com)
    -   Stripe was used to accept payment for orders.

15. [Cookie/Privacy Policy Generator](https://www.cookiepolicygenerator.com/) 
    -   Cookie Policy Generator was used to generate cookie and privacy policies.

16. [RegExr](https://regexr.com/)
    -   RegExr was used to test and generate regular expressions for use in field validation.

## Development

### Database Schema

<img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/media/tuckin_ms4_dbms_diagram.png?raw=true">

-   The database for TuckIn is a flat system made up of 8 custom collections.

-   The fields for each record can be found in the above image, or at [this link](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/media/tuckin_ms4_dbms_diagram.png).

-   Conceptually speaking, the database can be split into two conjoined sections: the order section and the restaurant section. The diagram above displays the order section in the top half and the restaurant section in the lower half.

### Django Secret Key Exposure

When starting off this project, I followed along with the course lectures to ensure that I had the project set up properly. In the course lecturers, however, the lecturer uploads the Django secret key to GitHub. I also did the same before realising what had happened. After contacting Student Care, they confirmed that removing 'settings.py' from GitHub in future commits or changing the Django secret key would be sufficient so as to not incur any penalties during grading. As such, I generated a new secret key using [https://miniwebtool.com/django-secret-key-generator/](https://miniwebtool.com/django-secret-key-generator/).

### Google Maps Places API Autocomplete Limitations

While implementing the Autocomplete feature from Google's Maps API, I discovered that while you could restrict results to a specific country or between a set of co-ordinates, Google would [not allow you to restrict results to a specific city](https://issuetracker.google.com/issues/35822067). As a workaround, I tried using two pairs of co-ordinates that surrounded the entire county of Dublin. However, this proved unworkable as, firstly, since Dublin's boundaries do not form a quadrilateral, the co-ordinates that would create the boundary would either include places outside of Dublin, or exclude areas within the county. Secondly, when setting a strict boundary in the Places API, you are restricted only to road and area names, with no house addresses being selectable.

The most effective solution to this is to use a combination of Google's Maps APIs (Places, GeoCoding, Geolocation, Distance Matrix) in conjunction with one another to convert a given co-ordinate into standard address format, and to then to use the aforementioned services to check if that address is within Dublin. This method would provide extra validation of the inputted address through cross-checking it through multiple different Google services, leading to higher accuracy, better results and tighter security. If this were a commercial project, this would be the way in which I would solve this problem. However, as this is a college project and using these APIs together could easily incur hefty monthly costs, I chose to use the free Google Maps Places API as well as native form validation via HTML. The word 'Dublin' was also placed into 3 different places on the homepage (including the website logo) so that users would know before typing that the service is restricted to Dublin. 

Biases were also used in the API settings so that the API would search within Dublin first, but it ultimately searches all counties of Ireland if not enough results are found within Dublin.

The 'findPlaceFromQuery' method was used to find a place within the Google Maps Places' database using the selected autocomplete address. Then, if the address contained the string 'Dublin' or 'Baile Átha Cliath' (for Irish-speaking users), the form can be submitted. Otherwise, the submit button becomes disabled and an error message displays informing the user of the corrective action. While this method is more simple than the ideal method, it is effective and appropriate for the use case of this college project.

As this is an MVP, all restaurants are presumed to deliver all over Dublin. In a commercial scenario, a more sophisticated system of address verification, delivery radii and geo-tracking would be used from the paid services of the Google Places API.

### Django Math Filters

-    In order to use multiplication and division in the Django templating language (without the result returning a rounded integer), [Django Math Filters](https://pypi.org/project/django-mathfilters/) was installed to allow this functionality. Specifically, it was required for the creation of the star ratings underneath each restaurant card in 'restaurants.html'.

### Custom Django Template Filters

-    Custom template filters were written to aid in the creation and rendering of the star rating system for restaurants. These can be found in 'restaurants/templatetags/restaurants_extra.py' or at [this link](https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/restaurants/templatetags/restaurants_extra.py).

-    Django's built-in 'json_script' template tag was used to [prevent code injection](https://adamj.eu/tech/2020/02/18/safely-including-data-for-javascript-in-a-django-template/) via some of Django's vulnerabilities.

### Delivery Time Timezone Issues

-    Upon starting the project, the 'TIME_ZONE' property in 'settings.py' was set to 'Europe/Dublin' to reflect the localised nature of the service. Each datetime object was also given the same time zone to make it an 'aware' datetime object. However, it was discovered upon viewing an order after submission, that the 'Europe/Dublin' timezone was being interpreted as '+0025' instead of '+0100'. This was later found out to be caused by the datetime objects ['not working' with pytz](http://pytz.sourceforge.net/#localized-times-and-date-arithmetic) for many time zones. As such, the project and all datetime objects were reverted to UTC via Django's 'timezone.utc' class. Issues still persist depending on the device of the user, which would require further examination before becoming a commercial product. In a transnational commercial example, the timezone of the user and the restaurant would be calculated separately so as to avoid errors. As such, the application does not currently adapt to daylight savings time. Therefore depending on when the examiner views this project, the delivery times may be an hour behind.

### Other/Misc

-   Despite contemporary style guides, HTML files were named using snake case for continuity and cohesion with the python views that call them.

-   A note for the CodeInstitute examiner: Some restaurants may not be open depending on what time of day the examiner is grading this project. Time is set to UTC.

-   After completing circa 60% of the project, I received feedback regarding my previous project stating that it would be useful to include more detail in my commit messages. I integrated this feedback into this project as soon as I received it by increasing the frequency at which I made commits. This allowed for lower-level and less crucial functionality and changes to be documented. However, VSCode recommends keeping commit messages to no more than 50 characters which I adhered to most of the time throughout this project.

-   For customers, the user field in the CustomerProfile model was named 'customer' instead of 'user' to prevent potential confusion in the future, when admin accounts for the restaurants themselves are to be set up, allowing them to manage their menu and details.

-   While jQuery was used for most of the JavaScript in the project, it was not used for the implementation of Google Autocomplete, in order to stick to Google's recommended practices.

-   CSRF tokens were removed while testing to avoid conflict with Cypress not providing the CSRF tokens needed for Django's security.

-   When changing a food's quantity in the bag, it is presumed that if the user does not continue with checkout, that they do not want to save the changes they made to any quantities in their bag. Therefore, if a user makes changes in their bag but then goes back to the restaurant's page or closes their browser tab, their changes are not saved. Only by proceeding with checkout will their changes to a food's quantity be saved. Deleting a food item does not have this restriction.

### Notable Issues Encountered

-   The 'payment_intent.succeeded' webhook from Stripe kept failing due to being unable to get anything except the payment id from the intent (an Attribute error kept occurring, Stripe support recommended removing the code causing the issue). As each payment intent is unique, the decision was made to simply use the payment intent to search for the order in the webhook handler.

-   'f-strings' were replaced with the '.format' method for Stripe's webhook handlers that were used in the lectures, as 500 errors were frequently occurring when using 'f-strings'. Stripe also uses the '.format' method in their example code in the [Stripe Docs](https://stripe.com/docs/webhooks/build).

-   While there are measures in place throughout the project to ensure the validity of the address inputted by the user, a user can still place an order with a false or disingenuous address. In a production website, full address verification provided by the Google Places API services that are behind a paywall would be used to prevent this from happening.

-   In rare circumstances, a restaurant with a 5-star rating displayed 6 stars, and a restaurant with a 3-star rating might only display 4 stars. The cause of these issues was eventually found to be an error in the rendering logic of the stars. More details can be found in the commit messages regarding this issue.

## Testing

### Code Validation

-   [MagicPython](https://marketplace.visualstudio.com/items?itemName=magicstack.MagicPython) 
    -   MagicPython was used to format all Python code to [PEP 8](https://pep8.org/) standard

-   [JSHINT](https://jshint.com/)
    -   JSHint was used to check for JavaScript errors. However, due to the widespread use of jQuery in the project, its usefulness was limited.

-   [Webformatter JavaScript](https://webformatter.com/javascript)
    -   Webformatter was used for JavaScript formatting.

-   HTML W3C Validator [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftuckin-ms4.herokuapp.com%2F)
    -   W3C's HTML validator was used to validate all HTML code rendered in the final project.

-   CSS W3C Validator [Results](http://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ftuckin-ms4.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    -   W3C's CSS validator was used to validate all CSS files. It found errors with Bootstrap's CSS that are out of the control of the developer, and therefore should not inform any grading decisions made.

### Testing User Stories from User Experience (UX) Section

#### Viewing and Navigation

-  As a hungry site user, I want to be able to...

    1.  View available restaurants in my area.

        -   Upon entering the site, the user is greeted with a screen dedicated to entering their address so that they can view restaurants available in their area.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/all_restaurants.PNG?raw=true">

    2.  See which restaurants are open and which are closed.

        -   Upon searching for restaurants, the user is presented first with a grid of restaurants that are open. Beneath the open restaurants is a banner stating the number of restaurants that will be opening at another time/date. These currently closed restaurants are then displayed beneath the banner in a similar grid with their images slightly greyed out.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/open_restaurants_with_closed_banner.PNG?raw=true">
        

        -   If a user goes to a restaurant menu of a restaurant that is currently closed, the banner image will be slightly greyed out, a message will be displayed beneath the restaurant name in the banner stating the next time it opens for ordering, and adding food to an order from a closed restaurant is also disabled.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/closed_restaurant_menu_header.PNG?raw=true">
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/closed_restaurant_add_food_to_bag_disabled.PNG?raw=true">

    3.  Clearly and easily see other customers' ratings of a restaurant.

        -   A restaurant's rating is displayed below its name on the 'All Restaurants' page. Users can submit ratings of a restaurant upon completing an order from that restaurant. Users can also change their rating via their order history should they wish to.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/restaurant_rating.PNG?raw=true">

        -   A restaurant's rating was purposely not placed on its menu, so as to encourage users to form their own opinions of restaurants on the platform.

    4.  View food available from a restaurant in easy-to-navigate sections.

        -   Each restaurant has a menu, containing multiple sections for the user to view, just like a physical menu. Links are provided for each section in case a user wants to skip to a particular section.
        
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/restaurant_menu_food.PNG?raw=true">

    5.  View a restaurant's opening times.

        -   Restaurant opening times are clearly displayed in the restaurant information section beneath the banner on the menu page.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/restaurant_menu_info.PNG?raw=true">

    6.  View a restaurant's delivery charge.

        -   Restaurant delivery charges are displayed in two areas: the 'All Restaurants' grid and in the restaurant menu. This allows for complete transparency and means the user gets no surprise charges at checkout.

        
        -   The delivery charge is also clearly displayed and accounted for in both the bag and the checkout stages so the user is always aware of all the costs.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/bag.PNG?raw=true">
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/checkout_order_summary.PNG?raw=true">

#### Registration and User Accounts

-   As an enthusiastic and efficient foodie, I want to be able to...

    1.  Register for an account.

        -   Account registration can be easily accessed from the nav, or from the checkout payment page.
        
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/navbar.PNG?raw=true">
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/checkout_create_account_or_log_in.PNG?raw=true">

    2.  Easily log in and log out.

        -   If a user is not logged into their account, a login button is displayed in the nav.
        -   If a user is logged into their account, a logout button is displayed in the nav.
        
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/navbar.PNG?raw=true">
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/navbar_logged_in.PNG?raw=true">

    3.  View my previous orders.

        -   As long a user has created an account and has logged into that account before placing an order, all their orders will be saved to their account for them to view in detail.
        
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/order_history.PNG?raw=true">

    4.  Save an address for use in checkout.

        -   Users can save their address for ease of use later when placing orders. This reduces the steps needed to be taken by a user to place the order and reduces friction in the purchasing process.
        
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/account_address.PNG?raw=true">

    5.  Recover my account in case I forget my password.

        -   Users can safely recover their account via the login screen, where there is a button to reset their password.
        
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/login.PNG?raw=true">

#### Sorting and Searching

-   As a site user who is looking for something specific, I want to be able to...

    1.  Refine restaurants by cuisine.

        -   Restaurants can be refined by their cuisine either via the homepage or directly in the 'All Restaurants' view.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/cuisine_refine.PNG">

        -   Not all cuisines contain restaurants at this time but are there for display purposes only.

    2.  Sort restaurants by rating and delivery cost.

        -   All restaurants can be sorted either by their rating from highest to lowest, or by their delivery cost, lowest to highest.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/sort.PNG?raw=true">

    3.  View food from a specific restaurant's menu section.

        -   Links are provided for each section within a menu at the top of the menu beneath the restaurant info section. These links smoothly bring the user down to the section associated with the link.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/menu_sections.PNG?raw=true">

    4.  Search for a restaurant either by name, cuisine, food or food description.

        -   The navigation bar contains a search box that users can use to find a restaurant they like quickly, or to find restaurants that contain food-related to the search query.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/searchbar.PNG?raw=true">

#### Purchasing and Checkout

-   As a site user who needs food ASAP, I want to be able to...

    1.  Add food to my bag with a message for the restaurant.

        -   Users can add food to their bag with a message for the restaurant via the popup modal that appears when selecting food from the menu.
        
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/add_food_to_bag.PNG?raw=true">

        -   If a user adds the same food to their bag but with different messages, the messages are displayed with commas separating them. This would need to be re-examined before commercial release.
        
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/bag_showing_food_messages.PNG?raw=true">

    2.  Change the quantity of food being added to my bag.

        -   When adding a menu item to the bag, users can adjust the quantity of the item up to 15 and no less than 1.

        -   While users can currently add more than 15 of a particular food item to their bag by adding the food multiple times, the bag page will not allow the user to proceed unless the quantity of each food item is less than or equal to 15.

    3.  View items in my bag to be ordered.

        -   The bag icon in the navbar brings users to the bag page where they can preview their order and make changes to food items and quantities if necessary.
        
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/nav_header.PNG?raw=true">

        -   The mobile bag icon contains the number of items currently in the bag for viewing convenience on the small screen.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/mobile_bag_icon.PNG?raw=true">

    4.  Adjust the quantity of a food item in my bag.

        -   Users can easily change the quantity of a food item on the bag page without the need to click an 'update' button. The assumption is made that if the user does not proceed with the order, the user does not want to save changes made to the bag. The changes made are saved upon pressing the 'Go to Checkout' button.

    5.  Confirm my address details before ordering.

        -   Users must enter their address if they are not signed into an account upon proceeding with checkout from the bag. Signed in users will have the address saved to their account pre-loaded into the fields.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/checkout_delivery_address.PNG?raw=true">

        -   Users have a second chance to verify/change their address upon reaching the payment page, in order to prevent orders from being sent to the wrong address.
        
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/checkout_payment_form.PNG?raw=true">

        -   Even though signed in users can save an address to their account, the 'Delivery Address' screen always gets displayed in case the user wants to order to an address not saved to their account.

    6.  Easily choose a delivery time for my order.

        -   The user can easily select a delivery time that suits them upon entering their address details in the checkout process.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/checkout_delivery_time.PNG?raw=true">
        
        -   Currently, the default delivery times are every 15 minutes on the hour from when a restaurant opens.

    7.  Simply and quickly enter my card details for payment.

        -   Stripe is used to accept card details securely in a one-line entry system. This allows users to enter all the details of their card in one line without having to change to another field on the form.

    8.  Feel my information and payment is secure.

        -   Stripe is a well-trusted payment method that uses state of the art security to process payments, providing peace of mind to both the buyer and the seller.

    9.  Reach out for help if something goes wrong.

        -   The navbar contains a link to the help page where users can contact the business for assistance.

        -   A link to the help page is also conveniently provided on the payment page in case the user encounters an issue while ordering.
        
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/checkout_help_link.PNG?raw=true">

    10. View an order confirmation upon checking out successfully.

        -   Upon successfully completing an order, users are greeted with a confirmation page where they can rate the restaurant, view an order summary and add the contents of the order to their now empty bag if they wish to place the same order again.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/order_confirmation.PNG?raw=true">

        -   The user's account contains an order history where users can revisit their past orders.
        
    11. Receive an email confirming my order.

        -   Upon successfully completing an order, users are sent an order confirmation email containing an order summary for their records.

#### Admin and Store Management

-   As the proud site owner, I want to be able to...

    1.  Accept requests from restaurants to join the platform.

        -   The footer of all non-checkout related pages contains a link where restaurants can request to join the platform.

        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/help.PNG?raw=true">

    2.  Receive requests for help from customers.

        -   There is a dedicated help page where users can contact the business for assistance.
        
        <img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/list_your_restaurant.PNG?raw=true">

        -   The navbar permanently contains a link to the help page.

        -   A link to the help page is also conveniently provided on the payment page in case the user encounters an issue while ordering.

### Testing with Cypress

[Cypress](www.cypress.io) was used to create QA tests for this app.

Each test file has a video displaying all tests running and passing, which can be viewed [here](https://github.com/RichardByrne95/CI-MS4-TuckIn/tree/main/cypress/videos).

Below is an image of the summary of all the test results generated by Cypress.

<img src="https://github.com/RichardByrne95/CI-MS4-TuckIn/blob/main/readme_images/cypress_test_results.PNG?raw=true">

Cypress was used to test the application via the following steps:

1.  Cypress was installed and saved as a dev dependency via NPM (Node Package Manager) using the command
```javascript
npm install cypress --save-dev
```
2.  Cypress was then run using the command:
```javascript
npx cypress open
```
This command added a cypress folder to the project and opened the testing software.

3.  Inside the cypress folder, a new file was created within the 'integration' folder called 'djangoAppNameSpec.js'.

4.  Each test was created using the formula 'Arrange, Act, Assert':
    -   'Arrange' sets up the initial state of the app.
    -   'Act' performs an action to be tested.
    -   'Asserts' makes an assertion as to the expected state of the app after the action has been taken.

5.  A 'spec' file was created for each Django app in the project, for separation and consistency.

### Manual Functionality Testing

-   All external links are functional and open in a new tab.
-   All internal links are functional and provide user feedback where applicable.
-   All forms function and submit data correctly.
-   All cookies work as expected.

### Manual Accessibility Testing

-   Semantic markup is used to convey the document structure. Some tags, like 'summary', were not used due to a lack of support on older browsers.
-   Information is presented and categorised in terms of its priority.
-   All images contain 'alt' text. Aria labels are used when the 'img' 'alt' attribute is not available.
-   Despite following Google's Web Accessibility Guidelines for contrast, Google Chrome's Lighthouse marked a small number of valid elements as invalid. Each element has been manually checked by the developer using Google's own up-to-date documentation. For example, when a user has added a food item to their bag, a button appears in the bag to allow the user to continue to checkout. The text inside this button on desktop is 1.4rem (14px) in size and is bold. The button text on mobile is 1.8rem (18px). Both of these meet the accessibility guidelines set out [here](https://web.dev/color-contrast/?utm_source=lighthouse&utm_medium=devtools), but Google Lighthouse still displays them as errors. My suspicion is that it is due to the fact that Google is looking for font sizes in pixels, but the project uses rem units. Nonetheless, the project still meets all standard accessibility guidelines.

### Manual Usability Testing

-   All nav links bring you to the correct page.
-   The mobile navbar icon opens the navbar as expected.
-   User Navigation is unambiguous.
-   While the 'Distinction' criteria state that 'users who direct to a non-existent page or resource are redirected back to the main page', it was deemed more appropriate to either display an error message on the same page if submitting a form, or redirecting them to a different page such as the bag, and displaying a message to the user about the error. This way the user is given explicit direction and understands that something went wrong.
-   Messages are displayed at the top of the website indicating user progress and feedback where appropriate.
-   The Stripe element on the payment page triggers an accessibility error due to a hidden element being focusable. This is unavoidable as Stripe control the code inserted onto the page and does not, therefore, contribute to the grading of the project.
-   As this is a proof of concept project, the Stripe API test keys were kept in favour of the live keys, as no actual live transactions will be taking place.

### Manual Database Testing

-   No database errors occur when using the queries built for this project.
-   Data integrity is maintained while creating, reading, updating or deleting data in the database.
-   All queries correctly and accurately retrieve data from the database.

### Manual Interface Testing

-   Heroku processes and displays everything that hasn't already been noted in this README correctly.
-   All pages are aesthetically consistent.

### Manual Compatibility Testing

-   This project functions as expected on Google Chrome, Firefox and Microsoft Edge.
-   Internet Explorer is not properly supported, and Safari was unable to be tested.

### Manual Responsiveness Testing

-   The website was viewed on a variety of devices including Windows Desktop, Windows Laptop, Moto G3, Pixel 3a XL, iPhone 6s, iPhone 7, iPhone 8 & iPhone X.
-   The website is responsive on all common device sizes.

### Manual Security Testing

-   Unauthorised access to secure pages returns the user to the sign-in page, or to another relevant page.
-   Incorrect login details returns a user-friendly error and reloads the page.
-   Database code injection by search bar is prevented by using regular expressions and by using the '.isalspha()' method in Python.
The website would also HTTPS in a commerical scenario.
-   Users can only access data that is either public or in their account.
-   Users can reset their password if they forget it via the login page.
-   All data, except order numbers, order dates, order totals and stripe payment ids associated with orders, is editable via the Django admin of the site.
-   Some regular expressions had to be removed as, despite them being in the correct format, the local development server repeatedly marked valid fields as invalid.

### Performance Testing

-   Lighthouse on Google Chrome Dev Tools gave the following scores on the deployed version hosted by Heroku and AWS:

    -   Performance: 96
    -   Accessibility: 96
    -   Best Practices: 100
    -   SEO: 90

    Points were mostly deducted due to 3rd party libraries causing slowdowns. However, accessibility points were also deducted due to Chrome incorrectly marking some texts as not having a sufficient contrast ratio. [Google's own accessibility guidelines](https://web.dev/color-contrast/?utm_source=lighthouse&utm_medium=devtools) state that text with a font size over 18px or 14px bold only needs a contrast ratio of 3:1 instead of the regular 4.5:1. However, Chrome did not seem to recognise this and marked it as an error.

-   Typical SEO was not implemented as this was not deemed necessary for the purpose and context of this project.

### Further Testing

-   Try/except syntax is used to redirect the user if anything goes wrong.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
-   All HTML was formatted using VSCode's built-in formatters.

## Deployment

This project was deployed using GitHub, Heroku and AWS, with a Postgres database, via the following steps:

### Source Control Process

This project was developed using Visual Studio Code, Git and GitHub using the following steps:

1.  Logged into Github Desktop App
2.  A new repository called 'CI-MS4-TuckIn' was created locally for this project.
3.  This repository was initialised with a blank README.md file.
4.  This repository was then published from Github Desktop to the remote Github server using 'Ctrl + P'.
5.  The project folder was opened in Visual Studio Code where the initial files were created.
6.  A new terminal in Visual Studio Code (Ctrl + Shift + ') was opened to begin the git commit process.
7.  Files were added to the local git staging area using 'git add <'filename'>' and 'git add *' where applicable.
8.  Local commits were made using the 'git commit -m <'message'>' command.
9.  These local commits were then periodically pushed to the remote Github server using the 'git push' command.
10. A local server was run throughout the development process using ```python manage.py runserver``` to test changes made in real-time to the HTML pages.

### Heroku Deployment

This project was deployed to Heroku using the following steps:

1.  A new app was created on Heroku for the project, with the region set as Europe.
2.  Once the app was created, the Heroku Postgres add-on was installed in the Heroku resources tab.
3.  A backup of the database was created in a file called 'db.json' using the command (this allows the database to be imported into the new Postgres database):
    ```python
    python -m django dumpdata exclude auth.permission --exclude contenttypes > db.json'
    ```
4.  'dj_database_url' was installed using pip in order to direct the database URL to Heroku.
5.  'psychopg2-binary' was also installed using pip to facilitate the adaptation of the Postgres database by this Python application.
6.  'dj_database_url' was imported into the project's 'settings.py' and the default 'DATABASES' variable value was replaced with "{'default': dj_database_url.parse()}".
7.  The 'Config Vars' were revealed in the Heroku app's Settings tab and the database URL was copied and pasted as a string into the brackets of the parse method from the previous step.
8.  The following command was then used to load the database backup created in step 3 into the new Postgres database:
    ```python
    python -m django loaddata db.json
    ``` 

9.  As a new database was now being used, the project's migrations needed to be applied by using: 
    ```python
    python manage.py migrate
    ```

10. An if statement was added to 'settings.py' so that the application could detect whether it should be using the hosted database or the local development database.
11. Gunicorn was then installed via pip which acts as the webserver in this project.
12. A Procfile was created in the project's root in order to tell Heroku to create a web dyno and run Gunicorn to serve the Django app.
13. 'heroku login' was used to login into the Heroku CLI.
14. In order to temporarily prevent Heroku from collecting the static files upon deployment, the following command was used:
    ```python
    heroku config:set DISABLE_COLLECTSTATIC=True --app=APP_NAME
    ```

15. The Heroku app hostname was added to ALLOWED_HOSTS in settings.py as 'HEROKU-APP-NAME.herokuapp.com'. 'localhost' and '127.0.0.1' were also added for local development.
16. A Heroku git remote was initialised using:
    ```python 
    heroku git:remote -a HEROKU_APP_NAME
    ```
17. The project was then deployed to the Heroku master via 'git push heroku main'.
18. The application was set up to automatically deploy from GitHub via Heroku's deployment settings.
18. In 'settings.py', 'DEBUG' was set to be true only if an environment variable called 'DEVELOPMENT' was present.

### AWS S3 Bucket Setup

1.  A new AWS S3 bucket was created with the same name as the Heroku app for this application.
2.  During setup of the bucket, 'Block all public access' was disabled in order to allow users to access the static files.
3.  'Static website hosting' was enabled for the bucket via the bucket's properties, and 'Host a static website' was chosen with document values set as 'index.html' and 'error.html' respectively.
4.  Under the bucket's permissions, a JSON 'CORS' configuration was added to set up the required access between the Heroku app and the S3 bucket.
5.  A bucket policy was generated using the policy generator. The 'Principal' field was set to allow all principles using '*', and the action was set to 'Get object'. The ARN (Amazon Resource Number) was then copied from the bucket policy page and pasted into the policy generator. 
6.  Once generated, the policy was pasted into the policy editor. The 'Resource' key of the policy was edited by adding '/*' to the end of the ARN to allow access to all resources in this bucket.
7.  The Access Control List was edited to allow public access to 'List' the objects in the bucket.

### AWS Group and User Access Setup

1.  Next, a new group was created in IAM (Identity and Access Management) called 'manage-HEROKU-APP-NAME'.
2.  Once created, a new Access management policy was created from the Policies section in IAM, by importing the 'AmazonS3FullAccess' policy.
3. The policy's 'Resource' key was changed to a list containing two strings, one being the S3 bucket's ARN, and the other being the ARN with '/*' at the end. This allows access to both the bucket and the content of the bucket.
4. The policy was named 'HEROKU-APP-NAME-policy' and a brief description of the policy was added.
5. The policy was then attached to the group created a few steps ago.
6. Lastly, a user was created called 'HEROKU-APP-NAME-staticfiles-user', programmatic access was given, and then the user was added to the group.
7. Once the user was created, the .csv file was downloaded that contained the user's Access key and Secret Access key.

### Connecting Django to AWS

1.  'boto3' and 'django-storages' were installed using pip, and 'storages' was added to the project's installed apps.
2.  'USE_AWS' environment variable was added to Heroku, and if statement was added so that if it existed, the following variables were assigned:
    ```python
    AWS_STORAGE_BUCKET_NAME = 'S3_BUCKET_NAME'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    ```
3.  The relevant variables and values from the last step were added to Heroku, and the 'DISABLE_COLLECTSTATIC' variable was removed to allow Django to collect our static files and upload them to S3.
4.  In order to tell Django where our static files will be coming from in production, another variable was added in settings.py called 'AWS_S3_CUSTOM_DOMAIN' with a value of 'BUCKET-NAME.s3.amazonaws.com'.
5.  Next, in order to tell Django that we want to use S3 to store the static files whenever 'collectstatic' is run, a new file at the root level called 'custom_storages.py' was created.
6.  Inside this file, 'settings' was imported from 'django.conf' and 'S3Boto3Storage' was imported from 'storages.backends.s3boto3'.
7.  Then a StaticStorage class was created, which inherited the 'S3Boto3Storage' class. A 'location' property was added with a value of 'settings.STATICFILES_LOCATION'. A copy of this class was then pasted below and its names adjusted for the media storage.
8.  Back in 'settings.py' the following variables and relevant values were created and assigned:
    ```python
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    ```
9.  In order to override and explicitly set the URLs for static and media files, the following variables were created in 'settings.py':
    ```python
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}'
    ```
10. A cache control section was added to 'setting.py' in order to improve performance for users by caching static files for a long time. This was done by adding the following variable:
    ```python
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    ```
11. In order to add media files to S3, a new folder was created in the S3 bucket called 'media' and the media files were uploaded to it.

### Using Django and Gmail to Send Emails

In order to send emails to users who either set up an account or place an order, a simple SMTP server was set up in Gmail using the developer's chosen email address via the following steps:

1.  In Gmail, 'Settings' was opened, then the 'Accounts and Imports' section was selected, and then 'Other Google Account settings' was clicked.
2.  2-step verification was enabled under the 'Security' tab.
3.  'App Passwords' was opened and a new app with an app of 'Mail', and then 'Other' + 'Django' as device type.
4.  The password was then copied and pasted into Heroku's config variables as 'EMAIL_HOST_PASSWORD'.
5.  Another config variable was added called 'EMAIL_HOST_USER' with a value of the developer's chosen email address.
6.  Next, the following code was added to 'settings.py':
    ```python 
    if 'DEVELOPMENT' in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = 'tuckin@example.com'
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
        DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
    ```
7.  Lastly, a method was created in 'webhook_handler.py' to send a confirmation email when the order had been confirmed in the database.

### Project Status

-   This project's development has paused while the grading for this project is being completed. This status will change once the course has been completed.

## Credits

If code was directly copied and pasted from another source and left unchanged, then the link to the source will be above that code. However, if a source was referenced but significantly customised to the project's needs, then the link above the code will be preceded by 'Referenced...'.

### Content

-   All content, unless otherwise stated, was written by the developer.

### Media

#### Image Sources

##### Background Images

-   Homepage - https://unsplash.com/photos/JplMVRjzQVU
-   Cookies Background - https://www.pexels.com/photo/cookies-on-square-white-ceramic-plate-890577/
-   Privacy Background - https://www.pexels.com/photo/camera-cctv-control-monitoring-274895/
-   Error Background - https://unsplash.com/photos/0W4XLGITrHg

##### Ezio Pizza

-   Cover Image - https://unsplash.com/photos/MQUqbmszGGM
-   Bufalina Pizza - https://unsplash.com/photos/exSEmuA7R7k
-   Panettone - https://unsplash.com/photos/AQ_og51xGlE
-   Antolini Amarone della Valpolicella Moropio - https://winesdirect.ie/pier-paulo-antolini-amarone-classico-moropio.html
-   Zuppa Del Giorno - https://unsplash.com/photos/KGw62KtHzxA

##### McDoogle's

-   Big Muc - https://unsplash.com/photos/sc5sTPMrVfk
-   Quarter Kilo - https://www.pexels.com/photo/ham-and-bacon-burger-2983098/
-   Cheez Burger - https://www.pexels.com/photo/close-up-photo-of-hamburger-1893557/
-   Chicken McNaggets - https://unsplash.com/photos/P_z_xlMGuEk
-   Coca Cola - https://unsplash.com/photos/z8PEoNIlGlg
-   Sweet Chilli Bean Wrap - https://unsplash.com/photos/F10nTHkCiW8
-   Chips - https://unsplash.com/photos/t4NNQyv09Sw

##### Tomato King

-   MASSIVE Burger - https://www.pexels.com/photo/photo-of-burger-beside-fires-3616956/
-   MightyMeaty - https://www.pexels.com/photo/person-holding-a-double-patty-cheese-burger-3826273/
-   MiniMeaty - https://www.pexels.com/photo/close-up-photo-of-a-cheeseburger-1556698/
-   MiniMeaty Meal - https://www.pexels.com/photo/tomato-burger-and-fried-fries-1600727/
-   Classic Hamburger - https://www.pexels.com/photo/photo-of-burger-and-fries-3219547/
-   Classic Hamburger Meal - https://www.pexels.com/photo/plate-of-fries-and-burger-3219483/
-   Crispy Chicken Burger - https://www.pexels.com/photo/bread-food-dinner-lunch-6896379/
-   Classic Chicken Burger - https://www.pexels.com/photo/bread-food-dinner-lunch-7963144/
-   Crispy Chicken Wings - https://www.pexels.com/photo/cooked-leg-chicken-with-green-vegetable-leaf-60616/
-   Fanta - https://pixabay.com/photos/aluminum-can-coca-cola-cylinder-87987/
-   Pepsi - https://pixabay.com/photos/pepsi-can-soda-cola-supermarket-5152332/
-   Veggie Bean Burger - https://www.pexels.com/photo/close-up-photo-of-burger-1639562/
-   Classic Chips - https://www.pexels.com/photo/fries-on-brown-table-2271110/
-   Onion Rings - https://pixabay.com/photos/food-restaurant-cafe-dining-dinner-3669928/

#### Logo Images Sources

-   Tomato King logo was sourced from [Deviant Art](https://www.deviantart.com/greateronion/art/TomatoKing-163647925).
-   McDoogle's logo was created by the developer using [freelogodesign.org](https://www.freelogodesign.org/).
-   Ezio Pizza's logo was created by the developer using [freelogodesign.org](https://www.freelogodesign.org/).

### Code

-   [Code Institute - Full Stack Software Development Course](https://codeinstitute.net/): Coding skills learned in this course allowed the developer to create all the pages of this web app.
-   [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web): Referenced for best practices for lists and images, as well as the smooth scrolling functionality.

### Acknowledgements

-   My mentor, Spencer Bariball, for continuous helpful feedback and encouragement.
-   Code Institute for giving me the skills to create this project.

### Support

-   Further information can be gotten by contacting the developer at [richardbyrne1995@gmail.com](mailto:richardbyrne1995@gmail.com)