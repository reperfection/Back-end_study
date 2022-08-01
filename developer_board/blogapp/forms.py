from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    
class BlogModelForm(forms.ModelForm):
    class Meta: #메타클래스 하에
        model = Blog #어떤 모델을 기반으로 자동으로 입력받을 건지 명시
        #어떤 값, 필드를 입력받을지 쓴다
        fields = '__all__' # 모든 필드 사용
        #fields = ['title', 'body']#특정 필드만 사용 시 리스트를 작성
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['comment']