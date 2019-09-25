# Third Milestone Project by Holly Horwood

[Keto Kitchen Website](https://keto-kitchen-hollyci.herokuapp.com/)

---

## **Disclaimer:** 
This website was designed for educational purposes only for the Code Institute.  All best endeavours have been made to ensure all content has been obtained legally and all good practice guidelines for web development have been followed.

---

## **Motivation/Purpose**
This is my third milestone project for the Full Stack Software Development course through Code Institute.  I decided to create this website because I am a Type 1 Diabetic.  Myself and others with this condition often struggle to find good recipes and meal ideas that will not affect our blood glucose levels dramatically.  The only diet that has worked to help control this has been a low carb one so I wanted to make a site where other diabetics and followers of a low carb or keto lifestyle can easily find delicious and healthy recipes.

---

## **UX** 

### **_Strategy_**

**Research:**

 Keto and Low Carb are very similar, the main difference is the amount of carbs allowed daily, those eating Low Carb (Low Carbohydrate) will consume usually between 50gm to 100gm of carbs per day whereas a Keto (Ketogenic) diet is stricter limiting the daily intake to less than 50gm per day to maintain a state of ketosis in the body. 
 
 I consider myself quite knowledgeable in this area as I have lived the low carb lifestyle for many years now. I also created my own low carb Facebook page for diabetics in New Zealand that at the time of writing this has over 1500 members and continues to grow almost daily.  Via my Facebook page I am able to discuss, learn, teach and share ideas, the page was a great inspiration for this project. I intend to eventually extend on this site to include restaurant recommendation for people looking for places to eat the offer low carb friendly options and I would also like to combine it with my previous project Keto Kitchen that shares recipes.  My Facebook page alone has already changed so many lives for the better and I see this project as the start of another venture that will continue to help make diabetics lives easier and improve their health along the way.

**Audience:** 

 Anyone with diabetes or anyone following a low carb/keto lifestyle.

### **_Scope_**

**Features:**

**Home Page**

On a smaller device like a mobile phone all recipes will display vertically one by one and on larger devices they will show as a Bootstrap card-deck side by side 3 across at a time.  A search box has been placed at the top of the screen so it is easy for the user to find what they are looking for quickly.  A navigation bar offers a way to add, login or return to the recipes page easily.  The logo can be clicked for quick access to the home page and each recipe contains a clickable image and a full recipe button that will both take the user to the full screen recipe. 

Each recipe includes some basic information like an overview blurb about the recipe, image, cooking time, calories, carbs, ratings etc to help the user decide which recipe they would like to make. 

**Full Recipe Page**

The full recipe page goes into detail more.  It shows a larger image with the customer rating review widget below and a short blurb about the recipe.  To the right a breakdown can been seen of important information like the author, cook time, prep time and some key nutritional information relevant to those on a Low Carb diet. 

**Recipe Search Results Page**

Once the customer has select all required search results (they can select multiple checkboxes or leave blank) they will be redirected to the display results page.  Here they can view any recipes that match the criteria they have set when selecting search options.  The options they ticked or clicked on in the search area remain visible on the screen in the search container so the user can easily see what they had chosen to look up.

**Login**

_*Note - User authentication was not required for this project so the modal is not currently functioning, authentication will be added in the future including user registration._

The modal is intended to prevent users from altering recipes added by other users.  The modal (once functioning) will require the user to enter their email address and password before they are able to login.  Users will first need to register and logged in users will be able to add, edit or delete their own recipes.

**Add and Edit Recipe Pages**

These pages have an editable form with inputs for the recipe information.  Each time a new recipe is added a unique ID is created in the Mongo database which is then used to get the recipe from the database when required.


### **_Skeleton_**

**Wireframes:**

![Balsamic Mockup1](static/images/kitchen-mockup4.png)
![Balsamic Mockup2](static/images/kitchen-mockup3.png)
![Balsamic Mockup3](static/images/kitchen-mockup2.png)
![Balsamic Mockup4](static/images/kitchen-mockup1.png)

### **_Surface_** 

I designed this site using modern neutral colours.  Different variations of green are used throughout the site to represent healthy living.  There is a logo and favicon for easy identification of the site.  The navbar is transparent however on scroll it becomes white otherwise the user may get frustrated if they try to click on anything behind the navbar as it wont work.  The bootstrap card deck was used to make it easy to identify individual recipes and where applicable the search container is at the top of the screen so the user can easily search the site.

---


## **User Story**

As a user on the website I want the ability to easily find diet friendly recipes. 

**End user goal:** Find a recipe. 

**End business goal:** Make finding health conscious recipes easier.

**Acceptance criteria:** Able to search the site for recipes matching my search criteria and get full instruction to follow so I can make the recipe.

---

## **Technologies Used**

**HTML & HTML5**
- HyperText Markup Language was used to create the structure        and layout of the index.html document. 
  
**CSS & CSS3**
- Used to add style to the web page.
  
**Bootstrap**
- Bootstrap was mainly used for positioning with its grid system to position containers. The card deck component was used to house each recipe.  Bootstrap was also used to create buttons, dropdowns and navbar.

**Javascript**
- Was used for image size restrictions and previews.

**JQuery**
- Used for the navbar colour change on scroll.

**MongoDB**
- Used to store all recipe input on a cloud based database.  
    *   MongoDB Schema - relational schema using nesting.  Diet and course are not likely to be edited by users, they are administratively designed data.  The other rational is that they are simple data as they have only have one field and that is their name.  However the recipe collection could be quite large so for the simple purpose of populating checkboxes or search and editing they are stored in their own collection as well.

**Pymongo**
- Used to interact with the MongoDB database from Python.

**Flask**
- Used to create Python routes and render or redirect them.

**Jinja**
- Used to create Python templates in HTML. 

**Unittest**
- Support with test automation.

**Heroku**
- Used in the deployment of this application.

**Ratings Widget**
- JS widget used for the star rating of each recipe.
https://rating-widget.com/

**Font Awesome**
- Used for icons on the page such as the footer links and search icon.

### **Other resources:**

**Stack Overflow**
- Image preview and file size check for add and edit pages. Code was altered but the original code was courtesy of nkon https://stackoverflow.com/questions/4459379/preview-an-image-before-it-is-uploaded

**YouTube**
- Navbar colour change on scroll - Code courtesy of System 22 I.T. Solutions https://www.youtube.com/watch?v=AM-GT_0Uu5w

**W3C Markup & CSS Validators**
- Used to check validity of HTML and CSS code used in this project.

**JSHint**
- Used to check all JS code for errors.

**MDN** 
- Main resource for research and help.

---

## **Testing**

**Running the Code**

- Click on the following link to access the live site at Github pages https://github.com/Holly-Horwood/keto_kitchen or for Heroku https://keto-kitchen-hollyci.herokuapp.com/

**Test Planning:**
  Automated testing was implemented using Pythons [unittest](https://docs.python.org/3/library/unittest.html) and can be viewed in the *test.py* file. All remaining tests were carried out manually by humans.  For the browser testing the users will interact with the map and click on all links and buttons and observe the results as well as viewing the site on different viewports. 

**Implementation:** 
 Users clicked on all buttons and links and interacted with the recipes in all possible variations, users also changed screen sizes throughout the process to make sure the site was responsive.

**Results:** 
 All buttons and links behaved as expected, and site overall worked as intended.

### **Manual Testing** 

#### Browser Testing: #### 

**Chrome**

Passed.  No issues were found when used on Chrome.

**Opera**

Passed. No issues were found when used on Opera.

**Firefox**

Passed. No issues were found when used on Firefox.

**Edge**

Passed. No issues were found when used on Edge.

#### **Individual Page Testing:**

**Home**

- Any errors found via validators were corrected.  Several different searches were entered into the search area, when search was clicked the page redirected to the results page as expected and showed any recipes matching the search criteria selected.  The image on the card for each recipe was clicked to ensure this redirected to the correct full recipe, all images behaved as expected.  From the full recipe page the 'recipe' nav item was clicked and that returned the user to the idex.html page again.  All recipes are showing the correct names and details as per the database.  The 'full recipe' card button was also clicked on each recipe to ensure the user would be redirected to the correct page, this worked as expected. The login nav item was also clicked, this links to a non functioning login modal, this will be made functional in the future but for this project is not required to work, the modal behaves as intended at this stage.  All colour and text is consistant, all all elements are aligned correctly.

**Full Recipe**

- Any errors found via validators were corrected.  Each recipe was checked to ensure the layout was as expected which it was.  Clicking on the Keto Kitchen logo on the top left redirects to the home page.  The 'edit' button redirects to the appropriate recipe ID in 'editrecipe.html' and the 'delete' button removes the recipe from the website and database respectively. All colour and text is consistant, all all elements are aligned correctly.

**Edit Recipe & Add Recipe**

-   Both pages are almost identical and any errors found via validators have been corrected.  In both all fields are editable and once the update or add recipe button is clicked the page will save everything to the database and populate the website.  There are some checks in place that ensure all fields are completed so if any are left blank the user is prompted to fill them out before continuing, all areas on this page are working as expected.  The images also have Javascript to check for image sizes before they are uploaded, images will also be previewed so the user can ensure they have selected the correct image for their recipe. Clicking on the Keto Kitchen logo on the top left redirects to the home page. All colour and text is consistant, all all elements are aligned correctly.

**Search Results**

- Any errors found via validators were corrected. The page was tested by searching for several different recipes and ensuring the returned results matched the Mongo database.  All search options appear to be working correctly and returning the expected results.  The search area itself is populated with the original search criteria as expected so the user can see what they originally searched for. Clicking on the Keto Kitchen logo on the top left redirects to the home page. All colour and text is consistant, all all elements are aligned correctly.

#### **External Testing**

**Responsive**
-   Responsive design testing was done using google chrome dev tools to resize the screen on each page, all pages are responsive as intended.

**W3C Markup & CSS Valiadators**
- Used to check validity of HTML and CSS code used in this project, both returned no errors at completion.  W3C did see Jinja as errors even though they were not.

**JSHint**
- Used to check all JS code for errors, none present on completion of this project.

#### **Issues:**

- The preview images for the edit recipe add recipe pages are not working correctly for aspect ration.  In the future some type image size control will be added to handle this problem.

- On edit the image must be added again or it will default to the alt, this will be fixed in a future update.

---

## **Future Updates**

- A functioning modal and user authentication including registration.

- Keyword search bar and more search options.

- User review section and change the current ratings widget to something better.

- Print recipe button.

- Connect to Pinterest.

- Pagination for all sized devices and scroll down arrow for smaller devices.

- Image aspect ratio control for uploaded images.

-   Add in new line functionality for adding and editing recipes.


---

## **Deployment**

This project was created using Visual Studio Code (VSCode).  Preparation for deployment is as follows:

### **Running The Code Locally:**

- Go to my repository https://github.com/Holly-Horwood/keto-kitchen
- Click on the clone or download button
- In the Clone with HTTPs section, click  to copy the clone URL for my repository.
- Open your environment terminal
- Type `git clone` into the command line and then paste my URL that you copied.
- Press enter and the clone will be created.

### **GitHub** ###

All coding was committed and pushed to my Github repository at:

https://github.com/Holly-Horwood/keto-kitchen

It was also published on Github pages at:

https://holly-horwood.github.io/keto-kitchen/

### **Deploying to Github Once Cloned and Edited** ###

- In your terminal type `git add .` to stage all pending updates
- Type `git commit -m "example massage"` add your own message explaining what you are committing.
- Type `git push -u origin master` to push to my repository


### **Heroku**

- I created a new app in heroku called keto-kitchen-hollyci.
<br>
-  In the terminal intiialise a new git repository:
    *    `git init` we want to link the GitHub repo to the app in heroku 
    *   `https://keto-kitchen-hollyci.herokuapp.com/`
<br>
- In VSCode *app.py* set the environment variables for Heroku
    *   ```app.run(host=os.environ.get('IP', '127.0.0.1'),  port=int(os.environ.get('PORT', '8080')),```
<br>
-   Then in *config.py* add:
    *   `MONGO_URI = os.environ.get('MONGO_URI')` 
<br>
- Go back to *Heroku* and in the project under *settings* and *config vars* add: 
    *   `IP = '0.0.0.0'`
    *   `PORT = 5000`
    *   `MONGO_URI = mongodb+srv://nz_user:password@myfirstcluster-clbrq.mongodb.net/keto_kitchen?retryWrites=true&w=majority`
<br>
- Add a *Procfile* with the following:

    *   `echo web: python run.py >Procfile`
    * In the Procfile add `web: python app.py -p $PORT`  *this is how Heroku runs the application*
    * `heroku ps:scale web=1` *This will start the app once it has deployed*

<br>

- Push to Github:
  * In terminal type `git add .`
  * `git commit -m "add a meaningful message here"`
  * `git push -u origin master`
  * enter username:
  * enter password:
<br>
- In Heroku go to the *deploy* tab

- Scroll down to *manual deploy* and select *deploy branch*

- After build is successful go back up and select to *auto deploy*

- Finally login to *Travis* to check testing is still working


---

## **Credits**

**Content:**

All content written by Holly Horwood.

**Media:**

-   Most images were supplied by Pixabay and Flickr
- All other images supplied by Holly Horwood
- Favicon was generated using favicon.io
-   File size uploaded image checker and file preview Javascript Code, Original code courtesy of nkon https://stackoverflow.com/questions/4459379/preview-an-image-before-it-is-uploaded
-   Star ratings widget courtesy of https://rating-widget.com/
-   Google fonts: Kaushan Script

**Acknowledgements:**

Thanks to Sebastian Immel my mentor for all of his help and patience.  Thanks also to the students and staff at Code Institute especially my tutors Sebastian and Dick.





Star ratings app from rating widget https://rating-widget.com/get/rating/javascript/#editor


