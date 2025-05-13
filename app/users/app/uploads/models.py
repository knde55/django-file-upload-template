# uploads/models.py
from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    status = models.CharField(
        choices=[('pending', '待审核'), ('approved', '已通过'), ('rejected', '已拒绝')],
        default='pending'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
