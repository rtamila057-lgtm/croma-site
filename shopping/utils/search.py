from django.db.models import Q

def apply_search(queryset, request, fields):
    q = request.GET.get('q')

    if q:
        query = Q()

        for field in fields:
            query |= Q(**{f"{field}__icontains": q})

        return queryset.filter(query)

    return queryset