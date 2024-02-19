from django.db import models
import uuid
import random
# Create your models here.

class Applicant(models.Model):
    First_Name = models.CharField(max_length=100 , null = True)
    Last_Name = models.CharField(max_length=100 , null = True)
    Age = models.CharField(max_length=15 , null = True)
    Phone_Number = models.IntegerField( null = True)
    Monthly_Salary = models.IntegerField(null = True)
    Approved_Limit = models.IntegerField( null = True)


class Loan(models.Model):
    Applicant_name = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    Loan_ID = models.IntegerField( blank = True) 
    Loan_Amount = models.IntegerField( default = 0)
    Tenure = models.IntegerField( default = 0) 
    Interest_Rate = models.DecimalField(max_digits=4, decimal_places=2, default=8.0) 
    Monthly_Payment = models.IntegerField( default = 0) 
    EMIs_paid_on_Time = models.IntegerField(default=0)
    Date_of_Approval = models.DateTimeField(null=True, blank=True)
    End_date = models.DateTimeField(null=True, blank=True)










# class Applicant(models.Model):
#     id = models.IntegerField( primary_key = True)
#     First_Name = models.CharField(max_length=100 , null = True)
#     Last_Name = models.CharField(max_length=100 , null = True)
#     Age = models.CharField(max_length=100 , null = True)
#     Phone_Number = models.CharField(max_length=15 , null = True)
#     Monthly_Salary = models.DecimalField(max_digits=10, decimal_places=2 , null = True)
#     Approved_Limit = models.DecimalField(max_digits=10, decimal_places=2 , null = True)
    
# class Loan(models.Model):
#     Applicant_name = models.ForeignKey(Applicant, on_delete=models.CASCADE)
#     Loan_ID = models.IntegerField(primary_key=True , blank = True , default = 0) 
#     Loan_Amount = models.DecimalField(max_digits=10, decimal_places=2 , default = 0)
#     Tenure = models.IntegerField( default = 0) 
#     Interest_Rate = models.DecimalField(max_digits=4, decimal_places=2, default=8.0) 
#     Monthly_Payment = models.DecimalField(max_digits=10, decimal_places=2 , default = 0) 
#     EMIs_paid_on_Time = models.IntegerField(default=0)
#     Date_of_Approval = models.DateTimeField(null=True, blank=True)
#     End_date = models.DateTimeField(null=True, blank=True)
