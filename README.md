# Second Milestone Project by Holly Horwood

[Keto Kitchen Website](https://keto-kitchen-hollyci.herokuapp.com/)

---

## **Disclaimer:** 
This website was designed for educational purposes only for the Code Institute.  All best endeavours have been made to ensure all content has been obtained legally and all good practice guidelines for web development have been followed.

---

## **Motivation/Purpose**
This is my third milestone project for the Full Stack Software Development course through Code Institute.  I decided to create this website because I am a Type 1 Diabetic.  Myself and others with the condition often struggle to find good recipes and meal ideas that will not affect our blood glucose levels dramatically.  The only diet that has worked to help control this has been a low carb one so I wanted to make a site where other diabetics and followers of a low carb lifestyle can easily find delicious and healthy recipes.

---

## **UX** 

### **_Strategy_**

**Research:**

 I consider myself quite knowledgable in this area as I have lived the low carb lifestyle for many years now. I also created my own low carb Facebook page for diabetics in New Zealand that at the time of writting this has over 1500 members and continues to grow almost daily.  Via my Facebook page I am able to discuss, learn, teach and share ideas, the page was a great inspiration for this project which I intend to eventually extend on to include restaurant recommendation for people looking for somewhere to eat the offer low carb friendly options.  My facebook page alone has already changed so many lives for the better and I see this project as the start of another venture that will continue to help make diabetics lives easier and improve their health along the way.

**Audience:** 

 Anyone with diabetes or anyone following a low carb lifestyle.

### **_Scope_**

**Features:**

**Home Page**

On a smaller device like a mobile phone all recipes will display vertically one by one and on larger devices they will show as a Bootsrap card-deck side by side 3 across at a time.  As search box has been placed at the top of the screen so it is easy for the user to find what they are looking for quickly.  A navigation bar offers a way to add, login or return to the recipes page easily.  The logo can be clicked for quick access to the home page and each recipe contains a clickable image and a full recipe button that will both take the user to the full screen recipe. 

Each recipe includes some basic information like and overview blurb about the recipe, image, cooking time, calories, carbs, ratings etc to help the user decide which recipe they would like to make. 

**Full Recipe Page**

**Recipe Search Results Page**

**Login Page**

This is linked to a modal that is not functioning as this is not required for this project.

### **_Skeleton_**

**Wireframes:**
![Balsamic Mockup1](static/images/kitchen-mockup4.png)
![Balsamic Mockup2](static/images/kitchen-mockup3.png)
![Balsamic Mockup3](static/images/kitchen-mockup2.png)
![Balsamic Mockup4](static/images/kitchen-mockup1.png)

### **_Surface_** 

I designed this site using modern neutral colours.  Different variations of green are used throughout the site to represent the element of nature.  I chose grey and white for the map so as not to detract from the marker colours.  The site is very simplistic making it easier for the user to identify key areas quickly so they can use the site effectively.  The map does offer some extra features like the ability to switch from terrain view to satellite so that the user can see more detail on the map.  On the larger view there are more images and links to help and inspire the user.

---


## **User Story**

As a user on the website I want the ability to find accommodation at DOC sites around New Zealand quickly and easily. 

**End user goal:** Find a place to stay 

**End business goal:** Make finding accommodation easier.

**Acceptance criteria:** Able to search New Zealand DOC Campsite and Huts on the map, find information about them and click on the more info link to redirect to DOC website to book.

---

## **Technologies Used**

**HTML & HTML5**
- HyperText Markup Language was used to create the structure        and layout of the index.html document. 
  
**CSS & CSS3**
- Used to add style to the web page.
  
**Bootstrap**
- Bootstrap was mainly used for positioning with its grid system to position containers. It was also used to create buttons, dropdowns, navbar and cards.

**Javascript**
- Was used to connect with the APIs and to manipulate them.  It was also used to create some interactive aspects of the newsletter form.

**DOC API**
- Used to retrieve data on Department of Conservation campsites and huts throughout New Zealand.

**Google Maps API**
- Google maps was used to display the map of New Zealand and create markers and marker clusters.

**Font Awesome**
- Used for icons on the page such as the footer links and search icon.

### **Other resources:**

**Stack Exchange**
- Geo.js was found here courtesy of gatadeoro and converted from Python code to Javascript for use in this project. https://gis.stackexchange.com/questions/225065/converting-nztm-new-zealand-transverse-mercator-to-lat-long

**Stack Overflow**
- Used as a resource when needing help or guidance, mostly with Javascript.

**W3C Markup & CSS Validators**
- Used to check validity of HTML and CSS code used in this project.

**JSHint**
- Used to check all JS code for errors.

**Ajax Loader**
- Used to create the map loader icon.
   
**GIMP** 
- Used to alter images and icons

**MDN** 
- Main resource for research and help.

---

## **Testing**

**Running the Code**

- Click on the following link to access the live site at Github pages https://holly-horwood.github.io/second-milestone-project/

**Test Planning:**
  All tests were carried out manually by humans.  For the browser testing the users will interact with the map and click on all links and buttons and observe the results as well as viewing the site on different viewports. 

**Implementation:** 
 Users clicked on all buttons and links and used the map in all possible variations, users also changed screen sizes throughout the process to make sure the site was responsive.

**Results:** 
 All buttons and links behaved as expected, and map zoom levels worked as intended.

#### Browser Testing: #### 

**Chrome**

Passed.  No issues were found when used on Chrome.

**Opera**

Passed. No issues were found when used on Opera.

**Firefox**

Passed. No issues were found when used on Firefox.

**Edge**

Passed. No issues were found when used on Edge.

#### **External Testing**

**W3C Markup & CSS Valiadators**
- Used to check validity of HTML and CSS code used in this project, both returned no errors at completion.

**JSHint**
- Used to check all JS code for errors, none present on completion of this project.

#### **Issues:**

- DOC API is quite slow to run.

- DOC API key returned CORS error.  Contacted developer of API who worked on resolving the issue, once it was fixed from their end they contacted me and I was able to connect without anymore errors.

- Loader/Spinner not loading on all searches correctly.  This will be fixed in a future update.

- Marker clusterer was not clearing markers as intended on reload, this was fixed with some Javascript.

- Due to Google Maps using a Mercator style map it was quite difficult to get the zoom to work correctly for New Zealand. New Zealand is harder to scale than other countries due to it's very Southern location on the map which means that the latitude and longitude axes are distorted.

---

## **Future Updates**

-   In the future I would like to fix the loader to make sure it is spinning on each search page load.

- I would also like to change the marker colours so they stand out more.

- Search box placement on smaller devices.  Some zoom levels proved difficult to not have part of the island covered by the search box so may look to implement a search box that resizes for smaller devices in the future.

- Fix image transition so it doesn't snap back to behind the map after hover.

---

## **Deployment**

Initially this project was started in Cloud9 but after Cloud9 switched to AWS the decision was made to finish the project in VSCode due to issue using AWS.

### **Running The Code:**

- Go to my repository https://github.com/Holly-Horwood/second-milestone-project
- Click on the clone or download button
- In the Clone with HTTPs section, click  to copy the clone URL for my repository.
- Open your environment terminal
- Type `git clone` into the command line and then paste my URL that you copied.
- Press enter and the clone will be created.

### **GitHub** ###

All coding was committed and pushed to my Github repository at:

https://github.com/Holly-Horwood/second-milestone-project

It was also published on Github pages at:

https://holly-horwood.github.io/second-milestone-project/

### **Deploying to Github Once Cloned and Edited** ###

- In your terminal type `git add .` to stage all pending updates
- Type `git commit -m "example massage"` add your own message explaining what you are committing.
- Type `git push -u origin master` to push to my repository

---

## **Credits**

**Content:**

All content written by Holly Horwood.

**Media:**

- DOC Location Map Api - Crown Copyright: Department of Conservation Te Papa Atawhai [2019].
- kea.jpg & cathedralcove.jpg both obtained from Flickers Creative Commons website.
- All other images supplied by Holly Horwood and Ryan Connor from our personal collection.
- Tent and Hut icons by icons8.com
- Favicon was generated using favicon.io
- gatadeoro for his post on Stack Exchange that helped with the geo.js file creation https://gis.stackexchange.com/questions/225065/converting-nztm-new-zealand-transverse-mercator-to-lat-long
- Google Maps Marker Clusterer care of the team at google maps https://github.com/googlemaps/v3-utility-library/tree/master/markerclusterer

**Acknowledgements:**

Thanks to Sebastian Immel my mentor for all of his help and patience.  Thanks also to the students and staff at Code Institute especially my tutors Nakita, Haley and Dick.

Thank you also to Mick and Julian at DOC for all of their help and awesome API.



Star ratings app from rating widget https://rating-widget.com/get/rating/javascript/#editor

MongoDB Schema
relational schema we are using nesting.  Diet and course are not likely to be edited by users, they are administratively designed data.  The other rational is that they are simple data as they have only one field and that is tyheir name.  However the recipe collection could be quite large so for the simple purpose of populating checkboxes or search and editing we store them in their own collectiona as well.

Google fonts: Kaushan Script