from django.contrib import admin
from .models import Order, OrderLineProductItem, OrderLineTicketItem


class OrderLineProductItemAdminInline(admin.TabularInline):
	model = OrderLineProductItem
	readonly_fields = ('productlineitems_total',)


class OrderLineTicketItemAdminInline(admin.TabularInline):
	model = OrderLineTicketItem
	readonly_fields = ('ticketlineitems_total',)


class OrderAdmin(admin.ModelAdmin):
	inlines = (OrderLineProductItemAdminInline,
			   OrderLineTicketItemAdminInline,)

	readonly_fields = ('order_number', 'date', 'delivery_cost',
					   'order_total', 'grand_total',)

	fields = ('order_number', 'date', 'full_name', 'email',
		      'phone_number', 'country', 'postcode',
		      'town_or_city', 'street_address1', 
		      'street_address2', 'county', 'delivery_option',
		      'click_and_collect_option', 'delivery_cost',
		      'order_total', 'grand_total',)

	list_display = ('order_number', 'date', 'full_name',
					'order_total', 'delivery_cost',
					'grand_total',)

	ordering = ('-date',)

admin.site.register(Order, OrderAdmin)