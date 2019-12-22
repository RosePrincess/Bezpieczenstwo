from django.shortcuts import get_object_or_404, redirect, render
from transfers.forms import TransferForm
from transfers.models import PreparedTransfer, Transfer

from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt


def transfer_sending(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            form.save(sender=request.user)
            return redirect('transfer_confirm')
    else:
        form = TransferForm()

    context = {
        'form': form
    }

    return render(request, 'transfer.html', context)

def transfer_confirmed(request):
    prepared_transfers = []

    for item in PreparedTransfer.objects.all():
        if item.sender_id == request.user.id:
            prepared_transfers.append(item)
    t = prepared_transfers[-1]
    if request.method == 'POST':

        Transfer.objects.create(receiver_name=t.receiver_name, receiver_account=t.receiver_account,
                                    title=t.title, amount=t.amount, sender=t.sender, confirm=False)
        t.delete()
        return redirect('transfer_sent')

    context = {
        'transfer': t
    }
    return render(request, 'transfer_confirm.html', context)

def transfer_sent(request):
    transfers = []
    for item in Transfer.objects.all():
        if item.sender_id == request.user.id:
            transfers.append(item)

    transfer = transfers[-1]

    if request.method == 'POST':
        return redirect('home')

    context = {
        'transfer': transfer
    }

    return render(request, 'transfer_sent.html', context)


def transfers_history(request):
    transfers = []
    for item in Transfer.objects.all():
        if item.sender_id == request.user.id:
            transfers.append(item)

    if request.method == 'POST':
        return redirect('home')

    context = {
        'transfers': transfers
    }
    return render(request, 'transfers_history.html', context)

@csrf_exempt
@user_passes_test(lambda user: user.is_superuser)
def admin_transfers_to_confirm(request):
    transfers = []
    for item in Transfer.objects.all():
        if item.confirm == False:
            transfers.append(item)

    if request.method == 'POST':
        print("________")
        print(request.POST['transfer'])
        print("________")
        return redirect('confirm_transfer', transfer_id=request.POST['transfer'])

    context = {
        'transfers': transfers
    }
    return render(request, 'admin_transfers_to_confirm.html', context)

@csrf_exempt
@user_passes_test(lambda user: user.is_superuser)
def admin_confirm_transfer(request, transfer_id):
    id = get_object_or_404(Transfer, id=transfer_id)
    if request.method == 'POST':
        Transfer.objects.filter(id=id).update(confirm=True)
        return redirect('home')

    return render(request, 'admin_confirm_transfer.html', {'id': id})

@csrf_exempt
@user_passes_test(lambda user: user.is_superuser)
def admin_csrf_attack(request):
    return render(request, 'admin_csrf_attack.html')




