from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import NetworkForm, FlowspecForm
from .models import Network, Flowspec

import requests
from django.http import JsonResponse

import os

# Set the FastNetMon API endpoint and authentication details
DEFAULT_API_ENDPOINT = "http://127.0.0.1:10007"
DEFAULT_API_USER = "fnmadmin"
DEFAULT_API_PASSWORD = "fnmpassword"

FNM_API_ENDPOINT = os.environ.get('FNM_API_ENDPOINT',DEFAULT_API_ENDPOINT)
FNM_API_USER = os.environ.get('FNM_API_USER',DEFAULT_API_USER)
FNM_API_PASSWORD = os.environ.get('FNM_API_PASSWORD',DEFAULT_API_PASSWORD)

@login_required
def home(request):
    return render(request, "home.html")

@login_required
def help(request):
    return render(request, "help.html")

@login_required
def network(request):
    # A HTTP POST?
    if request.method == "POST":
        form = NetworkForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            network = form.save(commit=False)
            network.save()
            messages.success(request, "You have successfully assigned a network.")
            # Redirect to home (/)
            return redirect("/network/")
        else:
            # The supplied form contained errors - just print them to the terminal.
            messages.error(request, form.errors)
            return redirect("/network/")
    else:
        # If the request was not a POST, display the form to enter details.
        form = NetworkForm()
        # Also populate the table with existing networks
        networks = Network.objects.all()
    return render(request, "network.html", {"form": form, "networks": networks})

@login_required
def network_delete(request):
    if request.method == "POST":
        w = Network.objects.get(id=request.POST["network_id"])
        w.delete()
    return redirect("/network/")

@login_required
def flowspec(request):
    # A HTTP POST?
    form = FlowspecForm(user=request.user)
    if request.method == "POST":
        form = FlowspecForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            flowspec = form.save(commit=False)
            flowspec.save()
            print("Flowspec passes validation")
            messages.success(request, "You have sucessfully commited a Flowspec rule.")
    # Also populate the table with existing networks
    flowspecs = Flowspec.objects.filter(net__user=request.user)
    return render(request, "flowspec.html", {"form": form, "flowspecs": flowspecs})

@login_required
def flowspec_toggle(request):
    if request.method == "POST":
        w = Flowspec.objects.get(id=request.POST["flowspec_id"])
        if w.active == True:
            if remove_flowspec_route(w):
                w.active = False
                w.save()
        elif w.active == False:
            if insert_flowspec_route(w):
                w.active = True
                w.save()
    return redirect("/flowspec/")

@login_required
def flowspec_redeploy(request):
    if request.method == "POST":
      rules = Flowspec.objects.filter(net__user=request.user)
      for rule in rules:
          if rule.active == True:
              insert_flowspec_route(rule)
    return redirect("/flowspec/")

@login_required
def flowspec_flush(request):
    if request.method == "POST":
      #nets = Network.objects.all(id__=request.user)
      rules = Flowspec.objects.filter(net__user=request.user)
      for rule in rules: 
          if remove_flowspec_route(rule):
              rule.active = False
              rule.save()
    return redirect("/flowspec/")

@login_required
def flowspec_delete(request):
    if request.method == "POST":
        w = Flowspec.objects.get(id=request.POST["flowspec_id"])
        if not w.active:
            w.delete()
        else:
            messages.warning(
                request,
                "You need to disable the Flowspec rule first.",
                extra_tags="flowspec_table",
            )
    return redirect("/flowspec/")


def insert_flowspec_route(rule):

    # Set the flowspec mandatory route details
    route = {
        "destination_prefix": rule.dstip,
        "action_type": rule.action,
    }

    # add the flowspec optional route details
    if rule.srcip:
        route["source_prefix"] = rule.srcip
    if rule.srcprt > 0:
        route["source_ports"] = [rule.srcprt]
    if rule.dstprt > 0:
        route["destination_ports"] = [rule.dstprt]
    if rule.protocol:
        route["protocols"] = [rule.protocol]

    # Make the API call to insert the flowspec route
    response = requests.put(
        f"{FNM_API_ENDPOINT}/flowspec",
        json=route,
        auth=(FNM_API_USER, FNM_API_PASSWORD),
    )
    # Check if the API call was successful
    if response.status_code == 200:
        return True
    return False


def remove_flowspec_route(rule):
    
    # Make the API call to insert the flowspec route
    response = requests.get(
        f"{FNM_API_ENDPOINT}/flowspec",
        auth=(FNM_API_USER, FNM_API_PASSWORD),
    )

    # Set the flowspec mandatory route details
    route = {
        "destination_prefix": rule.dstip,
        "action_type": rule.action,
    }

    # add the flowspec optional route details
    if rule.srcip:
        route["source_prefix"] = rule.srcip
    if rule.srcprt > 0:
        route["source_ports"] = [rule.srcprt]
    if rule.dstprt > 0:
        route["destination_ports"] = [rule.dstprt]
    if rule.protocol:
        route["protocols"] = [rule.protocol]

    print(route)

    uuid = None
    for value in response.json()["values"]:
        if value["announce"] == route:
            uuid = value["uuid"]
            break
    else:
        # notfound
        return True

    print(uuid)

    response = requests.delete(
        f"{FNM_API_ENDPOINT}/flowspec/{uuid}",
        auth=(FNM_API_USER, FNM_API_PASSWORD),
    )

    # Check if the API call was successful
    if response.status_code == 200:
        return True
    return False