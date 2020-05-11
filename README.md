# Massage.ify

https://massage-ify.herokuapp.com/techniques/

Learn and calloborate with a community of people dedicated to health and living a pain free life. Whether you're looking how to self manage pain, or how to provide bodywork to another person, there's something for everyone.

Explore an instructional index of massage styles, approaches and specific techniques. Collect favorite moves, create playlists with different time intervals that can be used for all day reminders to take stretch breaks, or setup an hour to follow a massage/stretching protocal. Anything is possible.

Submit your own massage techniques to the community to share your knowledge!

## Index

- [Authors](#authors)
- [Scope](#scope)
- [User Stories](#user-stories)
- [Wireframes](#wireframes)
- [Data Models](#data-models)
- [Future Updates](#future-updates)

## Getting Started

A place to collect and share body maintenace approaches and techniques. Submit your own ideas and styles to the community.
Create playlists with timers that can run all day to give you stretch break reminders or just to help stay on track while providing a massage to someone else for a set interval.

Create a profile, start browsing the index of techniques. Add to your favorites and create a playlist with your favorites. You can use the massage timer from the playlist page, it will automatically be set depending on how long each technique is. Stay tuned for updates.

## Authors

- **Tina Taylor** - https://github.com/longevitytina - https://www.linkedin.com/in/tina-taylor-codes/

## Scope

##### Technologies used:

- [Python](https://www.python.org) - Language
- [Django](https://www.djangoproject.com) - Web framework
- [Heroku](https://www.heroku.com) - Deployment
- [Bootstrap](https://getbootstrap.com) - Styling

## User Stories

##### Sprint 1: Basic Auth & Profiles

- Basic splash page

  - Login
  - Register

- Profile page - photo default - edit profile - list of playlists
- Navbar - Login or Logout - Massage index
- Seed data - massage techniques - playlists
- Index of favorite massage techniques
- Massage technique details page

##### Sprint 2: Techniques CRUD

- User can delete massage techniques from their favorites
- User can add massage techniques to favorites from the massage techniques index - Stretch: or from other user’s profiles/playlists

##### Sprint 3: Playlists

- User can create a massage playlist that saves to their profile - playlist adds techniques from the favorites index or global index
- User can edit a playlist - name, picture, add/delete techniques, adjust time
- Admin can edit or add new techniques to global index - Stretch: Users can submit a technique, but must it be approved before adding it to the global index?

##### Sprint 4: Playlist modes

- Add different playlist modes: - Self massage - interval timing for full day use - Partner massage - timer for continuous amount

## Wireframes

##### Profile Page

![Wireframe3](/wasteland//main_app/img/ss3.png)

<img src="/main_app/static/Images/profile.png" width="200" height="200">

##### Playlist Page

<img src="/main_app/static/Images/playlist_view.png" width="200" height="200">

##### Create Playlist Page

<img src="/main_app/static/Images/playlist_create.png" width="200" height="200">

##### Technique Index Page

<img src="/main_app/static/Images/tech_index.png" width="200" height="200">

##### Technique Detail Page

<img src="/main_app/static/Images/technique_detail.png" width="200" height="200">

## Data Models

<img src="/main_app/static/Images/Datamodels.png" width="200" height="200">

## Future Updates

##### Technologies

- Add Spotify playlist API
- Relaunch with React frontend
- Mobile app version - React Native

##### Features

- Edit profile
- Timer settings: User will be able to customize time intervals with alerts
- Submit techniques to the community
  - Users can upload photos and videos
    - Self made content
      - Connect IG, tiktok, etc..
- View other user's playlist and add them to your own profile
- Follow other users
- Various styling changes
  - Techniques in global database will display message that you've added them.
  - More transitions and icons
- Find massage therapist/trainers in your area
  - connect an external search api like yelp, nextdoor
  - Provide a site index of therapist in the website community
    - Provide profile pages for professionals
- Forums
  - Post skill-trade inquiries
  - Post discussions about pain, stories, guidance
- Injury tracker
  - Collect data that shows if methodologies/techniques are working
    - Display graphs to visually represent data
    - Share data with community, tags techniques used

## References

- [Django admin panel customization](https://data-flair.training/blogs/django-admin-customization/)
- [Datamodel builder](https://www.lucidchart.com/)
- [Create super user in script](https://stackoverflow.com/questions/6244382/how-to-automate-createsuperuser-on-django)
- [Split models.py into several files](https://stackoverflow.com/questions/6336664/split-models-py-into-several-files)
- [Extra fields on many-to-many relationships](https://docs.djangoproject.com/en/dev/topics/db/models/#extra-fields-on-many-to-many-relationships)
- [Random pic generator](https://source.unsplash.com/)
- [ManyToMany convert queryset iteration ](https://stackoverflow.com/questions/45768190/typeerror-manyrelatedmanager-object-is-not-iterable)
- [is_authenticated](https://docs.djangoproject.com/en/2.0/topics/auth/default/#limiting-access-to-logged-in-users)

- [Bootstrap profile page starter](https://bootstrapious.com/p/bootstrap-profile-page)
- [Sortable list library](https://github.com/SortableJS/Sortable)
- [Collectstatic error](https://stackoverflow.com/questions/36665889/collectstatic-error-while-deploying-django-app-to-heroku)
- [Display Timer](https://www.freecodecamp.org/forum/t/return-in-setinterval/186389/8)

- [Align buttons](https://stackoverflow.com/questions/20962483/how-do-i-make-two-bootstrap-buttons-side-by-side/20962556)
- [Modeling playlists](https://stackoverflow.com/questions/4799378/best-way-to-make-a-simple-orderable-playlist-in-django)
