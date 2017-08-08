from django.shortcuts import render

# Create your views here.



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