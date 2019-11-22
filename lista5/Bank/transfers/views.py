from django.shortcuts import render, redirect
from transfers.forms import TransferForm
from transfers.models import PreparedTransfer, Transfer

# Create your views here.

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
                                    title=t.title, amount=t.amount, sender=t.sender)
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
