import autocomplete_light.shortcuts as al

from .models import Item


class ItemAutocomplete(al.AutocompleteModelBase):
    choices = Item.objects.all()

    def choices_for_request(self):
        if getattr(self, 'request', None):
            user = getattr(self.request, 'user', None)

            if user and user.pk:
                return Item.objects.filter(owner=user)

        return Item.objects.none()
al.register(ItemAutocomplete)
