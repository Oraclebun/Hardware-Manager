from django.shortcuts import render, get_object_or_404
from .models import ProbeCard, ProbeCardReport
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, timedelta
from django.contrib.auth.decorators import permission_required, login_required
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from .forms import ProbeCardReportForm, SelectProbeCardModelForm, SelectBBKingPCModelForm, SelectMerlePCModelForm, SelectJoeCPCModelForm, SelectJoeCockerPCModelForm, SelectLesPaulPCModelForm, SelectJaniPCModelForm, SelectWomackPCModelForm, PCInstanceForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    """View function for home page of site."""

    #List probecards editted within a week
    last_editted = ProbeCardReport.objects.order_by('-date_added')[:5]
    one_week = date.today()-timedelta(days=7)
    
    editted_recently = ProbeCardReport.objects.filter(date_added__gte=one_week)
    context = {
        'last_editted' : last_editted,
        'editted_recently' : editted_recently,
        }
    
    #Render the HTML template index.html with the data
    return render(request, 'index.html', context=context)

def active(request):
    """View function for active probecards"""
    
    probecard_active = ProbeCardReport.objects.filter(status_log__exact='a')

    context = {
        'probecard_active' : probecard_active,
        }
    #Render the HTML template index.html with the data
    return render(request, 'stockcontrol/active.html', context=context)

class ProbeCardListView(generic.ListView):
    model = ProbeCard
    paginate_by = 20

class ProbeCardDetailView(generic.DetailView):
    model = ProbeCard


def merle(request):
    """View function for Merle ProbeCards only"""

    merle_pc = ProbeCardReport.objects.filter(probecard__device_name__iexact='merle').order_by('probecard','probehead_rebuild_num')
    context = {
        'merle_pc' : merle_pc,
        }
    return render(request, 'stockcontrol/merle.html', context=context)

def joec(request):
    """View function for JoeC ProbeCards only."""

    joec_pc = ProbeCardReport.objects.filter(probecard__device_name__iexact='joec').order_by('probecard', 'probehead_rebuild_num')

    context = {
        'joec_pc' : joec_pc,
        }
    return render(request, 'stockcontrol/joec.html', context=context)

def joecocker(request):
    """ View function for Joe Cocker Probecards only. """

    joecocker_pc = ProbeCardReport.objects.filter(probecard__device_name__icontains='joe cocker').order_by('probecard', 'probehead_rebuild_num')

    context = {
        'joecocker_pc' : joecocker_pc
        }
    return render(request, 'stockcontrol/joecocker.html', context=context)

def lespaul(request):
    """View function for LesPaul Probecards only"""

    lespaul_pc = ProbeCardReport.objects.filter(probecard__device_name__icontains='lespaul').order_by('probecard', 'probehead_rebuild_num')

    context={
        'lespaul_pc' : lespaul_pc
        }
    return render(request, 'stockcontrol/lespaul.html', context=context)

def jani(request):
    """View function for Jani Probecards only"""

    jani_pc = ProbeCardReport.objects.filter(probecard__device_name__iexact='jani').order_by('probecard', 'probehead_rebuild_num')

    context= {
        'jani_pc' : jani_pc
        }
    return render(request, 'stockcontrol/jani.html', context=context)

def womack(request):
    """ View function for Womack Probecards only."""

    womack_pc = ProbeCardReport.objects.filter(probecard__device_name__iexact='womack').order_by('probecard', 'probehead_rebuild_num')
    context= {
        'womack_pc' : womack_pc
        }
    return render(request, 'stockcontrol/womack.html', context = context)


def bbking(request):
    """ View function for BB King ProbeCards Only"""

    bbking_pc= ProbeCardReport.objects.filter(probecard__device_name__icontains='bb king').order_by('probecard','probehead_rebuild_num')
    context = {
        'bbking_pc': bbking_pc,
        }
    return render(request, 'stockcontrol/bbking.html', context=context)


class MyTasksView(LoginRequiredMixin,TemplateView):
    template_name = 'stockcontrol/tasks.html'


