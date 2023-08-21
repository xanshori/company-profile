from django.contrib import admin 
from .models import Intro,AboutUs,MenuServices,Services

# Register your models here.
@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    list_display=['title','is_published','created_at']
    min_objects = 1
    actions = None
    search_fields=['title']
    readonly_fields=['created_at']
    
    def has_delete_permission(self, request, obj=None):   
        queryset = self.model.objects.all()
        if queryset.count() <= self.min_objects:
            return False
        else:
            return super().has_delete_permission(request, obj)
        
    def get_readonly_fields(self, request, obj=None):
        if obj is None: 
            return self.readonly_fields
        else:
            queryset = self.model.objects.all()
            if queryset.count() <= self.min_objects:
                return self.readonly_fields + ['is_published']
            else:
                return self.readonly_fields
    
    
            


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display=['title','is_published','created_at']
    min_objects = 1
    actions = None
    search_fields=['title']
    readonly_fields=['created_at']
    
    def has_delete_permission(self, request, obj=None):   
        queryset = self.model.objects.all()
        if queryset.count() <= self.min_objects:
            return False
        else:
            return super().has_delete_permission(request, obj)
        
    def get_readonly_fields(self, request, obj=None):
        if obj is None:  # Tidak ada objek yang ada (sedang membuat baru)
            return self.readonly_fields
        else:
            queryset = self.model.objects.all()
            if queryset.count() <= self.min_objects:
                return self.readonly_fields + ['is_published']
            else:
                return self.readonly_fields
 

@admin.register(MenuServices)
class AdminMenuServices(admin.ModelAdmin):
    pass

@admin.register(Services)
class AdminServices(admin.ModelAdmin):
    pass