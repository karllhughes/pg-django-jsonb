# Django + Postgres JSONB

Start the containers: `docker-compose up -d` 
Run the migrations: `docker-compose exec web python manage.py migrate`
Enter the Python shell: `docker-compose exec web python manage.py shell`
Run model commands: 

```python
from pgdjangojsonb.models import Profile

# Get all Profiles:
Profile.objects.all()

# Create a Profile without preferences:
p = Profile(name="Sam", preferences={})
p.save()

# Create a Profile with preferences
p = Profile(name="Bill", preferences={'receive_emails': True, 'favorite_car': 'Tesla'})
p.save()

# Filter Profiles by preferences
Profile.objects.filter(preferences__receive_emails=True)

# Check the query that Django is running
print(Profile.objects.filter(preferences__receive_emails=True).query)

```
