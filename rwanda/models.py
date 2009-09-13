#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.db import models
from people.models import *

class Pregnant(Person):
    date_last_menses =   models.DateField("Date of Last menses", blank=True ,null=True)
#    def __init__(self,**kwargs) :
#        #add persontype.
 #       persontype ,isno = PersonType.objects.get_or_create(singular="Pregnant Woman" , plural="Pregnant Women")
#
        #print persontype
        #self.type_id = persontype.id
#        super(Person,self).__init__(**kwargs)
       
       
       
class Child(Person):
    weight =   models.DecimalField("weight",decimal_places=2,max_digits=6, blank=True ,null=True)
#    def __init__(self,**kwargs):
#        #add persontype.
#        persontype ,isno = PersonType.objects.get_or_create(singular="Child" , plural="Children")
#            
#        self.type_id = persontype.id
#        super(Person,self).__init__(**kwargs)
