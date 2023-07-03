from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rent, Car, Person, ContactUs
from .serializers import ContactSerializer, PersonSerializer, CarSerializer
from django.contrib.auth.hashers import make_password

@api_view(['GET', 'POST'])
def serve_contactus(request):
    if request.method == 'GET':
        contact_id = request.query_params.get('id', False)
        many = False
        if contact_id:
            try:
                contact = ContactUs.objects.get(id=contact_id)
            except:
                return Response({'error': 'id is not exist in the system'}, 500)
        else:
            many = True
            contact = ContactUs.objects.all()
        res = ContactSerializer(instance=contact, many=many)
        return Response(res.data)
    if request.method == 'POST':
        contact = ContactSerializer(data=request.data)
        if contact.is_valid():
            contact = contact.save()
            return Response({"message": f'we"ve recieved your message \n post id:{contact.id}'}, 200)
        else:
            return Response({"status": "not ok", "errors" : contact.errors}, 400)

@api_view(['GET', 'POST', 'PUT'])
def serve_person(request):
     if request.method == 'GET':
        has_car = request.query_params.get('has_car', False)
        person_id = request.query_params.get('id', False)
        many = False
        if person_id:
            try:
                    person = Person.objects.get(id=person_id)
            except:
                return Response({'error': 'id is not exist in the system'}, 500)
        elif has_car:
            person = Person.objects.all()
            person = [p for p in person if p.car_set.all()]
            many = True
        else:
            many = True
            person = Person.objects.all()
        res = PersonSerializer(instance=person, many=many)
        return Response(res.data)
     elif request.method == 'POST':
        person = PersonSerializer(data=request.data)
        if person.is_valid():
            password = person.validated_data.get('password')
            person = person.save(password=make_password(password))
            return Response('Person added succesfully', 200)
        else:
            return Response({"message":'person wasn"t added', "error": person.errors}, 400)
     elif request.method == 'PUT':
            user_id = request.query_params.get("id", False)
            if user_id:
                try:
                    user = Person.objects.get(id=user_id)
                except Exception as e:
                    return Response({"status": "not ok", "error": str(e)}, 400)
                user = PersonSerializer( instance=user, data=request.data, partial=True)
                if user.is_valid():
                    user.save()
                    return Response({"status": "ok", "info": "added succesfully"}, 200)
                else:
                    return Response({"status":"not ok", "errors": user.errors}, 400)
@api_view(['GET', 'DELETE', 'PUT', 'POST'])                
def serve_car(request):
    try:
        if request.method == 'GET':
            car_id = request.query_params.get('id', False)
            if car_id:
                car = Car.objects.get(id = car_id)
                many = False
            else:
                car = Car.objects.all()
                many = True
            car = CarSerializer(instance=car, many=many)
            return Response(car.data)
        elif request.method == 'POST':
            car = CarSerializer(data=request.data)
            if car.is_valid():
                car = car.save()
                return Response({"status": "Success", "info" : f"car added succesfully \n ticket id :{car.id}"}, 200)
            else:
                return Response({"status": "Failed", "error": car.errors}, 400)

        elif request.method == 'PUT':
            car_id = request.query_params.get('id', False)
            if car_id:
                car = Car.objects.get(id=car_id)
                car = CarSerializer(instance=car, data=request.data, partial=True)
                if car.is_valid():
                    car = car.save()
                    return Response({"status": 'succes', "info": f"car id {car.id} updated succesfully"}, 200)
                else:
                    return Response({'status':"failed", "errors": car.errors}, 400)
                
        elif request.method == 'DELETE':
            car_id = request.query_params.get('id', False)
            if car_id:
                car = Car.objects.get(id=car_id)
                car.delete()
                return Response({"status": "succes", "info": "car was deleted succesfully"}, 200)
            else:
                return Response({"status": "Failed", "info": "car wasn't able to get deleted"}, 400)

    except Exception as e:
        return Response({"status": "Failed", "error": str(e)}, 500)