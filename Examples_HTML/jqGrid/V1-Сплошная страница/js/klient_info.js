fetch('http://localhost:4388/ham/odata/Klient?$expand=pokupki/mashiny,pokupki/prodavec')
    .then(response => response.json())
    .then(response => 
        $(function () 
        {            
            const data = [];
            const colName = [
                { name: "ID", width:70, align:'center'},
                { name: "FIO", width:300, align:'center'},
                { name: "Pasport", width:150, align:'center'},
                { name: "Orga", width:200, align:'center'},
                { name: "Telefon", width:200, align:'center'}
            ];

            let i = 0;
            while (i < response.value.length){
                data.push({id: i+1, ID: response.value[i].$id, FIO: response.value[i].FIO, Pasport: response.value[i].Pasport, Orga: response.value[i].Organizaciya, Telefon: response.value[i].Telefon });
                i++;
            };

            "use strict";
                $("#grid").jqGrid({
                    colModel: colName, 
                    data: data,
                    ondblClickRow: function(rowId){
                        var rowData = jQuery(this).getRowData(rowId);
                        window.location.href = "klient_update.html?idUser=" + String(rowData.ID) + "&fioUser=" + String(rowData.FIO) + "&pasportUser=" + String(rowData.Pasport) + "&orgaUser=" + String(rowData.Orga) + "&telefonUser=" + String(rowData.Telefon)                      
                    }
                });
        })   
    )