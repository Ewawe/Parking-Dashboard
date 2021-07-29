from . import models


class dashboard:
    def compile(customer_id):
        context = {}
        models.Parkinglog.objects.filter(customer_id=customer_id)

        return context

    def parked_today(customer_id):


        return {'today' : 0}

class parking_history:
    def compile(customer_id):
        context = {}
        models.Parkinglog.objects.filter(customer_id=customer_id)

        return context

    def parked_today(customer_id):


        return {'today' : 0}


    