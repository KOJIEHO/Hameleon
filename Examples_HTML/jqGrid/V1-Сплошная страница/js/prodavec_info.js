fetch('http://localhost:4388/ham/odata/Prodavec?$expand=prodagi')
    .then(response => response.json())
    .then(response => 
        $(function () 
        {
            const data = [];
            const colName = [
                { name: "ID", width:70, align:'center'},
                { name: "FIO", width:300, align:'center'},
                { name: "Telefon", width:150, align:'center'},
                { name: "Prinyat", width:200, align:'center'},
                { name: "DataRogdeniya", width:200, align:'center'},
                { name: "Prodagi", width:70, align:'center'}
            ];
            
            let i = 0;
            while (i < response.value.length){
                if (response.value[i].prodagi != '[]'){
                    prodagi = response.value[i].Prodagi.length
                } else{
                    prodagi = 'Продаж нет'
                }

                data.push({id: i+1, ID: response.value[i].$id, FIO: response.value[i].FIO, Telefon: response.value[i].Telefon, Prinyat: response.value[i].Prinyat, DataRogdeniya: response.value[i].DataRogdeniya, Prodagi: prodagi });
                i++;
            };

            "use strict";
                $("#grid").jqGrid({   
                    colModel: colName, 
                    data: data,
                    ondblClickRow: function(rowId){
                        var rowData = jQuery(this).getRowData(rowId);
                        window.location.href = "prodavec_update.html?idUser=" + String(rowData.ID) + "&fioUser=" + String(rowData.FIO) + "&telefonUser=" + String(rowData.Telefon) + "&prinyatUser=" + String(rowData.Prinyat) + "&dataRogdeniyaUser=" + String(rowData.DataRogdeniya)                       
                    }
                });
        })
    )
