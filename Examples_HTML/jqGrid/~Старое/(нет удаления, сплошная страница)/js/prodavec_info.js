fetch('http://localhost:4388/ham/odata/Prodavec?$expand=prodagi')
    .then(response => response.json())
    .then(response => 
        $(function () 
        {
            const data = [];
            const colName = [
                { name: "ID" },
                { name: "fIO" },
                { name: "Telefon" },
                { name: "Prinyat" },
                { name: "DataRogdeniya" },
                { name: "Prodagi" }
            ];
            
            let i = 0;
            while (i < response.value.length){
                if (response.value[i].prodagi != '[]'){
                    prodagi = response.value[i].Prodagi.length
                } else{
                    prodagi = 'Продаж нет'
                }

                data.push({id: i+1, ID: response.value[i].$id, fIO: response.value[i].FIO, Telefon: response.value[i].Telefon, Prinyat: response.value[i].Prinyat, DataRogdeniya: response.value[i].DataRogdeniya, Prodagi: prodagi });
                i++;
            };

            "use strict";
                $("#grid").jqGrid({   
                    colModel: colName, 
                    data: data,
                });
        })
    )
