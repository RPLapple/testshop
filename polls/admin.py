from django.contrib import admin
from .models import Choice, Question


# Register your models here.
# 向管理页面注册了问题Question类。Django 知道它应该被显示在admin後台索引页里
# admin.site.register(Question)
# 你期望能自定义表单的外观(排序)和工作方式。可在注册模型时将这些设置告诉 Django。
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']  # 使得"Publication date"显示在"Question"之前

# 一個個網路上添加Choice內容太沒效率，所以
# 这会告诉 Django：“Choice 对象要在 Question 后台页面编辑。默认提供 3 个足够的选项字段。”
# class ChoiceInline(admin.StackedInline):  # StackedInline佔據的空間太大了所以換一個
class ChoiceInline(admin.TabularInline):    # 表格內聯
    model = Choice
    extra = 3


# **自己project的SQL表單可以用，譬如篩選等等的功能那些（至少管理員可以先設定）
# 拥有数十个字段的表单，你可能更期望将表单分为几个字段集
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]                              # “Choice对象要在Question后台页面编辑。默认提供3个选项。”
    inlines = [ChoiceInline]       # 有三个关联的选项插槽——由extra定义。
                                   # 每次返回已创建对象修改时，会见到三个新的插槽(原三無法刪除）
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 顯示column名
    list_filter = ['pub_date']     # 添加“过滤器”侧边栏，允许人们以 pub_date 字段来过滤列表
    search_fields = ['question_text']  # 后台使用LIKE查询数据，将待搜字段数限为不会出问题大小


admin.site.register(Question, QuestionAdmin)

