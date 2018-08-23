from django.contrib.admin import SimpleListFilter
from django.db.models import Q
from django.contrib.admin.filters import AllValuesFieldListFilter

from django.utils.translation import gettext_lazy as _


class InputFilter(SimpleListFilter):
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice



class ProjectFilter(InputFilter):
    parameter_name = 'name'
    title = _('Name')
    def queryset(self, request, queryset):
        term = self.value()
        if term is None:
            return
        any_name = Q()
        for bit in term.split():
            any_name &= (
                Q(name__icontains=bit)
            )
            return queryset.filter(any_name)

# class PriceFilter(InputFilter):
#     parameter_name = 'price2'
#     title = _('Price')
#     def queryset(self, request, queryset):
#         term = self.value()
#         if term is None:
#             return
#         any_name = Q()
#         for bit in term.split():
#             any_name &= (
#                 Q(price2 = bit)
#             )
#         return queryset.filter(any_name)


class PriceFilter(SimpleListFilter):
    parameter_name = 'price2'
    title = _('Price')
    def lookups(self, request, model_admin):
        return (
            ('0', _('0-5')),
            ('1', _('6 - 10')),
            ('2', _('11 - 20')),
            ('3', _('21 - 30')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(price2__gte=0, price2__lte=5)

        if self.value() == "1":
            return queryset.filter(price2__gte=6, price2__lte=10)

        if self.value() == "2":
            return queryset.filter(price2__gte=11, price2__lte=20)

        if self.value() == "3":
            return queryset.filter(price2__gte=21, price2__lte=30)



