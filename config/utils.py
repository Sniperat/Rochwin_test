from django.http import HttpResponse


def send_swagger_file(request):
    with open("openapi/schema.yaml", "r", encoding="utf-8", newline="") as swagger_file:
        return HttpResponse(swagger_file.read(), content_type="text/yaml")
