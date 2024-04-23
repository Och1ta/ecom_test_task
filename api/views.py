from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.permissions import IsAdminOrReadOnly
from api.serializers import EquipmentSerializer, StockSerializer, CategorySerializer, UserSerializer
from users.models import User
from warehouses.models import Equipment, Stock, Category


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="Retrieve a list of users")
    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of all users.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve a specific user")
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve details of a specific user.
        """
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create a new user")
    def create(self, request, *args, **kwargs):
        """
        Create a new user.
        """
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Update an existing user")
    def update(self, request, *args, **kwargs):
        """
        Update an existing user.
        """
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Partial update of a user")
    def partial_update(self, request, *args, **kwargs):
        """
        Partial update of a user.
        """
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Delete a user")
    def destroy(self, request, *args, **kwargs):
        """
        Delete a user.
        """
        return super().destroy(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    @swagger_auto_schema(operation_summary="Retrieve a list of categories")
    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of all categories.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve a specific category")
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve details of a specific category.
        """
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create a new category")
    def create(self, request, *args, **kwargs):
        """
        Create a new category.
        """
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Update an existing category")
    def update(self, request, *args, **kwargs):
        """
        Update an existing category.
        """
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Partial update of a category")
    def partial_update(self, request, *args, **kwargs):
        """
        Partial update of a category.
        """
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Delete a category")
    def destroy(self, request, *args, **kwargs):
        """
        Delete a category.
        """
        return super().destroy(request, *args, **kwargs)


class StockViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing stock information.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdminOrReadOnly]

    @swagger_auto_schema(operation_summary="Retrieve a list of stock information")
    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of all stock information.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve specific stock information")
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve details of specific stock information.
        """
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create new stock information")
    def create(self, request, *args, **kwargs):
        """
        Create new stock information.
        """
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Update existing stock information")
    def update(self, request, *args, **kwargs):
        """
        Update existing stock information.
        """
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Partial update of stock information")
    def partial_update(self, request, *args, **kwargs):
        """
        Partial update of stock information.
        """
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Delete stock information")
    def destroy(self, request, *args, **kwargs):
        """
        Delete stock information.
        """
        return super().destroy(request, *args, **kwargs)


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing equipment information.
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminOrReadOnly]

    @swagger_auto_schema(operation_summary="Retrieve a list of equipment")
    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of all equipment.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve specific equipment")
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve details of specific equipment.
        """
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create new equipment")
    def create(self, request, *args, **kwargs):
        """
        Create new equipment.
        """
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Update existing equipment")
    def update(self, request, *args, **kwargs):
        """
        Update existing equipment.
        """
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Partial update of equipment")
    def partial_update(self, request, *args, **kwargs):
        """
        Partial update of equipment.
        """
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Delete equipment")
    def destroy(self, request, *args, **kwargs):
        """
        Delete equipment.
        """
        return super().destroy(request, *args, **kwargs)
