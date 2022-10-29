# list down all artists
```>>> Artist.objects.all()
<QuerySet [<Artist: Stage_name =abd elhalemSocial_link = https://ar.wikipedia.org/wiki/%D8%B9%D8%A8%D8%AF_%D8%A7%D9%84%D8%AD%D9%84%D9%8A%D9%85_%D8%AD%D8%A7%D9%81%D8%B8>, <Artist: Stage_name =AdeleSocial_link = https://www.instagram.com/adele/>, <Artist: Stage_name =Dr dreSocial_link = https://www.instagram.com/drdre/>]>
```
# list down all atrits sorted by name
```>>>Artist.objects.order_by('stage_name')
<QuerySet [<Artist: Stage_name =AdeleSocial_link = https://www.instagram.com/adele/>, <Artist: Stage_name =Dr dreSocial_link = https://www.instagram.com/drdre/>, <Artist: Stage_name =abd elhalemSocial_link = https://ar.wikipedia.org/wiki/%D8%B9%D8%A8%D8%AF_%D8%A7%D9%84%D8%AD%D9%84%D9%8A%D9%85_%D8%AD%D8%A7%D9%81%D8%B8>]>
```
# list down all names starts with a
```>>> Artist.objects.filter(stage_name__startswith="a")
<QuerySet [<Artist: Stage_name =abd elhalemSocial_link = https://ar.wikipedia.org/wiki/%D8%B9%D8%A8%D8%AF_%D8%A7%D9%84%D8%AD%D9%84%D9%8A%D9%85_%D8%AD%D8%A7%D9%81%D8%B8>, <Artist: Stage_name =AdeleSocial_link = https://www.instagram.com/adele/>]
```
#  in 2 different ways, create some albums and assign them to any artists
 
 ```
>>> a = Album( artist_fk = Artist.objects.get(pk=1) , creation_time = timezone.now(),release_time = timezone.now(),album_cost = '500.38')
>>> a.save()
------------------------------------------
>>> b = Artist.objects.get(id=2)
>>> album = b.album_set.create( creation_time = timezone.now(),release_time = timezone.now(),album_cost = '200.53')
```
# get the latest released album
```
>>> Album.objects.last()
<Album: name = New Album Artist = Adele>
```
# get all albums released before today
```
>>> Album.objects.filter(release_time__lte = timezone.now()-datetime.timedelta(days=1))
<QuerySet []>
```
# get all albums released today or before but not after today
```
>>> Album.objects.filter(release_time__lte= timezone.now())  
<QuerySet [<Album: name = New Album Artist = abd elhalem>, <Album: name = New Album Artist = Adele>]>
```
# count the total number of albums 
```
>>> Album.objects.count()
2
```
# in 2 different ways, for each artist, list down all of his/her albums
```
>>> Album.objects.get(pk=1)
<Album: name = New Album Artist = abd elhalem>
<Album: name = New Album Artist = Adele>
>>> Album.objects.get(pk=3)
album.models.Album.DoesNotExist: Album matching query does not exist.
---------------------------------------------------
>>> Album.objects.select_related('artist_fk')
<QuerySet [<Album: name = New Album Artist = abd elhalem>, <Album: name = New Album Artist = Adele>]>
```
# list down all albums ordered by cost then by name 
```
>>> Album.objects.order_by('-album_cost' , 'album_name')  
<QuerySet [<Album: name = New Album Artist = abd elhalem>, <Album: name = New Album Artist = Adele>]>
```
