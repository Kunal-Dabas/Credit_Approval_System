from django.shortcuts import render
from django.http import JsonResponse
from .models import Loan , Applicant
from .serializers import LoanSerializer , ApplicantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.


@api_view( ['GET' , 'POST'])
def Loan_list(request):
    if( request.method == 'GET'):
        Loans = Loan.objects.all()
        L_serializer = LoanSerializer(Loans , many = True)
        return JsonResponse(L_serializer.data , safe = False)
    if( request.method == 'POST'):
        L_serializer = LoanSerializer( data = request.data)
        if ( L_serializer.is_valid()):
            L_serializer.save()
            return Response( L_serializer.data , status = status.HTTP_201_CREATED )
        else:
            return Response( L_serializer.data , status= status.HTTP_403_FORBIDDEN )

@api_view( ['GET' , 'POST'])
def Applicant_list(request):
    if( request.method == 'GET'):
        Applicants = Applicant.objects.all()
        App_serializer = ApplicantSerializer(Applicants , many = True)
        return JsonResponse(App_serializer.data , safe = False )

    if( request.method == 'POST'):
        request.data['Approved_Limit'] = str( 36 * float( request.data.get('Monthly_Salary')))
        App_serializer = ApplicantSerializer( data = request.data)
        if App_serializer.is_valid():
            App_serializer.save()
            return Response( App_serializer.data , status = status.HTTP_201_CREATED )
        else:
            return Response( App_serializer.data , status = status.HTTP_206_PARTIAL_CONTENT)
   
@api_view( [ 'GET'])            
def Loan_details(request , id):
    print(f"Received id: {id}")
    try:
        My_loan = Loan.objects.get( pk = id )
    except Loan.DoesNotExist:
        return Response( status = status.HTTP_404_NOT_FOUND)
    
    if ( request.method == 'GET'):
        L_serialized  = LoanSerializer( My_loan )
        return Response( L_serialized.data  )
    
@api_view( [ 'GET'])            
def LoanID_details(request , Loan_ID):
    print(f"Received id: {Loan_ID}")
    My_loan = get_object_or_404(Loan, Loan_ID=Loan_ID)
    if ( request.method == 'GET'):
        L_serialized  = LoanSerializer( My_loan )
        return Response( L_serialized.data  )

@api_view( ['POST'])
def Create_loan(request):
        loanamount = int( request.data.get('Loan_Amount'))
        tenur = int( request.data.get('Tenure'))
        interest = float( request.data.get('Interest_Rate'))
        m = (((loanamount*interest)/100 + loanamount)/tenur)/12
        request.data['Monthly_Payment'] = str(m)
        
        App_serializer = LoanSerializer( data = request.data)

        if App_serializer.is_valid():
            App_serializer.save()
            return Response( App_serializer.data , status = status.HTTP_201_CREATED )
        else:
            return Response( App_serializer.data , status = status.HTTP_201_CREATED)