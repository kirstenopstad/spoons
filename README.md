# Spoons
#### By Kirsten Opstad
#### A tool for expanding compassion

***

#### Video Demo:  <https://www.youtube.com/watch?v=g32EIWWSJJo&t=8s>
<!-- ![preview](url) -->
***
## Description

Spoons is a web-based application using JavaScript, Python, and SQL. Powered by the dynamic spoon counter, deducts spoons based on activities user selects, simulating the experience of expending energy throughout the day.

Registered users are able to change/update "spoon values" of activities, add new activities to their profile and change their "daily spoon count." Preferences are stored/updated in a SQL database.

Prompted by a conversation with a friend about communicating one's capacity to their partner, the purpose of Spoons is built to help expand compassion between partners, roommates, collaborators & colleagues.

Spoons was built as my final project for CS50.

***
## Technologies Used

* Python
* Flask
* SQL
* HTML
* CSS
* Bootstrap
* Werkzeug

***

## Objectives (MVP)

This application will:
* Display and update daily spoon count based on activities user selects
* Allow authenticated users to:
    * Add new activities
    * Update "spoon value" of activities
    * Update their overall "spoon count"

### __Specification__ (by Route)

#### Index
* ✅ Allow user to add activities to their day
    * ✅ Deduct "spoons" from counter based on activity clicked
    * ✅ Track how many times an activity has been clicked
    * ✅ Once user runs out of "spoons"
        * ✅ Allow simple reset
        * Prompt user to create account to customize
#### Counter
* ✅ Displays user activities organized by spoon value
* ✅ Allows user to add activities to their day & retains dynamic functionality of index
#### Register
* ✅ Allow user to register for an account via form.
    * ✅ Require input of a unique username. Render apology if username is blank or taken.
    * ✅ Require input of password, confirmation of password.  Render apology if password is blank or if don't match.
    * ✅ Submit via post to /register
    * ✅ Store username and hash of password in table users
#### Change (functionality now embedded in profile.html)
* ✅ Allow user to update value of an existing activity
    * ✅ Require input of an activity that exists in table. Render apology if not a valid activity.
    * ✅ Require input of number of spoons. Render apology if negative or not an int.
    * ✅ Store value in table profiles along with user and activity id
    * ✅ Allow user to update their default daily spoon level
#### Add (functionality now embedded in profile.html)
* ✅ Allow user to add a new activity
    * ✅ Require input of title and description. Render apology if blank or if a number.
    * ✅ Require user to set default value. Render apology if not a number
    * ✅ Store title and default value in table activities; store user value in profiles
#### Library (now "Profile")
* ✅ Display activities that user has customized (changed value or added)
* ✅ Ensure no duplicate activities are stored in user values
* Allow users to update spoon count from profile
* Allow users to add activities from profile
* Allow users to change activity spoon value count from profile
* Allow users to remove activity from profile using new route /remove

***

### __Goals__
1. ✅ Meet MVP (Minimum Viable Product)
2. ✅ Support repeat activites on single day with an activity counter
3. Add CRUD functionality from Index

### __Stretch Goals__

#### Share
* Allow user to share their activities & activity values with another user

***

## Process

### Questions considered

- *__What will your software do? What features will it have? How will it be executed?__*
    - Register, login & log out users
    - Track (on a daily basis) quantity of "spoons" used
        - Tasks that require energy reduce spoon count by a given amount
        - Tasks that replenish energy increase spoon count
    - Allow users to create new acivities and assign "spoon" value to them
    - Future features:
        - Allow users to form groups that share a task list (like a roommates using a chore wheel)
- *__What new skills will you need to acquire? What topics will you need to research?__*
    - How to securely store user passwords
    - How to reset a value (number of daily "spoons") based on a new day
- *__If working with one or two classmates, who will do what?__*
    - Working solo
- *__In the world of software, most everything takes longer to implement than you expect. And so it’s not uncommon to accomplish less in a fixed amount of time than you hope. What might you consider to be a good outcome for your project? A better outcome? The best outcome?__*
    - Good:
        - Operable web application that technically meets requirements above (not inlcuding future features)
    - Better:
        - Peer-tested web application that meets requirements and has integrated at least one piece of user feedback
        - Incorporates design aesthetics that improve the user experience (nice graphics)
    - Best:
        - Supports sharing data with other users (see future features).
        - Allows export of CSV of easy-to-read chart that displays:
            - Given set of connected users
            - Tasks & user-defined "spoon" values

***

## Setup/Installation Requirements

*Note: this project was built in the CS50 Codespace. Setup/Installation Requirements forthcoming.*

***

## Known Bugs

* No known bugs. If you find one, please email me at kirsten.opstad@gmail.com with the subject **[_Repo Name_] Bug** and include:
  * BUG: _A brief description of the bug_
  * FIX: _Suggestion for solution (if you have one!)_
  * If you'd like to be credited, please also include your **_github user profile link_**

*** 

## License

MIT License

Copyright (c) 2023 Kirsten Opstad

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
