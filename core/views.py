from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


from core.models import Wallet, Person, Income, Spending
from core.serializers import WalletSerializer, IncomeSerializer, SpendingSerializer


# {
#     "user": <username>
# }
@api_view(['POST'])
def get_wallets(request):
    wallets = Wallet.objects.filter(person__user_name=request.data['user'], removed=False)
    if wallets.exists():
        wallet_serializer = WalletSerializer(wallets, many=True)
        return Response(wallet_serializer.data)
    else:
        return Response({"details": "User has no wallets"})


# {
#     "user":<username>,
#     'wallet-name':<wallet-name>
# }
@api_view(['POST'])
def create_wallet(request):
    new_wallet = Wallet(person_id=Person.objects.get(user_name=request.data['user']).pk,
                        wallet=request.data['wallet-name'])
    new_wallet.save()
    return Response({"operation": "success"})


# {
#     "user":<username>,
#     'wallet-name':<wallet-name>
# }
@api_view(['POST'])
def remove_wallet(request):
    wallet = Wallet.objects.get(person_id=Person.objects.get(user_name=request.data['user']).pk,
                                wallet=request.data['wallet-name'])
    wallet.removed = True
    wallet.save()
    return Response({"operation": "success"})


# {
#     "user":<username>,
#     "from":<wallet-name>,
#     "to":<wallet-name>,
#     "amount": <amount>
# }
@api_view(['POST'])
def transfer(request):
    from_wallet = Wallet.objects.get(person_id=Person.objects.get(user_name=request.data['user']).pk,
                                     wallet=request.data['from'])
    from_wallet.amount = from_wallet.amount - request.data['amount']

    to_wallet = Wallet.objects.get(person_id=Person.objects.get(user_name=request.data['user']).pk,
                                   wallet=request.data['to'])
    to_wallet.amount = to_wallet.amount + request.data['amount']

    from_wallet.save()
    to_wallet.save()

    return Response({"operation": "success"})


# {
#     "user": <username>
# }
@api_view(['POST'])
def get_income(request):
    income = Income.objects.filter(person__user_name=request.data['user'], removed=False)
    if income.exists():
        income_serializer = IncomeSerializer(income, many=True)
        return Response(income_serializer.data)
    else:
        return Response({"details": "User has no income"})


# {
#     "user":<username>,
#     "income-name":<income-name>
# }
@api_view(['POST'])
def create_income(request):
    new_income = Income(person_id=Person.objects.get(user_name=request.data['user']).pk,
                        income=request.data['income-name'])
    new_income.save()
    return Response({"operation": "success"})


# {
#     "user":<username>,
#     "income-name":<income-name>
# }
@api_view(['POST'])
def remove_income(request):
    income = Income.objects.get(person_id=Person.objects.get(user_name=request.data['user']).pk,
                                income=request.data['income-name'])
    income.removed = True
    income.save()
    return Response({"operation": "success"})


# {
#     "user": <username>
# }
@api_view(['POST'])
def get_spending(request):
    spending = Spending.objects.filter(person__user_name=request.data['user'], removed=False)
    if spending.exists():
        spending_serializer = SpendingSerializer(spending, many=True)
        return Response(spending_serializer.data)
    else:
        return Response({"details": "User has no income"})


# {
#     "user":<username>,
#     "spending-name":<spending-name>
# }
@api_view(['POST'])
def create_spending(request):
    new_spending = Spending(person_id=Person.objects.get(user_name=request.data['user']).pk,
                            spending=request.data['spending-name'])
    new_spending.save()
    return Response({"operation": "success"})


# {
#     "user":<username>,
#     "spending-name":<spending-name>
# }
@api_view(['POST'])
def remove_spending(request):
    spending = Spending.objects.get(person_id=Person.objects.get(user_name=request.data['user']).pk,
                                    spending=request.data['spending-name'])
    spending.removed = True
    spending.save()
    return Response({"operation": "success"})
