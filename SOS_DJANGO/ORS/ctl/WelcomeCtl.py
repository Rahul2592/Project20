from django.shortcuts import render

from .BaseCtl import BaseCtl


class WelcomeCtl(BaseCtl):
    def display(self,  request, params = {}):
        print("---------Welcome----------", self, request)
        return render(request, self.get_template())

    def get_template(self):
        return "Welcome.html"
