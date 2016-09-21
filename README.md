# UDN2 

A mini UDN app built for Harvard Med School code test.

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

## 

## Wait, why udn2?  What happened to udn1?

So when I originally got the assignment, I quickly read the requirements and was off to the races.  Unfortunately, I got some crazy idea to store genetic mutations and environmental exposures as seperate models, this way it would be possible to perform analytics based on these parameters.  Django supported the Many to Many model field type, so it looked like it would be relatively simple.

As I continued working on it, I continued adding features that I thought would be neat and fixing the bugs that would crop up as a result and before I realized it, I had produced something wildly out-of-scope and overengineered given the requirements.  This includes multiple views to read and edit the extra models I had made, multiple forms corresponding to said models, and a bunch of workarounds in the models themselves to deal with the fact that actual participant model instance was now spidering out across several models... 

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