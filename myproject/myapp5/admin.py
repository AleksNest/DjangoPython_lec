from django.contrib import admin
from .models import Category, Product


@admin.action(description="сбросить кол в ноль")            # тест в действиях админке
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)                     # все значения поля quantity  выбранных в админке категорий станет равно 0


class ProductAdmin(admin.ModelAdmin):   # для изменения отображения модели в админке
    list_display = ['name', 'category', 'quantity']          # в админке будет отображаться в  Product е список 'name', 'category', 'quantity'
    ordering = ['category', '-quantity']                    # сортировка вначале по category по возрастанию, потом по quantity по убыванию
    list_filter = ['date_added', 'price']                      # фильтрация по дате и цене - добавляют в админке справа фильтр
    search_fields = ['description']                         # поиск по полю описание
    search_help_text = 'поиск по описанию'                  # подсказака в поле поиска в админке
    #search_fields = ['description', 'name']                 # Ищет как в столб name и description

    actions = [reset_quantity]                  # в админке устанавливается действие прописанное выше

    #fields = ['name', 'description', 'category', 'date_added', 'rating']                # в админке в каждом продукте отображать только указанные поля
    readonly_fields = ['date_added', 'rating']                                          # эти поля только для чтения
    fieldsets = [                                                                       #детализированное измсенение в кадминке вида продукции
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'катиегория товара и его описание',
                'fields': ['category','description'],
            },
        ),
        (
            'бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            },
        ),
        (
            'рейтинг',
            {
                'description': 'автоматический расчет рейтинга',
                'fields': ['rating', 'date_added'],
            },
        ),
    ]





admin.site.register(Category)               #подключение модели Category к админке
#admin.site.register(Product)
admin.site.register(Product, ProductAdmin)      #подключение модели Product и  ProductAdmin к админке

