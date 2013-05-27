from core.models import MenuItem, SubMenu

def menuitems(request):
    menu_items = MenuItem.objects.all()

    submenus = {}

    for menu in menu_items:
        if menu.only_mainmenu == True:
            submenus[menu.title] = SubMenu.objects.filter(menu=menu)

    return {'menu_items':MenuItem.objects.all(), 'submenus': submenus,}
