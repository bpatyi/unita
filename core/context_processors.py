from core.models import MenuItem

def menuitems(request):
	return {'menu_items':MenuItem.objects.all(),}