from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def hello_check_api_view(request):
    if request.method == "GET":
        return Response(
            {"msg":"Server Running"}
        )