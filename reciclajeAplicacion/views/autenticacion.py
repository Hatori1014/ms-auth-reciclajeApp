from rest_framework import status, views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from reciclajeAplicacion.serializers.autenticacionSerializer import AutenticacionSerializer
from reciclajeAplicacion.models.autenticacion import Autenticacion


class AutenticacionDetailView(generics.RetrieveAPIView):
    queryset = Autenticacion.objects.all()
    serializer_class = AutenticacionSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class AutenticacionListView(generics.ListAPIView):
    queryset = Autenticacion.objects.all()
    serializer_class = AutenticacionSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class AutenticacionCreateView(generics.CreateAPIView):
    queryset = Autenticacion.objects.all()
    serializer_class = AutenticacionSerializer

    def post(self, request, *args, **kwargs):
        serializer = AutenticacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"username":request.data["username"],
        "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


class AutenticacionUpdateView(generics.UpdateAPIView):
    queryset = Autenticacion.objects.all()
    serializer_class = AutenticacionSerializer
    #permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

class AutenticacionDeleteView(generics.DestroyAPIView):
    serializer_class = AutenticacionSerializer
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Autenticacion.objects.all()

    def delete(self, request, pk=None):
        user = self.get_queryset().filter(id=pk).first()
        if user:
            super().delete(pk)
            return Response(True)
        return Response(False)






     