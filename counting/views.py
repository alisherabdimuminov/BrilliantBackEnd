from datetime import datetime
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Model, Face, Worker
from .serializers import ModelSerializer, FaceModelSerializer, WorkerModelSerializer


# Inputs

@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def get_inputs_count_by_date(request: HttpRequest):
    today = datetime.today()
    day = request.GET.get("day")
    month = request.GET.get("month")
    year = request.GET.get("year")
    inputs_obj = None
    if day and month and year:
        inputs_obj = Model.objects.filter(created__day=day, created__month=month, created__year=year, type="input").order_by("-id")
    else:
        inputs_obj = Model.objects.filter(created__day=today.day, created__month=today.month, created__year=today.year, type="input").order_by("-id")
    if not inputs_obj:
        return Response({
            "status": "error",
            "errors": {
                "model": "model not found",
            },
            "data": {},
        })
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "count": inputs_obj.count()
        }
    })


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def get_inputs_by_date(request: HttpRequest):
    today = datetime.today()
    day = request.GET.get("day")
    month = request.GET.get("month")
    year = request.GET.get("year")
    inputs_obj = None
    if day and month and year:
        inputs_obj = Model.objects.filter(created__day=day, created__month=month, created__year=year, type="input").order_by("-id")
    else:
        inputs_obj = Model.objects.filter(created__day=today.day, created__month=today.month, created__year=today.year, type="input").order_by("-id")
    if not inputs_obj:
        return Response({
            "status": "error",
            "errors": {
                "model": "model not found",
            },
            "data": {},
        })
    inputs = ModelSerializer(inputs_obj, many=True)
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "inputs": inputs.data,
        }
    })


@api_view(http_method_names=["POST"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def post_inputs(request: HttpRequest):
    data = request.data
    inputs = ModelSerializer(Model, data=data)
    if inputs.is_valid():
        inputs.create(inputs.validated_data)
        return Response({
            "status": "success",
            "errors": {},
            "data": {
                "message": "Saved.",
            }
        })
    else:
        print(inputs.errors)
        return Response({
            "status": "error",
            "errors": {
                "error": "Failed to save",
            },
            "data": {},
        })
    

# Outputs

@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def get_outputs_count_by_date(request: HttpRequest):
    today = datetime.today()
    day = request.GET.get("day")
    month = request.GET.get("month")
    year = request.GET.get("year")
    outputs_obj = None
    if day and month and year:
        outputs_obj = Model.objects.filter(created__day=day, created__month=month, created__year=year, type="output").order_by("-id")
    else:
        outputs_obj = Model.objects.filter(created__day=today.day, created__month=today.month, created__year=today.year, type="output").order_by("-id")
    if not outputs_obj:
        return Response({
            "status": "error",
            "errors": {
                "model": "model not found",
            },
            "data": {},
        })
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "count": outputs_obj.count()
        }
    })


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def get_outputs_by_date(request: HttpRequest):
    today = datetime.today()
    day = request.GET.get("day")
    month = request.GET.get("month")
    year = request.GET.get("year")
    outputs_obj = None
    if day and month and year:
        outputs_obj = Model.objects.filter(created__day=day, created__month=month, created__year=year, type="output").order_by("-id")
    else:
        outputs_obj = Model.objects.filter(created__day=today.day, created__month=today.month, created__year=today.year, type="output").order_by("-id")
    if not outputs_obj:
        return Response({
            "status": "error",
            "errors": {
                "model": "model not found",
            },
            "data": {},
        })
    outputs = ModelSerializer(outputs_obj, many=True)
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "outputs": outputs.data,
        }
    })
    

@api_view(http_method_names=["POST"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def post_outputs(request: HttpRequest):
    data = request.data
    output = ModelSerializer(Model, data=data)
    if output.is_valid():
        output.create(output.validated_data)
        return Response({
            "status": "success",
            "errors": {},
            "data": {
                "message": "Saved.",
            }
        })
    else:
        return Response({
            "status": "error",
            "errors": {
                "error": "Failed to save",
            },
            "data": {},
        })
    

# Gruop Inputs

@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def get_group_inputs_count_by_date(request: HttpRequest):
    today = datetime.today()
    day = request.GET.get("day")
    month = request.GET.get("month")
    year = request.GET.get("year")
    group_inputs_obj = None
    if day and month and year:
        group_inputs_obj = Model.objects.filter(created__day=day, created__month=month, created__year=year, type="group_input").order_by("-id")
    else:
        group_inputs_obj = Model.objects.filter(created__day=today.day, created__month=today.month, created__year=today.year, type="group_input").order_by("-id")
    if not group_inputs_obj:
        return Response({
            "status": "error",
            "errors": {
                "model": "model not found",
            },
            "data": {},
        })
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "count": group_inputs_obj.count()
        }
    })


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def get_group_inputs_by_date(request: HttpRequest):
    today = datetime.today()
    day = request.GET.get("day")
    month = request.GET.get("month")
    year = request.GET.get("year")
    group_inputs_obj = None
    if day and month and year:
        group_inputs_obj = Model.objects.filter(created__day=day, created__month=month, created__year=year, type="group_input").order_by("-id")
    else:
        group_inputs_obj = Model.objects.filter(created__day=today.day, created__month=today.month, created__year=today.year, type="group_input").order_by("-id")
    if not group_inputs_obj:
        return Response({
            "status": "error",
            "errors": {
                "model": "model not found",
            },
            "data": {},
        })
    group_inputs = ModelSerializer(group_inputs_obj, many=True)
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "group_inputs": group_inputs.data,
        }
    })
    

