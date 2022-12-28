from django_filters import rest_framework as filters

class CharFilterInFilters(filters.BaseInFilter, filters.CharFilter):
    pass

class ArticleFilter(filters.FilterSet):
    category = CharFilterInFilters(field_name='category__title', lookup_expr='in')


