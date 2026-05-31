from django.contrib import admin

from .models import AskClick, DateProposal, FoodOption, SiteContent, TimeSlot


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteContent.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FoodOption)
class FoodOptionAdmin(admin.ModelAdmin):
    list_display = ('label', 'emoji', 'slug', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('label',)}


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('label', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(DateProposal)
class DateProposalAdmin(admin.ModelAdmin):
    list_display = ('status_label', 'food_choice', 'date', 'time_slot', 'said_yes', 'completed', 'updated_at')
    list_filter = ('completed', 'said_yes', 'date')
    readonly_fields = ('created_at', 'updated_at', 'said_yes_at', 'food_chosen_at', 'scheduled_at')


@admin.register(AskClick)
class AskClickAdmin(admin.ModelAdmin):
    list_display = ('choice', 'created_at')
    list_filter = ('choice',)
    readonly_fields = ('choice', 'created_at')
