from rest_framework.decorators import api_view
from rest_framework.response import Response
from bson.objectid import ObjectId

# Create your views here.
from money_manager_api.models import Person, Wallet
from transactions_mongo.models import IncomeTransaction
from transactions_mongo.serializers import IncomeTransactionSerializer


# {
#     'user': <user_name>
# }
@api_view(['POST'])
def get_income_transactions(request):
    transactions = IncomeTransaction.objects.using("mongodb").filter(user=request.data['user'], removed__in=[False])
    serialized_transactions = IncomeTransactionSerializer(transactions, many=True)
    return Response(serialized_transactions.data)


# {
#     'user': <user-name>,
#     'to-wallet': <to-wallet>,
#     'income-name': <income-name>,
#     'amount': <amount>,
# }
@api_view(['POST'])
def create_income_transaction(request):
    wallet = Wallet.objects.get(person_id=Person.objects.get(user_name=request.data['user']).pk,
                                wallet=request.data['to-wallet'])
    wallet.amount = request.data['amount'] + wallet.amount
    wallet.save()

    transaction = IncomeTransaction(user=request.data['user'],
                                    to_wallet=request.data['to-wallet'],
                                    income=request.data['income-name'],
                                    amount=request.data['amount'])
    transaction.save(using="mongodb")
    return Response({"operation": "success"})


# {
#     '_id': <id>
# }
@api_view(['POST'])
def remove_income_transaction(request):
    transaction = IncomeTransaction.objects.using("mongodb").get(pk=ObjectId(request.data['_id']))
    wallet = Wallet.objects.using("default").get(wallet=transaction.to_wallet, person__user_name=transaction.user)

    wallet.amount = wallet.amount - transaction.amount
    transaction.removed = True

    wallet.save(using="default")
    transaction.save(using="mongodb")
    return Response({"operation": "success"})
