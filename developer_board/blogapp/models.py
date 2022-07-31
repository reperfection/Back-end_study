from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
#이렇게만 만든다면 어떤 문제? 어떤 게시글에 해당하는 댓글인지 남겨줘야 한다.
#어떤 게시물인지를 참조해야 한다. 이 블로그 객체를 참조해야 한다.
#밑의 post는 어떤 게시물에 달려있는 댓글인지를 알 수 있는, 댓글이 달린 그 게시물이 쓰임=>Foreign Key를 쓴다
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    #이 댓글은 블로그에 종속적인 데이터. 게시글이 삭제되면 댓글도 덩달아 삭제되어야 한다.
    #이 포스트가 삭제된다면, 게시글이 삭제된다면 참조하고 있는 그 댓글, comment객체도 삭제한다는 의미
    
    def __str__(self):
        return self.comment