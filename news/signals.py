from django.contrib.comments.signals import comment_will_be_posted
from django.contrib.comments.models import Comment
from django.http import HttpResponseRedirect

from django.dispatch import Signal
latest_news_created = Signal(providing_args=["title","content","slug"])


#def unapprove_comment(sender, **kwargs):
#	the_comment = kwargs['comment']
#	the_comment.is_public = False
#	return True
#	
#comment_will_be_posted.connect(unapprove_comment)




    

