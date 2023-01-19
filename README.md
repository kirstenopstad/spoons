# SPOONS
#### Video Demo:  <https://www.youtube.com/watch?v=g32EIWWSJJo&t=8s>
#### Description:

- Spoons is a web-based application using JavaScript, Python, and SQL.

## Getting Started
### Questions to consider:

- What will your software do? What features will it have? How will it be executed?
    - Register, login & log out users
    - Track (on a daily basis) quantity of "spoons" used
        - Tasks that require energy reduce spoon count by a given amount
        - Tasks that replenish energy increase spoon count
    - Allow users to create new acivities and assign "spoon" value to them
    - Future features:
        - Allow users to form groups that share a task list (like a roommates using a chore wheel)
- What new skills will you need to acquire? What topics will you need to research?
    - How to securely store user passwords
    - How to reset a value (number of daily "spoons") based on a new day
- If working with one or two classmates, who will do what?
    - Working solo
- In the world of software, most everything takes longer to implement than you expect. And so it’s not uncommon to accomplish less in a fixed amount of time than you hope. What might you consider to be a good outcome for your project? A better outcome? The best outcome?
    - Good:
        [] Operable web application that technically meets requirements above (not inlcuding future features)
    - Better:
        [] Peer-tested web application that meets requirements and has integrated at least one piece of user feedback
        [] Incorporates design aesthetics that improve the user experience (nice graphics)
    - Best:
        [] Supports sharing data with other users (see future features).
        [] Allows export of CSV of easy-to-read chart that displays:
            - Given set of connected users
            - Tasks & user-defined "spoon" values

## Goal Milestones
    [X] Create SQLite database spoons.db
    ### Index
        [X] Allow user to add activities to their day
            [X] Deduct "spoons" from counter based on activity clicked
            [X] Track how many times an activity has been clicked
            [X] Once user runs out of "spoons"
                [X] Allow simple reset
                [] Prompt user to create account to customize
    ### Counter
        [X] Displays user activities organized by spoon value
        [X] Allows user to add activities to their day & retains dynamic functionality of index
    ### Register
        [X] Allow user to register for an account via form.
            [X] Require input of a unique username. Render apology if username is blank or taken.
            [X] Require input of password, confirmation of password.  Render apology if password is blank or if don't match.
            [X] Submit via post to /register
            [X] Store username and hash of password in table users
    ### Change (functionality now embedded in profile.html)
        [X] Allow user to update value of an existing activity
            [X] Require input of an activity that exists in table. Render apology if not a valid activity.
            [X] Require input of number of spoons. Render apology if negative or not an int.
            [X] Store value in table profiles along with user and activity id
        [X] Allow user to update their default daily spoon level
    ### Add (functionality now embedded in profile.html)
        [X] Allow user to add a new activity
            [X] Require input of title and description. Render apology if blank or if a number.
            [X] Require user to set default value. Render apology if not a number
            [X] Store title and default value in table activities; store user value in profiles
    ### Library (now "Profile")
        [X] Display activities that user has customized (changed value or added)
        [X] Ensure no duplicate activities are stored in user values
        [] Allow users to update spoon count from profile
        [] Allow users to add activities from profile
        [] Allow users to change activity spoon value count from profile
        [] Allow users to remove activity from profile using new route /remove

    ### Extra Credit:
        #### Share
            [] Allow user to share their activities & activity values with another user
