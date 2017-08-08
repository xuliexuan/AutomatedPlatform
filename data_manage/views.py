#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import import_glucose_from_csv
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .forms import (
    GlucoseImportForm,
)

logger = logging.getLogger(__name__)


@login_required
def import_data(request):
    if request.method == 'POST':
        form = GlucoseImportForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                logger.info('Importing data from uploaded CSV file for user: %s',
                            request.user)
                import_glucose_from_csv(request.user, request.FILES['file'])
            except ValueError as e:
                logger.error('Could not import data from uploaded CSV file for'
                             ' user: %s. Details: %s', request.user, e)
                message = 'Could not import your data. Make sure that it follows' \
                          ' the suggested format. (Error Details: %s)' % e
                messages.add_message(request, messages.WARNING, message)
                return render(request, 'data_manage/data_import.html', {'form': form})
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = GlucoseImportForm()

    return render(request, 'data_manage/data_import.html', {'form': form})


@login_required
def dashboard(request):
    """
    Displays the glucose data table for the currently logged in user. A form
    for quickly adding glucose values is also included.

    The data is loaded by the GlucoseListJson view and rendered by the
    Datatables plugin via Javascript.
    """
    # form = GlucoseQuickAddForm()
    # form.fields['category'].initial = get_initial_category(request.user)
    #
    #
    # return render(request, 'core/dashboard.html', {'form': form,
    #                                                'glucose_unit_name': request.user.settings.glucose_unit.name})
    return render(request, 'core/dashboard.html')