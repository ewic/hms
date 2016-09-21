# UDN2 

A mini UDN app built for Harvard Med School code test.

You can find my slow descent into madness via a series of progressively less helpful commit messages on my github here: `http://github.com/ewic/hms`

Requirements

* Python3

## Starting the app

Make the models

```
python manage.py makemigrations
python manage.py migrate
```

Start the dev server

```
python manage.py runserver
```

Access to the site is via `http://localhost:8000/udn2`.

## Answers to questions

1. **What are some measures we could take to secure this application? Not everyone should be able to see the information entered by participants.**

I'm not too sure about the security of SQLite itself, but I would imagine that as a lightweight prototyping database, it would be inadequate for medical records.  I would first change the choice of storage to something more robust and proven, such as MariaDB or PostGres.

For the web server, I don't think there's any reason to stray far from the traditional and proven choices of things like Apache or nginx.  Web servers such as these would be able to handle encrypted traffic via SSL or what have you, so client to server communication would be secure.

If all data entry were expected to be only done from a single location or set of locations, it wouldn't be unreasonable to restrict access to the app via ip address.  While this protection would be susceptible to an ip spoofing attack, I think if an institution is supplying its own ips and maintaining its own DNS, then we could trust our security as far as we trust those systems.

I used Django's built-in form validation for new participant entry, however I did no such thing when saving the status update to a participant instance.  This means that we are most likely vulnerable to some kind of form injection attack on that end.  The Participant model's status field was created using Django's CharField Choice functionality.  Hopefully this means that it won't listen to attempts to change the value to something outside of the list of choices, but I don't know for sure.

2. **What are some ways in which the above mentioned workflow could be made more dynamic from a UI/UX perspective?**

In my experience, a smooth workflow, especially for non-technical users, is one where everything important is clear and central to the view, and the flow of information is demonstrated with visual cues.  Above all, the goal should be to avoid confusion and provide a clear pathway to step through a site.  However it is important not to alienate or frustrate experienced users by intentionally slowing progress through a site in favor of making it more accessible.  I think it is possible to have a happy marriage of the two design paradigms.

For instance, if a client is in a multi-step data entry process, with 2 or more views encompassing a complete interaction, every time a client moves to the next step in the process, there should be a visual indicator that they are progressing as well as a clear pathway to get back to the previous step.  This can be something like a scrolling or sliding animation, or a clear flowchart listing all the steps and which one the user is on.

With this in mind, I would make sure to include a complete site navigation in the mess that I made.  I would also introduce a proper templating or layout framework.  I have experience with Bootstrap, but I have heard of other libraries such as ReactJS being used.

Ideally, I would create the entire app seperate from the API.  While I learned a lot about Django and its capability to produce a complete front-end, my experience has been that the two should be split apart from each other.  This way you can change one without affecting the other.  This means that the Django API would **only** be responsible for the storage, validation, and most likely transformation of data.  Whatever front-end is made would **only** responsible for the retrieval and display of data.  Inputting data would be done via exposing an endpoint on the API that would intake simple data.  This way the front end can emit simple structures such as raw JSON without knowing anything about the system its emitting to.  It would be up to the API to process bad data and respond with errors or what have you.

## Wait, why do you have udn2?  What happened to udn1?

So when I originally got the assignment, I quickly read the requirements and was off to the races.  Unfortunately, I got some crazy idea to store genetic mutations and environmental exposures as seperate models, this way it would be possible to perform analytics based on these parameters.  Django supported the Many to Many model field type, so it looked like it would be relatively simple.

As I continued working on it, I continued adding features that I thought would be neat and fixing the bugs that would crop up as a result and before I realized it, I had produced something wildly out-of-scope and overengineered given the requirements.  This includes multiple views to read and edit the extra models I had made, multiple forms corresponding to said models, and a bunch of workarounds in the models themselves to deal with the fact that actual participant model instance was now spidering out across several models... 

The result is a wildly incomplete but potentially much more capable application employing multiple Django-centric solutions found across the lands of StackOverflow.   It had no hope of being finished within a reasonable time.

Thus, I made udn2 in the past couple hours, which does everything it needs to and nothing more.  I included the half-written original documentation below, if you would like to read it, as well as the code, located in the `/udn/` folder.  Additionally the `udn` app is installed and started up alongside `udn2`, and has its admin functionality enabled.  To create a new admin you will have to create one via `python manage.py createnewsuperuser`, but `udn2` does not have any admin capabilities set up because it wasn't in the requirements.  <3

# UDN1

A mini undiagnosed diseases network app built in Django for Harvard Med School code test.

So I started 

Built with <3.

## Starting the app

Should be pretty straightforward.  I did not use my own DB solution, SQLite does everything I need.

Requirements:

* python3

```
# Register and make models
$ python manage.py makemigrations
$ python manage.py migrate

# Start the server
$ python manage.py runserver
```

## Models

### Participants
The participants in the study or database.  Contains name and date of birth attributes.  Age is calculated via `getAge()` method using the date of birth.

Associated environmental exposures and genetic mutations are connected via many-to-many relationship.  This allows the app the ability to sort and identify participants based on these attributes and might be helpful later on down the line.

Methods `getEnvironmentalExposures()` and `getGeneticMutations()` do exactly what you expect.

### Environmental Exposures and Genetic Mutations
For this example, these are identical.  Only a name and description attribute, but I assume some smart scientist somewhere might want them to be more capable.

## Views

### Form view
The form view will dynamically switch based on the context it receives.  Thus, any new object entry will have the same entry point.  This might bite us later on down the line if the app were to grow, but it's not a crazy idea to split off future forms into their own view and even group associated forms in this way.

### Participant View
Lists all the relevant attributes for the given participant.  Also provide s entry into the new gm and new ee forms.

### Participant List View
Lists all the participants entered into the system.