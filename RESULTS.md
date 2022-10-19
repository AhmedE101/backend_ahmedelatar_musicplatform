# create some artists


>>> a = Artist( stage_name = "abd elhalem" , social_link = 'https://ar.wikipedia.org/wiki/%D8%B9%D8%A8%D8%AF_%D8%A7%D9%84%D8%AD%D9%84%D9%8A%D9%85_%D8%AD%D8%A7%D9%81%D8%B8')
>>> a.save()

# list down all atrists

>>> Artist.objects.all()
<QuerySet [<Artist: stage_name =abd elhalem social_link = https://ar.wikipedia.org/wiki/%D8%B9%D8%A8%D8%AF_%D8%A7%D9%84%D8%AD%D9%84%D9%8A%D9%85_%D8%AD%D8%A7%D9%81%D8%B8>]>

# list down all artists sorted by name

>>> Artist.objects.order_by('-stage_name')
<QuerySet [<Artist: Stage_name =abd elhalem social_link = https://ar.wikipedia.org/wiki/%D8%B9%D8%A8%D8%AF_%D8%A7%D9%84%D8%AD%D9%84%D9%8A%D9%85_%D8%AD%D8%A7%D9%81%D8%B8>]>

# list down all artists whose name starts with a 

>>> Artist.objects.filter(Stage_Name__startswith='a')
<QuerySet [<Artist: Stage_name =abd elhalem social_link = https://ar.wikipedia.org/wiki/%D8%B9%D8%A8%D8%AF_%D8%A7%D9%84%D8%AD%D9%84%D9%8A%D9%85_%D8%AD%D8%A7%D9%81%D8%B8>]>
>>> Artist.objects.filter(stage_name__startswith='z')
<QuerySet []>

# two different , creating albums and assign them to any artists

>>> a = Album ( artist_fk = Artist.objects.get(pk=1) , creation_time = timezone.now() , release_Time = timezone.now() , album_cost='200.50')
>>> a.save()
-------------------------------

>>> b = Artist.objects.get(id=2)
>>> album = b.album_set.create(creation_time = timezone.now() , release_time = timezone.now() , album_cost = '500.3')


# get all albums released today or before but not after today

>>>  Album.objects.filter(release_time__lte = timezone()-datetime.timelta(days=1 ) )
(due to creation time i will do it later but idea is understood)

# get all albums released before today

>>> import datetime
>>> Album.objects.filter(release_Time__lte = timezone.now()-datetime.timelta(days=1))

(same point above)

# count the total number of albums

>>> Album.objects.count()

# list down all albums orderd by cost then 

>>> Album.objects.order_by('-album_cost' , 'album_name')


