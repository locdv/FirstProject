from django.contrib import admin

# Register your models here.

from .models import Question, Choice
"""
 đăng kí thông tin được quản lý bởi admin
"""


class ChoiceInline(admin.TabularInline):
    model = Choice
    # cung cấp 3 choice cho một question bởi mặc định
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """
    tạo section để hiển thị thông tin của question
    date thông tin có thể collapse
    """
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    """
    class tham chieu
    """
    inlines = [ChoiceInline]
    # thông tin phụ để hiển thị
    list_display = ('question_text', 'pub_date')
    # trường để filter
    list_filter = ['pub_date']
    # hiển thị box để search theo trường
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
