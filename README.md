# SideHustle

This website aims to provide a convenient place to find services that could make people's lives easier, as well as a place where service providers can earn money and hone their skills. 

Why? For the service providers, a formal job can be hard to find, a potentially very big commitment, and, in most cases, unfortuantely, the work is not that enjoyable. This site gives providers an opportunity to find work with hours that suit them, and they can choose to offer services that they would enjoy providing.

For customers, it can be hard to find people to get useful jobs done. From cleaning a wheelie bin to tutoring their kids, this site allows them to find people who are willing to do those jobs. Customers can choose from the list of services already being offered, or they can request a service that they don't see on offer, providing a useful signal to service providers that there is demand for such a service.

There are a few existing websites that offer similar environments, with TaskRabbit, Airtasker, Bizzby and Craiglist likely being the most well known. However, these sites either don't operate in Ireland or are note very popular here. There is scope for the growth of these sort of websites in Ireland, and an Irish-based site like SideHustle may be the best candidate to drive that growth.

The target audience for this site would be anyone who has a skill to offer or anyone who needs help with a problem.

View the live site [here.](https://adam-pp4-workapp.herokuapp.com/)

![Mockup](docs/readme-images/mockup.PNG)

# User-Experience-Design

## The-Strategy-Plane

### Agile Planning

This project was developed using agile methodologies. Epics(milestones) were broken down into User Stories, and then broken down even further into tasks. Acceptance Criteria and Dependcies were also laid out in the User Stories.

The Kanban board was created using github projects and can be located [here](https://github.com/users/adammkeane/projects/5/views/1).

![Kanban image](docs/readme-images/kanban_board.PNG)
![User story example image 1](docs/readme-images/user_story1.PNG)
![User story example image 2](docs/readme-images/user_story2.PNG)

**EPIC 1 - Initial Setup**
- USER STORY: Django Setup & Deployment
- USER STORY: Admin Site
- USER STORY: Post Model

**EPIC 2 - Bulletin Board**

- USER STORY: Bulletin Board
- USER STORY: Split Bulletin Board
- USER STORY: Post Details
- USER STORY: Search Posts

**EPIC 3 - Site Basics**

- USER STORY: Home Page
- USER STORY: Nav Bar/Bootstrap Install
- USER STORY: Footer
- USER STORY: Allauth/User Authorization Management

**EPIC 4 - Post CRUD Model**
- USER STORY: Create Post
- USER STORY: View User's Post (Profile Page)
- USER STORY: Edit Post
- USER STORY: Delete Post

**EPIC 5 - Post Reviews**
- USER STORY: PostReview Model
- USER STORY: Create Post Reviews
- USER STORY: Edit Post Reviews
- USER STORY: View Post Reviews
- USER STORY: Delete Post Reviews

## The-Scope-Plane

* Responsive Design - Site should be fully functional on all devices from 320px up
* Hamburger menu for mobile devices
* Ability to perform CRUD functionality on Post model.
* Some restricted access for signed in users and post creators.

## The-Structure-Plane

### Features

**Bulletin Board**

``USER STORY - As a Site User I can view a paginated list of post so that I can see what services/requests are being offered/solicited and get more information about the ones I'm interested in.``

![Bulletin Board](docs/readme-images/bulletin_board.PNG)
![Bulletin Board2](docs/readme-images/bulletin_board2.PNG)

**Post Reviews**

``USER STORY - As a Site User I can view review scores for posts so that I can have useful information when deciding whether or not I should engage with the post and trust the poster.``

``USER STORY - As a Site User I can create a review of a post so that I can share useful knowledge with other site users.``

![Post Reviews](docs/readme-images/post_reviews.PNG)

**Profile Page**

``USER STORY - As a Site User I can view a User's Profile Page (including mine own), which contains a list of all posts from that User so that I can either keep track of my own posts, or get more information about another Users services/requests.``

``USER STORY - As a Site User I can edit my posts so that I can makes changes after the initial posting.``

``USER STORY - As a Site User I can delete my posts so that I can remove posts that I have no more need for.``

![Post Reviews](docs/readme-images/profile_page.PNG)

## The-Skeleton-Plane

### Wireframes

- Home Page


![Home Page](docs/readme-images/home_page_wireframe.PNG)


- Bulletin Board


![Bulletin Board](docs/readme-images/bulletin_board_wireframe.PNG)

- Bulletin Home

![Bulletin Home](docs/readme-images/bulletin_home_wireframe.PNG)

- Post Detail

![Post Detail](docs/readme-images/post_detail_wireframe.PNG)

- Profile Page

![Profile Page](docs/readme-images/profile_page_wireframe.PNG)

## Technologies

* HTML
    * The structure of the Website was developed using HTML as the main language.
* CSS
    * The site was styled using custom CSS in an external file.
* Javascript
    * The site was given interactivity using a mixture of custom and adapted JS in two external files.
* GitHub
    * Source code is hosted on GitHub and delpoyed using Git Pages.
* Git 
    * Used to commit and push code during the development opf the Website
* Font Awesome
    * Icons obtained from https://fontawesome.com/ were used as the Social media links in the footer section. 
* TinypNG
    * https://tinypng.com/ was used to reduce the size of the images used throughout the website
* Favicon.io
    * favicon files were created at https://favicon.io/

## Testing 

### Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px x 634px and upwards as defined in [WCAG 2.1 Reflow criteria for responsive design](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html) on Chrome, Edge, Firefox and Opera browsers.

Steps to test:

1. Open browser and navigate to [Know Ya Countries](https://adammkeane.github.io/know-ya-countries/)
2. Open the developer tools (right click and inspect)
3. Set to responsive and decrease width to 320px and height to 634px.
4. Set the zoom to 50%
5. Click and drag the responsive window to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched.
No horizontal scroll is present.
No elements overlap.

Actual:

The score and question number section on the quiz page went onto 2 lines on the small screen sizes. To fix this, media queries were used to made that text smaller on smaller screens.

Website was also opened on the following devices and no responsive issues were seen:

- Google Pixel 3a
- Dell XPS 15
- iPhone Mini


### Accessibility

[Wave Accessibility](https://wave.webaim.org/) tool was used throughout development and for final testing of the deployed website to check for any aid accessibility testing.

Testing was focused to ensure the following criteria were met:

- All forms have associated labels or aria-labels so that this is read out on a screen reader to users who tab to form inputs
- Color contrasts meet a minimum ratio as specified in [WCAG 2.1 Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user
- All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions
- All not textual content had alternative text or titles so descriptions are read out to screen readers
- HTML page lang attribute has been set
- Aria properties have been implemented correctly
- WCAG 2.1 Coding best practices being followed

### Functional Testing

**Navigation Links**
Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

| Navigation Link | Page to Load    |
| --------------- | --------------- |
| Know Ya Countries text and Home icon in navigtion bar | index.html      |
| Capital Cities of Asia Quiz on home page | asia-capitals.html |

Links on all pages navigated to the correct pages as exptected.

**Game Testing**
| Test Case # | Description                                                                                                                                                               | Steps                                                                                                                                                                                                                                            | Expected                                                                                                                                                                                                                                                                                         | Actual      | Pass/Fail |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | --------- |
| 1           | Test correct answer feedback functioning correctly                                                                                                                        | 1\. Start game.<br>2\. Answer question correctly.                                                                                                                                                                                                | 1.Green background color added to input field and text feedback.<br>2\. Text feedback appears saying that we were correct.<br>3\. Input field, dropdown arrow and check answer button disabled.<br>4\. Focus taken away from the input field.                                                    | As expected | Pass      |
| 2           | Test inccorrect answer feedback functioning correctly                                                                                                                     | 1\. Start game.<br>2\. Answer question incorrectly.                                                                                                                                                                                              | 1\. Red background color added to input field and text feedback.<br>2\. Text feedback appears saying that we were incorrect.<br>3\. Input field, dropdown arrow and check answer button disabled.<br>4\. Focus taken away from the input field.                                                  | As expected | Pass      |
| 3           | Test invalid answer feedback functioning correctly                                                                                                                        | 1\. Start game.<br>2\. Answer question invalidly (not exactly matching a dropdown list option).                                                                                                                                                  | 1.Yellow background color added to input field and text feedback.<br>2\. Text feedback appears saying that we had invalid guess.<br>3\. Check answer button disabled.<br>4\. All other fields/buttons remained active.<br>5\. Input field emptied.<br>6\. Focus taken away from the input field. | As expected | Pass      |
| 4           | Test is all countries appeared in the quiz and not double ups.                                                                                                            | 1\. Start game.<br>2\. Answer every question.<br>3\. console.log the country object half way through and before last question of the quiz.                                                                                                       | 1\. Each country that we've already answered is being removed from the countries object.<br>2\. By last question, the console.log should should just one option for the last renaming country.                                                                                                   | As expected | Pass      |
| 5           | Test score and question number were being updated correctly.                                                                                                              | 1\. Start game.<br>2\. Play full quiz,during which I answering 3 random questions correctly.                                                                                                                                                     | 1\. My score at the end should be 3.<br>2\. The question number at the end should be 50/50.                                                                                                                                                                                                      | As expected | Pass      |
| 6           | Test Jerusalem didn't appear twice in the dropdown options list, and that the one option was deemed correct for both Israel and Palestine (More details in bugs section). | 1\. Start game.<br>2\. Click dropdown arrow to see all options. If we see only one instance of Jerusalem, move on to step 3.<br>3\. Skip ahead until we see both Israel and Palestine. For both, select the sole Jerusalem option as the answer. | 1\. Jerusalem only appears once in the dropdown list.<br>2\. When its selected as the answer for both Israel and Palestine, we get the correct answer feedback, as mentioned in Test Case #1.                                                                                                    | As expected | Pass      |
| 7           | Test modal functioning correctly on both home page and capitals of Asia quiz page.                                                                                        | 1\. Load home page.<br>2\. Click how to play button. Close modal if it opens.<br>3\. Click on question mark in the nav bar. Close modal if it opens.<br>1\. Start game.<br>2\. Click on question mark in the nav bar. Close modal if it opens.   | 1\. Modal opens when either the how to button or the question mark is clicked on both pages.<br>2\. Modal can be closed by clicking on the gray out background or the X button at the top right of the modal.                                                                                    | As expected | Pass      |
| 8           | Test end of quiz functionality.                                                                                                                                           | 1\. Start game.<br>2\. Click next until you reach the end.<br>3\. Click replay button.                                                                                                                                                           | 1.Pink background color added to input field and text feedback.<br>2\. Input field, dropdown arrow, check answer button and next button disabled.<br>3\. Replay button appears. When clicked, it reloads the page and the quiz start again.                                                      | As expected | Pass      |

**Footer Social Media Icons / Links**
Testing was performed on the Font Awesome Social Media icons in the footer to ensure that each one opened in a new tab and that each one had a hover affect of the orange branding color.

Each item opened a new tab when clicked as expected and correct hover color was present.

### Validator Testing 

- HTML
  - No errors were found when passing through the official [W3C validator](https://validator.w3.org)

![Index HTML Test](docs/readme-images/index-w3-html-test.PNG)

![Asia Quiz HTML Test](docs/readme-images/asia-quiz-w3-html-test.PNG)

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)

![CSS Test](docs/readme-images/w3c-css1.PNG)
![CSS Test2](docs/readme-images/w3c-css2.PNG)

- JS
  - No major errors were found when passing through the [JSHint](https://jshint.com/)
  - The displayNames variable is actually a function that is being called on an onclick attribute, as opposed to a variable. 
  - I couldn't figue out the warning about the for in loop.

![Javascript Test](docs/readme-images/jshint.PNG)

### Bugs
- Flavicon emblem was not showing up on deployed site, but it was showing up on the site generated from the GitPod workspace. From searching online, after being pointed in the right direction by my very helpful mentor, I found that this was caused by using absolute files paths, instead of relative files paths, for my Flavicon images. When changed to relative files paths, the Flavicon emblems did show up when using the deployed site.

- On mobile devices, when I delete the last character in the guess input field, the check answer button doesn't get disabled. I need to click backspace one extra time, when inout field is already empty, for the check answer button to disable. Couldn't find a fix for this. I experimented with using touchend event as well as the keyup event, but I couldn't get this to work. This problem does not exist on desktop version of the site.

- By playing through a full game, I noticed that options in the dropdown list were getting deleted when the already answered countries were being removed from the games. To fix this, I made the dropdown list options reference a separate data source for its content, an array containing all the captials.

- After adding the score and question number tracking feature, I found that correct answere were being taken away from the total questions. If i get 2 correct scores, I only end up with 48 questions. It turns out I was deleting object keys within the check answer function, as well as in the next function. Removed the deleing from the check answer function and that solved the problem.

- Jerusalem is argued to be the capital of both Israel and Palestine. This meant that two Jerusalem options were showing up in the dropdown list and only one was correct when either Israel or Palestine is asked. To fix this, I added a continue for Palestine in the loop that generated the dropdown list and added a condition to accept any answer with the Jerusalem text as the correct answer for Palestine.

- Found it was annoying having to keep selecting the guess input field with each new question, so used the run game function, triggered by the next button, to control focus and put the focus back to the guess input field with every new question.

- Question number was increasing 1 beyond total number of questions at end of quiz before user inputs disabled. To fix, I had to create a new check in the next function to not increase the question number when it got down to the last country in the country list object.


## Deployment

### Version Control

The site was created using the Visual Studio code editor and pushed to github to the remote repository ‘tacos-travels’.

The following git commands were used throughout development to push code to the remote repo:

```git add .``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m 'commit message'``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Deployment to Github Pages

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the menu on left select 'Pages'
  - From the source section drop-down menu, select the Branch: main
  - Click 'Save'
  - A live link will be displayed in a green banner when published successfully. 

The live link can be found here - https://adammkeane.github.io/know-ya-countries/index.html

### Clone the Repository Code Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now of been cloned on your local machine for use.

## Credits 
Thanks to mentor Daisy McGirr for her help with the project.







