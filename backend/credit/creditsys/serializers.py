from rest_framework import serializers
from .models import Loan , Applicant
# from .models import  Applicant

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        # fields = ['id','First_Name','Last_Name','Age','Phone_Number','Monthly_Salary','Approved_Limit',]
        fields = ['id','First_Name','Last_Name','Age','Phone_Number','Monthly_Salary','Approved_Limit',]


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        # fields = ['id','Loan_ID','Loan_Amount','Tenure','Interest_Rate','Monthly_Payment','EMIs_paid_on_Time', 'Date_of_Approval' , 'End_date']
        fields = ['Applicant_name','Loan_ID','Loan_Amount','Tenure','Interest_Rate','Monthly_Payment','EMIs_paid_on_Time', 'Date_of_Approval' , 'End_date']