@api_view(http_method_names=["POST"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def post_group_inputs(request: HttpRequest):
    data = request.data
    group_inputs = ModelSerializer(Model, data=data)
    if group_inputs.is_valid():
        group_inputs.create(group_inputs.validated_data)
        return Response({
            "status": "success",
            "errors": {},
            "data": {
                "message": "Saved.",
            }
        })
    else:
        return Response({
            "status": "error",
            "errors": {
                "error": "Failed to save",
            },
            "data": {},
        })


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def all_by_date(request: HttpRequest):
    today = datetime.today()
    day = request.GET.get("day")
    month = request.GET.get("month")
    year = request.GET.get("year")
    group_inputs_obj = None
    if day and month and year:
        group_inputs_obj = Model.objects.filter(created__day=day, created__month=month, created__year=year).order_by("-id")
    else:
        group_inputs_obj = Model.objects.filter(created__day=today.day, created__month=today.month, created__year=today.year).order_by("-id")
    if not group_inputs_obj:
        return Response({
            "status": "error",
            "errors": {
                "model": "model not found",
            },
            "data": {},
        })
    group_inputs = ModelSerializer(group_inputs_obj, many=True)
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "all": group_inputs.data,
        }
    })


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def get_statistics_by_date(request: HttpRequest):
    today = datetime.today()
    day = request.GET.get("day")
    month = request.GET.get("month")
    year = request.GET.get("year")
    inputs_obj = None
    outputs_obj = None
    group_inputs_obj = None
    start = 8
    end = 20
    statistics = []
    for i in range(start, end + 1):
        if day and month and year:
            inputs_obj = Model.objects.filter(created__day=day, created__month=month, created__year=year, created__hour=i, type="input")
            outputs_obj = Model.objects.filter(created__day=day, created__month=month, created__year=year, created__hour=i, type="output")
            group_inputs_obj = Model.objects.filter(created__day=day, created__month=month, created__year=year, created__hour=i, type="group_input")
        else:
            inputs_obj = Model.objects.filter(created__day=today.day, created__month=today.month, created__year=today.year, created__hour=i, type="input")
            outputs_obj = Model.objects.filter(created__day=today.day, created__month=today.month, created__year=today.year, created__hour=i, type="output")
            group_inputs_obj = Model.objects.filter(created__day=today.day, created__month=today.month, created__year=today.year, created__hour=i, type="group_input")
        statistics.append({
            "x": i,
            "y1": inputs_obj.count(),
            "y2": outputs_obj.count(),
            "y3": group_inputs_obj.count(),
        })

    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "statistics": statistics,
        }
    })



@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def get_faces(request: HttpRequest):
    today = datetime.today()
    day = request.GET.get("day")
    month = request.GET.get("month")
    year = request.GET.get("year")
    worker = request.GET.get("worker")
    faces_obj = None
    if day and month and year:
        if worker:
            worker = Worker.objects.get(pk=worker)
            faces_obj = Face.objects.filter(created__day=day, created__month=month, created__year=year, worker=worker)
        else:
            faces_obj = Face.objects.filter(created__day=day, created__month=month, created__year=year)
    else:
        if worker:
            worker = Worker.objects.get(pk=worker)
            faces_obj = Face.objects.filter(created__day=today.day, created__month=today.month, created__year=today.year, worker=worker)
        else:
            faces_obj = Face.objects.filter(created__day=today.day, created__month=today.month, created__year=today.year)
    faces = FaceModelSerializer(faces_obj, many=True)
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "faces": faces.data,
        }
    })



@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def get_workers(request: HttpRequest):
    workers_obj = Worker.objects.all()
    workers = WorkerModelSerializer(workers_obj, many=True)
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "workers": workers.data
        },
    })


@api_view(http_method_names=["POST"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def create_worker_face(request: HttpRequest):
    uuid = request.data.get("uuid")
    image = request.FILES.get("image")
    worker = Worker.objects.filter(uuid=uuid)
    if worker:
        worker = worker.first()
        face = Face.objects.create(
            worker=worker,
            type="worker",
            image=image
        )
        return Response({
            "status": "success",
            "errors": {},
            "data": {
                "message": "Saved!"
            }
        })
    else:
        return Response({
            "status": "error",
            "errors": "Worker not found",
            "data": {},
        })
    

@api_view(http_method_names=["POST"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def create_customer_face(request: HttpRequest):
    image = request.FILES.get("image")
    face = Face.objects.create(
        type="customer",
        image=image
    )
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "message": "Saved!"
        }
    })