class MyTasksSuccess(LoginRequiredMixin,TemplateView):
    template_name = 'stockcontrol/create_update_success.html'
    
    
class ProbeCardReportCreate(LoginRequiredMixin,CreateView):
    model = ProbeCardReport
    template_name = 'stockcontrol/create_report_form.html'
    form_class = ProbeCardReportForm
    success_url = reverse_lazy('create-update-success')
    
    def get_initial(self):
        self.initial.update({ 'author': self.request.user })
        return self.initial
    
class ProbeCardReportUpdate(LoginRequiredMixin,UpdateView):
    model = ProbeCardReport
    

@login_required
def select_probecard(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        pc_instance_num = request.POST.get('probecard')
                
        # Create a form instance and populate it with data from the request (binding):
        form = SelectProbeCardModelForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('probecard-detail', args=[pc_instance_num]))

    # If this is a GET (or any other method) create the default form.
    else:
        form = SelectProbeCardModelForm()

    context = {
        'form': form,
    }

    return render(request, 'stockcontrol/probecard_select_form.html', context)


@login_required
def select_bbking(request):
    if request.method == 'POST':
        pk=request.POST.get('probecard')
        return HttpResponseRedirect(reverse('pcreport-detail', args=(pk,)))
        #If this is a GEt request, create the default form
    else:
        form = SelectBBKingPCModelForm()
        context = {
            'form' : form,
            }
        return render(request, 'stockcontrol/probecard_select_form.html', context)        


@login_required
def select_merle(request):
    if request.method == 'POST':
        pk=request.POST.get('probecard')
        return HttpResponseRedirect(reverse('pcreport-detail', args=(pk,)))
        #If this is a GEt request, create the default form
    else:
        form = SelectMerlePCModelForm()
        context = {
            'form' : form,
            }
        return render(request, 'stockcontrol/probecard_select_form.html', context)        
    

@login_required
def select_joec(request):
    if request.method == 'POST':
        pk=request.POST.get('probecard')
        return HttpResponseRedirect(reverse('pcreport-detail', args=(pk,)))
        #If this is a GET request, create the default form
    else:
        form = SelectJoeCPCModelForm()
        context = {
            'form' : form,
            }
        return render(request, 'stockcontrol/probecard_select_form.html', context)        


@login_required
def select_joecocker(request):
    if request.method == 'POST':
        pk=request.POST.get('probecard')
        return HttpResponseRedirect(reverse('pcreport-detail', args=(pk,)))
        #If this is a GET request, create the default form
    else:
        form = SelectJoeCockerPCModelForm()
        context = {
            'form' : form,
            }
        return render(request, 'stockcontrol/probecard_select_form.html', context)


@login_required
def select_lespaul(request):
    if request.method == 'POST':
        pk = request.POST.get('probecard')
        return HttpResponseRedirect(reverse('pcreport-detail', args=(pk,)))
    else:
        form = SelectLesPaulPCModelForm()
        context = {
            'form' : form,
            }
        return render(request, 'stockcontrol/probecard_select_form.html', context)


@login_required
def select_jani(request):
    if request.method == 'POST':
        pk = request.POST.get('probecard')
        return HttpResponseRedirect(reverse('pcreport-detail', args=(pk,)))
    else:
        form = SelectJaniPCModelForm()
        context = {
            'form' : form,
            }
        return render(request, 'stockcontrol/probecard_select_form.html', context)


@login_required    
def select_womack(request):
    if request.method == 'POST':
        pk = request.POST.get('probecard')
        return HttpResponseRedirect(reverse('pcreport-detail', args = (pk,)))
    else:
        form = SelectWomackPCModelForm()
        context = {
            'form' : form,
            }
        return render(request, 'stockcontrol/probecard_select_form.html', context)
    

class UpdateReport(LoginRequiredMixin,UpdateView):
    model = ProbeCardReport
    form_class = PCInstanceForm
    template_name = 'stockcontrol/edit_report_form.html'
    success_url = reverse_lazy('create-update-success')

    def get_initial(self):
        self.initial.update({ 'author': self.request.user })
        return self.initial
