from .models import Expense

from tastypie.resources import ModelResource

class ExpenseResource(ModelResource):

    class Meta:
        resource_name = 'expenses'
        queryset = Expense.objects.all()