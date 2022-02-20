from rest_framework.decorators import api_view
from rest_framework.response import Response
from bson.objectid import ObjectId

# Create your views here.
from core.models import Person, Wallet
from transactions.models import IncomeTransaction, SpendingTransaction
from transactions.serializers import IncomeTransactionSerializer, SpendingTransactionSerializer


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


# {
#     'user': <user_name>
# }
@api_view(['POST'])
def get_spending_transactions(request):
    transactions = SpendingTransaction.objects.using("mongodb").filter(user=request.data['user'], removed__in=[False])
    serialized_transactions = SpendingTransactionSerializer(transactions, many=True)
    return Response(serialized_transactions.data)


# {
#     'user': <user-name>,
#     'from-wallet': <from-wallet>,
#     'spending-name': <spending-name>,
#     'amount': <amount>,
# }
@api_view(['POST'])
def create_spending_transaction(request):
    from_wallet = Wallet.objects.get(person_id=Person.objects.get(user_name=request.data['user']).pk,
                                     wallet=request.data['from-wallet'])
    from_wallet.amount = from_wallet.amount - request.data['amount']
    from_wallet.save()

    transaction = SpendingTransaction(user=request.data['user'],
                                      from_wallet=request.data['from-wallet'],
                                      spending=request.data['spending-name'],
                                      amount=request.data['amount'])
    transaction.save(using="mongodb")
    return Response({"operation": "success"})


# {
#     '_id': <id>
# }
@api_view(['POST'])
def remove_spending_transaction(request):
    transaction = SpendingTransaction.objects.using("mongodb").get(pk=ObjectId(request.data['_id']))
    wallet = Wallet.objects.using("default").get(wallet=transaction.from_wallet, person__user_name=transaction.user)

    wallet.amount = wallet.amount + transaction.amount
    transaction.removed = True

    wallet.save(using="default")
    transaction.save(using="mongodb")
    return Response({"operation": "success"})
