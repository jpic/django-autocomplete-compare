from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse

from .forms import S2ItemForm, AlItemForm
from .models import Item


class ItemFormMixin(object):
    template_name = 'form.html'
    model = Item

    def get_form(self, form_class=None):
        form = super(ItemFormMixin, self).get_form(form_class=form_class)

        if not form.instance.pk:
            form.instance.owner = self.request.user

        return form

class S2FormMixin(object):
    form_class = S2ItemForm

    def get_success_url(self):
        return reverse('s2_item_update', args=(self.object.pk,))


class S2UpdateView(LoginRequiredMixin, ItemFormMixin, S2FormMixin,
        generic.UpdateView):
    pass


class S2CreateView(LoginRequiredMixin, ItemFormMixin, S2FormMixin,
        generic.CreateView):
    pass


class AlFormMixin(object):
    form_class = AlItemForm

    def get_form(self, form_class=None):
        form = super(AlFormMixin, self).get_form(form_class=form_class)

        # Activate request in AL validation
        form.fields['parent'].request = self.request

        return form

    def get_success_url(self):
        return reverse('al_item_update', args=(self.object.pk,))


class AlCreateView(LoginRequiredMixin, ItemFormMixin, AlFormMixin,
        generic.CreateView):
    pass


class AlUpdateView(LoginRequiredMixin, ItemFormMixin, AlFormMixin,
        generic.UpdateView):
    pass
