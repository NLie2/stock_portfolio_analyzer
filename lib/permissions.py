from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsOwnerOrReadOnly(BasePermission):

  def has_object_permission(self, request, view, obj):
    # Check to see if the request is read-only (so if it is part of safe methods)
    if request.method in SAFE_METHODS: return True

    # Else we check if the user on request is the same as the user on our obj.
    return request.user == obj.user

class IsOwner(BasePermission):
  
  def has_object_permission(self, request, view, obj):
    # Else we check if the user on request is the same as the user on our obj.
    print(request.user, obj.user)
    return request.user == obj.user